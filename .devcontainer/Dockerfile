# https://github.com/microsoft/vscode-dev-containers/blob/main/containers/python-3/README.md
ARG VARIANT=3.12-bookworm
FROM mcr.microsoft.com/vscode/devcontainers/python:${VARIANT}
COPY requirements.txt /tmp/pip-tmp/
RUN python3 -m pip install --upgrade pip \
  && python3 -m pip install --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
  && pipx install pre-commit ruff \
  && pre-commit install
