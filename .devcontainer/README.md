**DevContainer Setup Guide**

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Navigate to the DevContainer Folder:**
   ```bash
   cd .devcontainer
   ```

3. **Review the Configuration Files:**
   - Open `Dockerfile` and make sure it has the necessary dependencies and configurations for your project.
   - Inspect `devcontainer.json` to ensure it specifies the required extensions, settings, and Docker settings.

4. **Build the Docker Image:**
   ```bash
   docker build -t <your-image-name> .
   ```

5. **Open VS Code in the DevContainer:**
   - Launch VS Code, ensuring you have the "Remote - Containers" extension installed.
   - Open the cloned repository in VS Code.
   - You should be prompted at the bottom-right to "Reopen in Container." Click on it.

6. **Wait for the Container to Build:**
   - VS Code will now build the container based on the configurations you've provided. This may take a few minutes.

7. **Verify Container Connection:**
   - Once the container is built, check the bottom-left corner of VS Code. It should indicate that you are now inside the container.

8. **Open an Algorithm and Run It:**
   - Navigate to the algorithm file you want to run.
   - Write or modify the code as needed.
   - Run the code as you normally would.

Remember to tailor the Dockerfile and devcontainer.json to the specific requirements of your project. If issues persist, carefully check error messages during the build process, as they often provide insights into what might be going wrong.


For more details visit:
https://code.visualstudio.com/docs/devcontainers/tutorial
