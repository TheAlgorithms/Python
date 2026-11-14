#!/bin/bash
# Start the AlgoDev MCP server in Docker (local only) and confirm it answers.
#
#   mcp_server/check_server.sh    # (re)build the image, then check
#
# Speaks the same newline-delimited JSON-RPC that Claude Code would over stdio:
#   1. initialize       -> the handshake succeeds
#   2. tools/list       -> run_doctests and ruff_check are registered
#   3. tools/call       -> run_doctests on a known-good file reports exit=0

set -euo pipefail

IMAGE="algodev-mcp"
SAMPLE="sorts/bubble_sort.py"
REPLY_TIMEOUT=90

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(dirname "$HERE")"

# Always build: Docker's layer cache makes this near-instant when nothing changed,
# and it guarantees the check never runs against a stale image.
echo "building $IMAGE ..."
# The Dockerfile reads .pre-commit-config.yaml from the repo root via the named
# build context "repo".
docker build --quiet --build-context repo="$REPO" -t "$IMAGE" "$HERE" >/dev/null

# Same flags as .mcp.json, so this exercises what Claude Code will launch.
coproc SERVER {
    docker run -i --rm --network none --user "$(id -u):$(id -g)" \
        -v "$REPO:/repo:ro" "$IMAGE"
}
to_server=${SERVER[1]}
from_server=${SERVER[0]}
server_pid=$SERVER_PID

cleanup() {
    exec {to_server}>&- 2>/dev/null || true # EOF on stdin makes the server exit
    wait "$server_pid" 2>/dev/null || true
}
trap cleanup EXIT

send() {
    printf '%s\n' "$1" >&"$to_server"
}

# Read lines until the response carrying this request id arrives.
reply_for() {
    local id=$1 line
    while read -r -t "$REPLY_TIMEOUT" line <&"$from_server"; do
        if [[ "$line" =~ \"id\":$id[,}] ]]; then
            printf '%s\n' "$line"
            return 0
        fi
    done
    echo "FAIL: server exited or sent no reply to request $id (timeout ${REPLY_TIMEOUT}s)" >&2
    return 1
}

fail() {
    echo "FAIL: $1" >&2
    echo "  got: $2" >&2
    exit 1
}

send '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"check_server","version":"0"}}}'
reply=$(reply_for 1)
[[ "$reply" == *'"serverInfo"'* ]] || fail "initialize handshake" "$reply"
echo "ok  initialize"

send '{"jsonrpc":"2.0","method":"notifications/initialized"}'

send '{"jsonrpc":"2.0","id":2,"method":"tools/list"}'
reply=$(reply_for 2)
for tool in run_doctests ruff_check; do
    [[ "$reply" == *"\"name\":\"$tool\""* ]] || fail "tool $tool not listed" "$reply"
done
echo "ok  tools/list (run_doctests, ruff_check)"

send "{\"jsonrpc\":\"2.0\",\"id\":3,\"method\":\"tools/call\",\"params\":{\"name\":\"run_doctests\",\"arguments\":{\"path\":\"$SAMPLE\"}}}"
reply=$(reply_for 3)
[[ "$reply" == *'exit=0'* ]] || fail "run_doctests on $SAMPLE" "$reply"
echo "ok  tools/call run_doctests $SAMPLE"

echo "OK: $IMAGE is up and answering"
