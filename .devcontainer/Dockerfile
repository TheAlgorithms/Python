# https://github.com/devcontainers/images/tree/main/src/python
# Debian 13 "Trixie" base. Python 3.14 is the current latest-stable CPython;
# the trixie image tags are versioned (there is no floating `3-trixie` alias yet),
# so we pin the newest available: 3.14-trixie.
ARG VARIANT=3.14-trixie
FROM mcr.microsoft.com/devcontainers/python:${VARIANT}
COPY requirements.txt /tmp/pip-tmp/
RUN python3 -m pip install --upgrade pip \
  && python3 -m pip install --no-cache-dir -r /tmp/pip-tmp/requirements.txt \
  && pipx install pre-commit ruff uv
