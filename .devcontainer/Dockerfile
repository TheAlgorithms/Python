# https://github.com/microsoft/vscode-dev-containers/blob/main/containers/python-3/README.md
ARG VARIANT=3.13-bookworm
FROM mcr.microsoft.com/vscode/devcontainers/python:${VARIANT}
RUN pip install --upgrade pip && pip install uv
COPY pyproject.toml uv.lock ./
RUN uv sync \
  && pipx install pre-commit ruff