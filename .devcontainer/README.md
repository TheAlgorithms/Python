https://code.visualstudio.com/docs/devcontainers/tutorial
Prerequisites:
- You need Visual Studio Code

Install Docker:
- Docker is needed to create and manage your containers

Docker Desktop:
- Download and install Docker Desktop or an alternative Docker Option, like Docker on a remote host or Docker compliant CLI

Start Docker:

Run the Docker Desktop application to start Docker. You will know it's running if you look in the activity tray and see the Docker whale icon.

Docker might take a few minutes to start. If the whale icon is animated, it is probably still in the process of starting. You can click on the icon to see the status.

Check Docker:
Once Docker is running, you can confirm that everything is working by opening a new terminal window and typing the command:
docker --version
# Docker version 18.09.2, build 6247962

Install the extension:
The Dev Containers extension lets you run Visual Studio Code inside a Docker container.

Check installation
With the Dev Containers extension installed, you will see a new Status bar item at the far left.
The Remote Status bar item can quickly show you in which context VS Code is running (local or remote) and clicking on the item will bring up the Dev Containers commands.

Get the sample
To create a Docker container, we are going to open a GitHub repository with a Node.js project.
Open the Command Palette (F1) to run the command Dev Containers: Try a Dev Container Sample... and select the Node sample from the list.
Note: There are other dev container samples such as vscode-remote-try-python or vscode-remote-try-java, but this tutorial will use vscode-remote-try-node.

Wait for the container to build
The window will then reload, but since the container does not exist yet, VS Code will create one and clone the sample repository into an isolated container volume. This may take some time, and a progress notification will provide status updates. Fortunately, this step isn't necessary the next time you open the folder since the container will already exist.
After the container is built, VS Code automatically connects to it and maps the project folder from your local file system into the container.

Check the container
Once the container is running and you're connected, you should see your remote context change in the bottom left of the Status bar.

Check your environment
One of the useful things about developing in a container is that you can use specific versions of dependencies that your application needs without impacting your local development environment.
The specific container for this tutorial has Node.js v18 installed, which you can check by opening a new terminal Terminal > New Terminal (Ctrl+Shift+`) and entering:

node --version; npm --version
This should show the following versions:
v18.12.1
8.19.2

Run the application
We can now hit F5, which will run the application inside the container. Once the process starts, navigate to http://localhost:3000 and you should see the simple Node.js server running!

Ending your container connection
You can end your session in the container and go back to running VS Code locally with File > Close Remote Connection.

How it works
This next section describes in more detail how the Dev Containers extension sets up and configures your containers.
The Dev Containers extension uses the files in the .devcontainer folder, namely devcontainer.json, and an optional Dockerfile or docker-compose.yml, to create your dev containers.
In the example we just explored, the project has a .devcontainer folder with a devcontainer.json inside. The devcontainer.json uses the image mcr.microsoft.com/devcontainers/javascript-node:0-18. You can explore this image in greater detail in the devcontainers/images repo.
First, your image is built from the supplied Dockerfile or image name, which would be mcr.microsoft.com/devcontainers/javascript-node:0-18 in this example. Then a container is created and started using some of the settings in the devcontainer.json. Finally your Visual Studio Code environment is installed and configured again according to settings in the devcontainer.json. For example, the dev container in this example installs the streetsidesoftware.code-spell-checker extension.
Note: Additional configuration will already be added to the container based on what's in the base image. For example, we see the streetsidesoftware.code-spell-checker extension above, and the container will also include "dbaeumer.vscode-eslint" as that's part of mcr.microsoft.com/devcontainers/typescript-node. This happens automatically when pre-building using devcontainer.json, which you may read more about in the pre-build section.
Once all of this is done, your local copy of Visual Studio Code connects to the Visual Studio Code Server running inside of your new dev container.