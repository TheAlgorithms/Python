#!/usr/bin/env python3
"""Refresh the Hacktoberfest 2026 open-PR cleanup tracker.

This script is run once a day by the ``hacktoberfest_prep`` GitHub Actions
workflow (see ``.github/workflows/hacktoberfest_prep.yml``). It:

1. Reads ``docs/hacktober_2026_prep.md`` and, for every tracked pull request
   that is still an unchecked ``[ ]`` box, checks whether the PR has since
   been merged or closed. Resolved rows are ticked (``[ ]`` -> ``[x]``) and
   annotated with ``merged`` / ``closed``.
2. Rewrites a machine-generated ``## Automated statistics`` section at the end
   of the file with the current number of open issues and open pull requests
   and the top three algorithm directories that have the most open pull
   requests labelled ``awaiting reviews``.
3. Exits non-zero once Hacktoberfest 2026 has begun (on or after
   2026-10-01, UTC), so the prep window closing is loud rather than silent.

It only uses the standard library and the ``GITHUB_TOKEN`` provided by the
Actions runner, so there is nothing to install.
"""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

REPO = os.environ.get("GITHUB_REPOSITORY", "TheAlgorithms/Python")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
API = "https://api.github.com"
TRACKER = "docs/hacktober_2026_prep.md"
AWAITING_LABEL = "awaiting reviews"
HACKTOBERFEST_START = dt.date(2026, 10, 1)

# A tracked row looks like: ``12. [ ] #15144 awaiting reviews``
ROW_RE = re.compile(
    r"^(?P<idx>\d+)\.\s+\[(?P<mark>[ x])\]\s+#(?P<pr>\d+)\b(?P<rest>.*)$"
)
STATS_HEADER = "## Automated statistics"


def _request(url: str) -> tuple[dict | list, dict]:
    """GET ``url`` and return ``(json_body, headers)``, retrying on 403/rate limit."""
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "hacktoberfest-prep-bot",
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    for attempt in range(4):
        req = urllib.request.Request(url, headers=headers)  # noqa: S310
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:  # noqa: S310
                return json.load(resp), dict(resp.headers)
        except urllib.error.HTTPError as exc:
            remaining = exc.headers.get("X-RateLimit-Remaining")
            if exc.code in (403, 429) and remaining == "0":
                reset = int(exc.headers.get("X-RateLimit-Reset", "0"))
                wait = max(1, reset - int(time.time())) + 1
                print(f"Rate limited; sleeping {wait}s", file=sys.stderr)
                time.sleep(min(wait, 90))
                continue
            if exc.code >= 500 and attempt < 3:
                time.sleep(2 * (attempt + 1))
                continue
            raise
    msg = f"giving up on {url}"
    raise RuntimeError(msg)


def _search_count(query: str) -> int:
    url = f"{API}/search/issues?q={urllib.parse.quote(query)}&per_page=1"
    body, _ = _request(url)
    return int(body.get("total_count", 0))  # type: ignore[union-attr]


def pr_state(number: int) -> str | None:
    """Return ``"merged"`` / ``"closed"`` for a resolved PR, else ``None``."""
    body, _ = _request(f"{API}/repos/{REPO}/pulls/{number}")
    if body.get("state") == "open":  # type: ignore[union-attr]
        return None
    return "merged" if body.get("merged_at") else "closed"  # type: ignore[union-attr]


def top_awaiting_directories(
    limit: int = 3, max_prs: int = 400
) -> list[tuple[str, int]]:
    """Count open ``awaiting reviews`` PRs by the top-level directory they touch."""
    query = f'repo:{REPO} is:pr is:open label:"{AWAITING_LABEL}"'
    counts: dict[str, int] = {}
    page = 1
    scanned = 0
    while scanned < max_prs:
        url = (
            f"{API}/search/issues?q={urllib.parse.quote(query)}"
            f"&per_page=100&page={page}"
        )
        body, _ = _request(url)
        items = body.get("items", [])  # type: ignore[union-attr]
        if not items:
            break
        for item in items:
            number = item["number"]
            files, _ = _request(f"{API}/repos/{REPO}/pulls/{number}/files?per_page=100")
            dirs = set()
            for changed in files:  # type: ignore[union-attr]
                parts = changed["filename"].split("/")
                if len(parts) > 1 and not parts[0].startswith("."):
                    dirs.add(parts[0])
            for directory in dirs:
                counts[directory] = counts.get(directory, 0) + 1
            scanned += 1
            if scanned >= max_prs:
                break
        if len(items) < 100:
            break
        page += 1
    ranked = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    return ranked[:limit]


def refresh_checkboxes(lines: list[str]) -> tuple[list[str], int]:
    """Tick rows whose PR is now merged/closed. Returns (new_lines, n_updated)."""
    updated = 0
    out: list[str] = []
    for line in lines:
        match = ROW_RE.match(line)
        if not match or match.group("mark") == "x":
            out.append(line)
            continue
        state = pr_state(int(match.group("pr")))
        if state is None:
            out.append(line)
            continue
        out.append(f"{match.group('idx')}. [x] #{match.group('pr')} {state}")
        updated += 1
    return out, updated


def build_stats_block() -> str:
    open_issues = _search_count(f"repo:{REPO} is:issue is:open")
    open_prs = _search_count(f"repo:{REPO} is:pr is:open")
    awaiting = _search_count(f'repo:{REPO} is:pr is:open label:"{AWAITING_LABEL}"')
    today = dt.datetime.now(dt.UTC).date().isoformat()
    top_dirs = top_awaiting_directories()

    lines = [
        STATS_HEADER,
        "",
        f"_Generated automatically by "
        f"`scripts/hacktoberfest_prep_update.py` on {today} (UTC)._",
        "",
        f"- **Open issues:** {open_issues}",
        f"- **Open pull requests:** {open_prs}",
        f"- **Open PRs labelled `{AWAITING_LABEL}`:** {awaiting}",
        "",
        "**Top three directories to work on** (most open pull requests labelled "
        f"`{AWAITING_LABEL}`):",
        "",
    ]
    if top_dirs:
        for rank, (directory, count) in enumerate(top_dirs, start=1):
            plural = "PR" if count == 1 else "PRs"
            lines.append(f"{rank}. `{directory}/` — {count} awaiting-reviews {plural}")
    else:
        lines.append("_No open `awaiting reviews` pull requests found._")
    lines.append("")
    return "\n".join(lines)


def splice_stats(text: str, stats_block: str) -> str:
    idx = text.find(STATS_HEADER)
    head = text[:idx].rstrip("\n") if idx != -1 else text.rstrip("\n")
    return f"{head}\n\n{stats_block}\n"


def main() -> int:
    with open(TRACKER, encoding="utf-8") as handle:
        text = handle.read()

    body_before_stats = text.split(STATS_HEADER, 1)[0]
    lines = body_before_stats.splitlines()
    lines, n_updated = refresh_checkboxes(lines)
    body = "\n".join(lines)

    stats_block = build_stats_block()
    new_text = splice_stats(body, stats_block)

    with open(TRACKER, "w", encoding="utf-8") as handle:
        handle.write(new_text)

    print(f"Checked off {n_updated} newly-resolved pull request(s).")

    today = dt.datetime.now(dt.UTC).date()
    if today >= HACKTOBERFEST_START:
        print(
            f"Hacktoberfest 2026 has begun ({today} >= {HACKTOBERFEST_START}); "
            "the prep window is over — failing on purpose so this job is retired.",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
