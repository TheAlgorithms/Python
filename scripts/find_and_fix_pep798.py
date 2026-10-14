#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///

"""
Find (and optionally fix) opportunities to use PEP 798 in Python source files.

PEP 798 allows unpacking inside comprehensions and generator expressions:
https://peps.python.org/pep-0798/

The following flattening patterns are detected:

    [y for x in xs for y in x]                      ->  [*x for x in xs]
    {y for x in xs for y in x}                      ->  {*x for x in xs}
    (y for x in xs for y in x)                      ->  (*x for x in xs)
    {k: v for d in ds for k, v in d.items()}        ->  {**d for d in ds}

Only the simplest, always-equivalent forms are rewritten: exactly two ``for``
clauses, no ``async``, and no ``if`` filter on the inner clause.  Nested
candidates are fixed innermost first; re-run the script to catch any leftovers.
The rewritten source uses Python 3.15+ syntax, so fixed files need 3.15+.

Usage:
    scripts/find_and_fix_pep798.py [--fix] PATH [PATH ...]

Without ``--fix`` the script only reports and exits with status 1 if any
opportunities were found.
"""

import argparse
import ast
import sys
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from pathlib import Path

Comprehension = ast.ListComp | ast.SetComp | ast.GeneratorExp | ast.DictComp

# Nodes that need parentheses after ``*`` or ``**`` (they bind looser than ``|``).
_NEEDS_PARENS_AFTER_STAR = (
    ast.BoolOp,
    ast.Compare,
    ast.IfExp,
    ast.Lambda,
    ast.NamedExpr,
    ast.UnaryOp,
)
# Nodes that need parentheses inside a ``for ... in`` / ``if`` comprehension clause.
_NEEDS_PARENS_IN_CLAUSE = (ast.IfExp, ast.Lambda, ast.NamedExpr, ast.Yield)


@dataclass(frozen=True)
class Finding:
    """A PEP 798 opportunity: a source span and its replacement text."""

    line: int
    start: int
    end: int
    old: str
    new: str


def _is_name(node: ast.expr, name: str) -> bool:
    return isinstance(node, ast.Name) and node.id == name


def _is_flattening(node: Comprehension) -> bool:
    """
    Return True if the comprehension is a simple two-level flattening.

    >>> def check(code: str) -> bool:
    ...     return _is_flattening(ast.parse(code, mode="eval").body)
    >>> check("[y for x in xs for y in x]")
    True
    >>> check("[y for x in xs if x for y in x]")
    True
    >>> check("[y for x in xs for y in x if y]")
    False
    >>> check("[y + 1 for x in xs for y in x]")
    False
    >>> check("[y for x in xs]")
    False
    >>> check("{k: v for d in ds for k, v in d.items()}")
    True
    >>> check("{k: v for d in ds for k, v in d.items() if v}")
    False
    >>> check("{k: v for d in ds for v, k in d.items()}")
    False
    >>> check("{k: v for d in ds for k, v in d.items(1)}")
    False
    """
    if len(node.generators) != 2:
        return False
    outer, inner = node.generators
    if outer.is_async or inner.is_async or inner.ifs:
        return False
    if isinstance(node, ast.DictComp):
        match inner.target, node.key, node.value, inner.iter:
            case (
                ast.Tuple(elts=[ast.Name(id=a), ast.Name(id=b)]),
                ast.Name(id=key),
                ast.Name(id=value),
                ast.Call(func=ast.Attribute(attr="items"), args=[], keywords=[]),
            ):
                return a != b and (a, b) == (key, value)
        return False
    return isinstance(inner.target, ast.Name) and _is_name(node.elt, inner.target.id)


class _Offsets:
    """Convert AST (line, UTF-8 byte column) positions to string offsets."""

    def __init__(self, source: str) -> None:
        self.lines = source.splitlines(keepends=True)
        self.line_starts = [0]
        for line in self.lines:
            self.line_starts.append(self.line_starts[-1] + len(line))

    def offset(self, line: int, byte_col: int) -> int:
        text = self.lines[line - 1].encode()[:byte_col].decode()
        return self.line_starts[line - 1] + len(text)


def _segment(source: str, offsets: _Offsets, node: ast.expr, parens: tuple) -> str:
    start = offsets.offset(node.lineno, node.col_offset)
    end = offsets.offset(node.end_lineno, node.end_col_offset)
    text = source[start:end]
    return f"({text})" if isinstance(node, parens) else text


def _replacement(source: str, offsets: _Offsets, node: Comprehension) -> str:
    outer, inner = node.generators
    star = "**" if isinstance(node, ast.DictComp) else "*"
    iterable = inner.iter
    if isinstance(node, ast.DictComp):
        iterable = iterable.func.value
    unpacked = _segment(source, offsets, iterable, _NEEDS_PARENS_AFTER_STAR)
    target = _segment(source, offsets, outer.target, ())
    outer_iter = _segment(source, offsets, outer.iter, _NEEDS_PARENS_IN_CLAUSE)
    clauses = [f"for {target} in {outer_iter}"]
    clauses += [
        f"if {_segment(source, offsets, cond, _NEEDS_PARENS_IN_CLAUSE)}"
        for cond in outer.ifs
    ]
    start = offsets.offset(node.lineno, node.col_offset)
    end = offsets.offset(node.end_lineno, node.end_col_offset)
    return f"{source[start]}{star}{unpacked} {' '.join(clauses)}{source[end - 1]}"


def _span(offsets: _Offsets, node: ast.AST) -> tuple[int, int]:
    return (
        offsets.offset(node.lineno, node.col_offset),
        offsets.offset(node.end_lineno, node.end_col_offset),
    )


def find_opportunities(source: str) -> list[Finding]:
    """
    Return non-overlapping PEP 798 opportunities, innermost candidates first.

    >>> [f.new for f in find_opportunities("[y for x in xs for y in x]")]
    ['[*x for x in xs]']
    >>> find_opportunities("[y for y in ys]")
    []
    >>> len(find_opportunities("a = [y for x in xs for y in x]\\nb = {*x for x in xs}"))
    1
    """
    tree = ast.parse(source)
    offsets = _Offsets(source)
    candidates = [
        node
        for node in ast.walk(tree)
        if isinstance(node, Comprehension) and _is_flattening(node)
    ]
    # Innermost (smallest) first so that nested candidates keep the inner fix.
    candidates.sort(key=lambda node: _span(offsets, node)[1] - _span(offsets, node)[0])
    taken: list[tuple[int, int]] = []
    findings: list[Finding] = []
    for node in candidates:
        start, end = _span(offsets, node)
        if any(start < t_end and t_start < end for t_start, t_end in taken):
            continue
        taken.append((start, end))
        findings.append(
            Finding(
                line=node.lineno,
                start=start,
                end=end,
                old=source[start:end],
                new=_replacement(source, offsets, node),
            )
        )
    return sorted(findings, key=lambda finding: finding.start)


def fix_source(source: str) -> str:
    """
    Rewrite every opportunity found by :func:`find_opportunities`.

    >>> print(fix_source("x = [y for ys in yss for y in ys]"))
    x = [*ys for ys in yss]
    >>> print(fix_source("x = {k: v for d in ds if d for k, v in d.items()}"))
    x = {**d for d in ds if d}
    """
    for finding in reversed(find_opportunities(source)):
        source = f"{source[: finding.start]}{finding.new}{source[finding.end :]}"
    return source


def iter_python_files(paths: Iterable[Path]) -> Iterator[Path]:
    for path in paths:
        if path.is_dir():
            yield from sorted(path.rglob("*.py"))
        else:
            yield path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("paths", nargs="+", type=Path, help="files or directories")
    parser.add_argument("--fix", action="store_true", help="rewrite files in place")
    args = parser.parse_args(argv)

    total = 0
    for path in iter_python_files(args.paths):
        source = path.read_text(encoding="utf-8")
        try:
            findings = find_opportunities(source)
        except SyntaxError as error:
            print(f"{path}: skipped ({error.msg})", file=sys.stderr)
            continue
        for finding in findings:
            print(f"{path}:{finding.line}: {finding.old!r} -> {finding.new!r}")
        total += len(findings)
        if findings and args.fix:
            path.write_text(fix_source(source), encoding="utf-8")
    print(f"{total} PEP 798 opportunit{'y' if total == 1 else 'ies'} found")
    return 0 if args.fix or not total else 1


if __name__ == "__main__":
    sys.exit(main())
