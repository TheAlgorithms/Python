## Prerequisites

1. **Visual Studio Code (VS Code):** Ensure you have VS Code installed on your machine. You can download it from [here](https://code.visualstudio.com/).

2. **Docker:** Dev Containers rely on Docker, so make sure Docker is installed. Download it from [Docker's official website](https://www.docker.com/).

## Step 1: Install the Remote Development Extension

Open VS Code and install the "Remote Development" extension. This extension pack includes the tools required to develop inside a container. To do this:

   - Open the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window or use the keyboard shortcut `Ctrl+Shift+X`.

   - Search for "Remote Development" and install the extension pack provided by Microsoft.

## Step 2: Create a Dev Container Configuration

1. Open your project folder in VS Code.

2. Create a `.devcontainer` folder in the root of your project.

3. Inside the `.devcontainer` folder, create a `devcontainer.json` file. This file defines the configuration for your dev container.

   ```json
   // .devcontainer/devcontainer.json
   {
     "name": "My Dev Container",
     "image": "your-preferred-docker-image",
     "extensions": ["your-required-vscode-extensions"],
     "settings": {
       "terminal.integrated.shell.linux": "/bin/bash"
     }
   }
   ```

   - Replace `"your-preferred-docker-image"` with the Docker image you want to use for your development environment.
   - Add any additional VS Code extensions you need in the `"extensions"` array.

## Step 3: Open Project in Dev Container

1. Save the `devcontainer.json` file.

2. In the lower-right corner of the window, click on the green square icon (`><`), or use the command palette (`Ctrl+Shift+P`) and select "Remote-Containers: Reopen in Container."

3. VS Code will now rebuild your development environment inside a container. This might take some time, depending on the size of the Docker image.

## Step 4: Develop Inside the Dev Container

Once the container is built and your project is open:

- Use the integrated terminal in VS Code to run commands inside the container.
- All extensions you specified in `devcontainer.json` are available.
- Code, debug, and test your application as you normally would.

## Tips and Tricks

- To rebuild the container, click on the green square icon in the lower-right corner and select "Rebuild Container."
- To stop using the container, click on the green square icon and select "Close Remote Connection."

That's it! You're now set up to use dev containers for your development environment. This approach enhances consistency across different development machines and facilitates collaboration among team members.
--
For more details visit:
https://code.visualstudio.com/docs/devcontainers/tutorial
