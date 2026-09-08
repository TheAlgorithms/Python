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

The slow part of the job is looking at the files touched by every open
``awaiting reviews`` PR (potentially a few hundred of them). Those requests
have no dependencies on one another, so they are fired concurrently through a
single ``httpx2.AsyncClient`` with a bounded concurrency limit — this turns a
long series of round-trips into a handful of batches and cuts the runtime from
~16 minutes to well under a minute. Progress is reported to stderr as it goes
so a human watching the Actions log can see it is alive.

It only needs ``httpx2`` (the repo-standard HTTP client) and the
``GITHUB_TOKEN`` provided by the Actions runner.
"""

import asyncio
import datetime as dt
import os
import re
import sys
import time

import httpx2

REPO = os.environ.get("GITHUB_REPOSITORY", "TheAlgorithms/Python")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
API = "https://api.github.com"
TRACKER = "docs/hacktober_2026_prep.md"
AWAITING_LABEL = "awaiting reviews"
HACKTOBERFEST_START = dt.date(2026, 10, 1)

# How many API requests to keep in flight at once. GitHub's authenticated
# primary limit is 5000/hour, but bursts of concurrent requests can trip the
# secondary limits, so keep this modest.
CONCURRENCY = 8

# A tracked row looks like: ``12. [ ] #15144 awaiting reviews``
ROW_RE = re.compile(
    r"^(?P<idx>\d+)\.\s+\[(?P<mark>[ x])\]\s+#(?P<pr>\d+)\b(?P<rest>.*)$"
)
STATS_HEADER = "## Automated statistics"


def _log(message: str) -> None:
    """Emit a progress line to stderr, flushed so Actions shows it live."""
    print(message, file=sys.stderr, flush=True)


def _headers() -> dict[str, str]:
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "hacktoberfest-prep-bot",
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    return headers


async def _request(
    client: httpx2.AsyncClient,
    sem: asyncio.Semaphore,
    url: str,
    params: dict | None = None,
) -> tuple[dict | list, dict]:
    """GET ``url`` and return ``(json_body, headers)``, retrying on 403/rate limit.

    The semaphore bounds how many of these run concurrently.
    """
    async with sem:
        for attempt in range(4):
            resp = await client.get(url, params=params)
            if resp.is_success:
                return resp.json(), dict(resp.headers)
            remaining = resp.headers.get("X-RateLimit-Remaining")
            if resp.status_code in (403, 429) and remaining == "0":
                reset = int(resp.headers.get("X-RateLimit-Reset", "0"))
                wait = max(1, reset - int(time.time())) + 1
                _log(f"Rate limited on {url}; sleeping {min(wait, 90)}s")
                await asyncio.sleep(min(wait, 90))
                continue
            if resp.status_code >= 500 and attempt < 3:
                await asyncio.sleep(2 * (attempt + 1))
                continue
            resp.raise_for_status()
        msg = f"giving up on {url}"
        raise RuntimeError(msg)


async def _search_count(
    client: httpx2.AsyncClient, sem: asyncio.Semaphore, query: str
) -> int:
    body, _ = await _request(
        client, sem, f"{API}/search/issues", {"q": query, "per_page": 1}
    )
    return int(body.get("total_count", 0))  # type: ignore[union-attr]


async def pr_state(
    client: httpx2.AsyncClient, sem: asyncio.Semaphore, number: int
) -> str | None:
    """Return ``"merged"`` / ``"closed"`` for a resolved PR, else ``None``."""
    body, _ = await _request(client, sem, f"{API}/repos/{REPO}/pulls/{number}")
    if body.get("state") == "open":  # type: ignore[union-attr]
        return None
    return "merged" if body.get("merged_at") else "closed"  # type: ignore[union-attr]


async def top_awaiting_directories(
    client: httpx2.AsyncClient,
    sem: asyncio.Semaphore,
    limit: int = 3,
    max_prs: int = 400,
) -> list[tuple[str, int]]:
    """Count open ``awaiting reviews`` PRs by the top-level directory they touch."""
    query = f'repo:{REPO} is:pr is:open label:"{AWAITING_LABEL}"'
    numbers: list[int] = []
    page = 1
    while len(numbers) < max_prs:
        body, _ = await _request(
            client,
            sem,
            f"{API}/search/issues",
            {"q": query, "per_page": 100, "page": page},
        )
        items = body.get("items", [])  # type: ignore[union-attr]
        if not items:
            break
        numbers.extend(item["number"] for item in items)
        if len(items) < 100:
            break
        page += 1
    numbers = numbers[:max_prs]

    total = len(numbers)
    _log(f"Scanning changed files for {total} '{AWAITING_LABEL}' PR(s)...")
    done = 0

    async def dirs_for(number: int) -> set[str]:
        nonlocal done
        files, _ = await _request(
            client, sem, f"{API}/repos/{REPO}/pulls/{number}/files", {"per_page": 100}
        )
        dirs = set()
        for changed in files:  # type: ignore[union-attr]
            parts = changed["filename"].split("/")
            if len(parts) > 1 and not parts[0].startswith("."):
                dirs.add(parts[0])
        done += 1
        if done % 25 == 0 or done == total:
            _log(f"  ...scanned {done}/{total} PR(s)")
        return dirs

    results = await asyncio.gather(*(dirs_for(n) for n in numbers))

    counts: dict[str, int] = {}
    for dirs in results:
        for directory in dirs:
            counts[directory] = counts.get(directory, 0) + 1
    ranked = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    return ranked[:limit]


async def refresh_checkboxes(
    client: httpx2.AsyncClient, sem: asyncio.Semaphore, lines: list[str]
) -> tuple[list[str], int]:
    """Tick rows whose PR is now merged/closed. Returns (new_lines, n_updated)."""
    # Collect the PR numbers of every still-unchecked tracked row, then look
    # their states up concurrently.
    pending = [
        int(match.group("pr"))
        for line in lines
        if (match := ROW_RE.match(line)) and match.group("mark") != "x"
    ]
    if pending:
        _log(f"Checking {len(pending)} open tracker row(s) for resolution...")
    states = dict(
        zip(
            pending,
            await asyncio.gather(*(pr_state(client, sem, n) for n in pending)),
        )
    )

    updated = 0
    out: list[str] = []
    for line in lines:
        match = ROW_RE.match(line)
        if not match or match.group("mark") == "x":
            out.append(line)
            continue
        state = states.get(int(match.group("pr")))
        if state is None:
            out.append(line)
            continue
        out.append(f"{match.group('idx')}. [x] #{match.group('pr')} {state}")
        updated += 1
    return out, updated


async def build_stats_block(client: httpx2.AsyncClient, sem: asyncio.Semaphore) -> str:
    _log("Collecting open issue/PR counts...")
    awaiting_query = f'repo:{REPO} is:pr is:open label:"{AWAITING_LABEL}"'
    open_issues, open_prs, awaiting = await asyncio.gather(
        _search_count(client, sem, f"repo:{REPO} is:issue is:open"),
        _search_count(client, sem, f"repo:{REPO} is:pr is:open"),
        _search_count(client, sem, awaiting_query),
    )
    today = dt.datetime.now(dt.UTC).date().isoformat()

    lines = [
        STATS_HEADER,
        "",
        (
            f"_Generated automatically by "
            f"`scripts/hacktoberfest_prep_update.py` on {today} (UTC)._"
        ),
        "",
        f"- **Open issues:** {open_issues}",
        f"- **Open pull requests:** {open_prs}",
        f"- **Open PRs labelled `{AWAITING_LABEL}`:** {awaiting}",
        "",
        (
            "**Top three directories to work on** (most open pull requests "
            f"labelled `{AWAITING_LABEL}`):"
        ),
        "",
    ]
    if top_dirs := await top_awaiting_directories(client, sem):
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


async def compute(lines: list[str]) -> tuple[list[str], int, str]:
    """Do all the network work: resolve tracker rows and build the stats block."""
    async with httpx2.AsyncClient(headers=_headers(), timeout=30) as client:
        sem = asyncio.Semaphore(CONCURRENCY)
        lines, n_updated = await refresh_checkboxes(client, sem, lines)
        stats_block = await build_stats_block(client, sem)
    return lines, n_updated, stats_block


def main() -> int:
    started = time.monotonic()
    with open(TRACKER, encoding="utf-8") as handle:
        text = handle.read()

    body_before_stats = text.split(STATS_HEADER, 1)[0]
    lines = body_before_stats.splitlines()

    lines, n_updated, stats_block = asyncio.run(compute(lines))

    body = "\n".join(lines)
    new_text = splice_stats(body, stats_block)

    with open(TRACKER, "w", encoding="utf-8") as handle:
        handle.write(new_text)

    elapsed = time.monotonic() - started
    print(f"Checked off {n_updated} newly-resolved pull request(s) in {elapsed:.1f}s.")

    today = dt.datetime.now(dt.UTC).date()
    if today >= HACKTOBERFEST_START:
        _log(
            f"Hacktoberfest 2026 has begun ({today} >= {HACKTOBERFEST_START}); "
            "the prep window is over — failing on purpose so this job is retired."
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
