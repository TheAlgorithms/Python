# Development Container

This is **Devcontainer** configuration to provide a consistent development environment for all contributors.

## Features

- [x] Pre-configured **Python environment**
- [x] Automatic installation of **pre-commit hooks**
- [x] **Ruff** linter ready to check your code
- [x] **Oh My Zsh** with plugins:
- `zsh-autosuggestions`
- `zsh-syntax-highlighting`

## Usage

1. Install [**Docker** ](https://www.docker.com/get-started/) and [**Visual Studio Code**](https://code.visualstudio.com/)
2. Install the **Remote - Containers** extension in VS Code

    - Do `CTRL+P`, paste this command and press `Enter`

        ```shell
        ext install ms-vscode-remote.remote-containers
        ```
3. Open this repository in VS Code
4. When prompted, click **"Reopen in Container"**
5. Wait for the environment to build and initialize

After setup:

- `pre-commit` hooks are installed
- `ruff` and other tools are available
- The shell uses Zsh by default

## Tips

To manually run checks on all files:

```bash
pre-commit run --all-files
```

> For further information here's [Microsoft tutorial about devcontainers.](https://code.visualstudio.com/docs/devcontainers/tutorial)
