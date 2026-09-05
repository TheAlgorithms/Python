#!/bin/bash
#
# Close every open pull request labelled "require type hints".
# Thin wrapper around close_pull_requests_with_label.sh so all five backlog
# jobs share one implementation. Set DRY_RUN=1 to preview.
set -euo pipefail
exec "$(dirname "$0")/close_pull_requests_with_label.sh" "require type hints" "$@"
