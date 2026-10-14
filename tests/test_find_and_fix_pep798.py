from pathlib import Path

import pytest

from scripts.find_and_fix_pep798 import (
    find_opportunities,
    fix_source,
    iter_python_files,
    main,
)


@pytest.mark.parametrize(
    ("before", "after"),
    [
        ("[y for x in xs for y in x]", "[*x for x in xs]"),
        ("{y for x in xs for y in x}", "{*x for x in xs}"),
        ("(y for x in xs for y in x)", "(*x for x in xs)"),
        ("sum(y for x in xs for y in x)", "sum(*x for x in xs)"),
        ("{k: v for d in ds for k, v in d.items()}", "{**d for d in ds}"),
        ("[y for x in xs if x for y in x]", "[*x for x in xs if x]"),
        ("[y for x in xs if x if x.a for y in x]", "[*x for x in xs if x if x.a]"),
        ("[y for x, z in xs for y in x.items]", "[*x.items for x, z in xs]"),
        ("[y for x in xs for y in x or ()]", "[*(x or ()) for x in xs]"),
        ("[y for x in (a if b else c) for y in x]", "[*x for x in (a if b else c)]"),
        ("[y for x in xs for y in (x)]", "[*x for x in xs]"),
        ("[y for x in xs for y in f(x)[0]]", "[*f(x)[0] for x in xs]"),
        ("[y for x in xs for y in x][0]", "[*x for x in xs][0]"),
        ("[é for ü in xs for é in ü]", "[*ü for ü in xs]"),
        ("{k: v for d in ds for k, v in (a or b).items()}", "{**(a or b) for d in ds}"),
    ],
)
def test_fixes(before: str, after: str) -> None:
    assert fix_source(before) == after


@pytest.mark.parametrize(
    "source",
    [
        "[y for y in ys]",
        "[y + 1 for x in xs for y in x]",
        "[z for x in xs for y in x]",
        "[y for x in xs for y in x if y]",
        "[y for x in xs for y in x for z in y]",
        "[x for x in xs for x, y in x]",
        "{k: v for d in ds for k, v in d.items() if v}",
        "{k: v for d in ds for v, k in d.items()}",
        "{k: v for d in ds for k, v in d.items(1)}",
        "{k: v for d in ds for k, v in d}",
        "{k: v for d in ds for k, k in d.items()}",
        "[x for x in xs]",
        "list(itertools.chain.from_iterable(xs))",
    ],
)
def test_no_opportunity(source: str) -> None:
    assert find_opportunities(source) == []
    assert fix_source(source) == source


def test_async_comprehensions_are_ignored() -> None:
    source = (
        "async def f():\n"
        "    return [y async for x in xs for y in x]\n"
        "async def g():\n"
        "    return [y for x in xs async for y in x]\n"
    )
    assert find_opportunities(source) == []


def test_find_reports_line_and_text() -> None:
    source = "a = 1\nb = [y for x in xs for y in x]\n"
    (finding,) = find_opportunities(source)
    assert finding.line == 2
    assert finding.old == "[y for x in xs for y in x]"
    assert finding.new == "[*x for x in xs]"
    assert source[finding.start : finding.end] == finding.old


def test_multiple_findings_in_order() -> None:
    source = (
        "a = [y for x in xs for y in x]\nb = {k: v for d in ds for k, v in d.items()}\n"
    )
    assert fix_source(source) == "a = [*x for x in xs]\nb = {**d for d in ds}\n"


def test_nested_candidates_fix_innermost_only() -> None:
    source = "[w for v in [y for x in xs for y in x] for w in v]"
    (finding,) = find_opportunities(source)
    assert finding.old == "[y for x in xs for y in x]"
    assert fix_source(source) == "[w for v in [*x for x in xs] for w in v]"


def test_multiline_comprehension() -> None:
    source = "result = [\n    y\n    for x in xs\n    for y in x\n]\n"
    assert fix_source(source) == "result = [*x for x in xs]\n"


def test_iter_python_files(tmp_path: Path) -> None:
    (tmp_path / "sub").mkdir()
    first = tmp_path / "a.py"
    second = tmp_path / "sub" / "b.py"
    other = tmp_path / "c.txt"
    for path in (first, second, other):
        path.write_text("")
    assert list(iter_python_files([tmp_path])) == [first, second]
    assert list(iter_python_files([other])) == [other]


def test_main_reports_without_fixing(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    path = tmp_path / "mod.py"
    path.write_text("a = [y for x in xs for y in x]\n")
    assert main([str(path)]) == 1
    output = capsys.readouterr().out
    assert f"{path}:1:" in output
    assert "1 PEP 798 opportunity found" in output
    assert path.read_text() == "a = [y for x in xs for y in x]\n"


def test_main_fix_rewrites_file(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    path = tmp_path / "mod.py"
    path.write_text("a = [y for x in xs for y in x]\nb = {y for x in xs for y in x}\n")
    assert main(["--fix", str(path)]) == 0
    assert path.read_text() == "a = [*x for x in xs]\nb = {*x for x in xs}\n"
    assert "2 PEP 798 opportunities found" in capsys.readouterr().out


def test_main_clean_file_returns_zero(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    path = tmp_path / "mod.py"
    path.write_text("a = [y for y in ys]\n")
    assert main([str(path)]) == 0
    assert "0 PEP 798 opportunities found" in capsys.readouterr().out


def test_main_skips_syntax_errors(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    path = tmp_path / "bad.py"
    path.write_text("def (:\n")
    assert main([str(path)]) == 0
    assert "skipped" in capsys.readouterr().err
