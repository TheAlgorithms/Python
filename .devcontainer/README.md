**DevContainer Setup Guide**

**Prerequisites:**
- Ensure you have Docker installed: [Docker](https://www.docker.com/get-started)
- Install Visual Studio Code: [Visual Studio Code](https://code.visualstudio.com/download)
- Add Remote - Containers extension for VSCode: [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

**Getting Started:**

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your/repository.git
   cd repository
   ```

2. **Navigate to the DevContainer Directory:**
   ```bash
   cd .devcontainer
   ```

3. **Open in Visual Studio Code:**
   ```bash
   code .
   ```

4. **Reopen in DevContainer:**
   - Press `F1` to open the command palette.
   - Type `Remote-Containers: Reopen in Container` and select it.

5. **Wait for Container to Build:**
   The initial launch takes time as the container is built. Subsequent launches are faster.

6. **Verify DevContainer:**
   Open a terminal in VSCode. The prompt should now display the container name.
   ```bash
   your-username@container-name:~$
   ```

7. **Start Your Development:**
   Begin coding within the DevContainer environment with pre-configured tools and dependencies.

**Stopping and Restarting:**
- To stop, close VSCode.
- To restart, repeat steps 3 and 4.

**Customization:**
- Modify the DevContainer configuration in `devcontainer.json` if necessary.

You're ready to code! For any issues, consult our documentation or contact support.
For more details visit:
https://code.visualstudio.com/docs/devcontainers/tutorial
