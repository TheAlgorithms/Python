#!/usr/bin/env bash
set -uo pipefail
cd /app

OUTPUT_PATH=""
MODE=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --output_path)
      OUTPUT_PATH="$2"
      shift 2
      ;;
    base|new)
      MODE="$1"
      shift
      ;;
    *)
      echo "unknown argument: $1" >&2
      exit 2
      ;;
  esac
done

if [[ -z "$MODE" ]]; then
  echo "mode argument required (base or new)" >&2
  exit 2
fi

case "$MODE" in
  base)
    pytest tests --ignore=tests/test_binary_search_leftmost.py --junitxml="$OUTPUT_PATH"
    ;;
  new)
    pytest tests/test_binary_search_leftmost.py --junitxml="$OUTPUT_PATH"
    ;;
esac
