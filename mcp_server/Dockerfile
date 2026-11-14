FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

ENV UV_PYTHON_INSTALL_DIR=/opt/python \
    UV_CACHE_DIR=/tmp/uv-cache \
    HOME=/tmp \
    PYTHONDONTWRITEBYTECODE=1

# Server deps on the image's 3.13; the repo's 3.15t is only for running doctests.
# Pinned below 2: mcp 2.x renamed FastMCP to MCPServer; the course material uses v1.
RUN uv pip install --system "mcp[cli]<2" ruff \
 && uv python install 3.15t \
 && ln -s "$(uv python find 3.15t)" /usr/local/bin/python3.15t

# uv is build-time only: at runtime the server calls python3.15t directly, so the
# non-root user never needs uv's (root-owned) cache.

# pre-commit hook environments are baked in: the container runs with --network none.
ENV PRE_COMMIT_HOME=/opt/pre-commit

RUN apt-get update \
 && apt-get install -y --no-install-recommends git \
 && rm -rf /var/lib/apt/lists/* \
 && uv pip install --system pre-commit \
 && git config --system --add safe.directory '*'

# "repo" is a named build context (the repository root); only this file is read.
# Rebuild the image whenever .pre-commit-config.yaml changes its rev pins.
COPY --from=repo .pre-commit-config.yaml /tmp/pc/.pre-commit-config.yaml
RUN cd /tmp/pc && git init -q . \
 && pre-commit install-hooks \
 && cd / && rm -rf /tmp/pc \
 && chmod -R a+rwX "$PRE_COMMIT_HOME"

COPY precommit_check.sh /usr/local/bin/precommit-check
COPY algo_server.py /srv/algo_server.py
WORKDIR /repo
ENTRYPOINT ["python", "/srv/algo_server.py"]
