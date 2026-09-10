# Skill: Review an open issue for TheAlgorithms/Python

Triage an open issue — most often one carrying the `bug` label — **together with
every pull request attached to it**, and produce a verdict a maintainer can act on
without re-doing the work. The goal is a review that any triager (human or AI) can
run the same way every time, and that ends in an explicit list of `Closes #NNNNN`
lines the maintainer can paste into a merge commit.

This repo exists to **teach visitors to fix bugs by doing**. So the default is to
merge adequate existing contributor work, not to open a fresh PR that races them.
Only open your own PR when no attached PR adequately solves the issue.

## How to run this skill

### 1. Reproduce before you trust the report

- Check out current `master` and actually **run the failing case** from the issue.
- If it reproduces, say so and paste the minimal reproducer (inputs → observed
  output, e.g. `nan` + a `RuntimeWarning`).
- If you **cannot** confirm it locally — an optional dependency isn't installed,
  the failure needs an external service, the report is too vague — **say that
  explicitly rather than guessing.** "Not reproducible in a vanilla checkout"
  is a real, useful verdict.

### 2. Classify the issue

Sort each issue into one bucket and act accordingly:

- **Confirmed bug with an adequate open PR** → recommend the specific PR to merge.
- **Confirmed bug, no adequate PR** → open a new PR yourself (see step 5).
- **Not a bug / working-as-intended** → recommend closing, and explain why (e.g.
  binary search returning *an* index of a duplicate is correct, not a defect).
- **Feature request mislabeled as a bug** → recommend dropping the `bug` label; do
  **not** close it as a bug.
- **Too vague / needs reporter info** → comment **on the issue itself** asking for
  the one concrete thing missing (a file path, a traceback, a reproducer), and note
  it should be closed if no answer arrives.
- **Environment / optional-dependency, not an algorithm defect** → note it needs
  someone with that environment; it is not fixable in a vanilla checkout.

### 3. Examine every attached PR — pick one, name the duplicates

For a bug with several open PRs:

- **Verify each fix's doctest values numerically** against a trusted reference
  (`scipy`, `numpy.linalg`, `geopy`, or a brute-force check over random inputs).
  Don't take a doctest's word for it — confirm the number.
- Prefer the **first-in PR with the smallest correct diff** that follows repo
  convention (doctests over new test files, `raise` over `assert`, no unrelated
  reindentation or churn of clean doctests into floating-point noise).
- **Reject out-of-scope "fixes"** — e.g. swapping a real divide-by-zero for a
  `1e-15` magic constant makes results implementation-defined. Fix the issue, not
  more.
- Identify the byte-for-byte **duplicates** so the maintainer can close them with
  thanks in the same action.

### 4. Emit the verdict — fixed output shape

Post one comment that a maintainer can act on directly. For each issue give a
one-line rationale and the exact autoclose line. Two formatting rules matter a lot
to human maintainers scanning the thread:

- **Start every line that references an issue or PR with a Markdown list marker
  (`- ` or `* `).** GitHub-flavored Markdown only autolinks `#NNNNN` inside a list,
  and those autolinks are colored — **purple = merged, red = closed, green = open** —
  so the maintainer can see merge/close progress at a glance. A bare `#14813` at the
  start of a line does not autolink.
- **Merging a PR that closes an issue also closes the issue's other open PRs**, so
  fold the duplicates into one autoclose statement rather than listing the winner
  alone:

  ```text
  * #14813 — 3x3 inverse returns the transpose → merge #14821
    (Closes #14813, Closes #14840, Closes #15045)
  ```

Recommended shape:

```text
## Confirmed bugs with an adequate open PR — merge
* #<issue> — <one-line what/why> → merge #<pr> (Closes #<issue>, Closes #<dupe>, …)

## Not a bug / not merge-ready
* #<issue> — <feature-request → relabel | needs cleanup | needs a human call>

## Summary — lines to add
* Closes #<issue> → #<pr>
```

### 5. When you must open your own PR

If no attached PR is adequate, open one — but let the contributors keep the credit
where their work was close. Use autoclose keywords in the **commit message body**
so the merge closes the issue *and* the superseded PRs:

```text
Fixes #12233
Fixes #12262
Fixes #13635
```

Follow the [`new-pull-request`](../new-pull-request/SKILL.md) skill for the
mechanics (synced `master`, named branch, checked description box, untouched
`uv.lock`).

## Tone

Be specific and kind. Name the exact PR and the exact reason, credit the
contributor by handle, and offer runners-up detailed feedback so they learn — the
point of the repo is that people come back and fix the next one.
