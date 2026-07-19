#!/usr/bin/env bash
set -uo pipefail
cd /app

MODE="${1:-new}"

case "$MODE" in
  base)
    pytest tests  # run existing repo tests
    ;;
  new)
    pytest tests/test_binary_search_duplicates.py
    ;;
  *)
    echo "unknown mode: $MODE (expected base or new)" >&2
    exit 2
    ;;
esac