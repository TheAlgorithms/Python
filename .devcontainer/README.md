**Step-by-step instructions to start up DevContainer**

**Step 1: Install Visual Studio Code**
- If you haven't already, download and install Visual Studio Code from the [official website](https://code.visualstudio.com).


**Step 2: Install Docker**
1. **Docker Desktop:** Docker is needed to create and manage your containers. Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop), or an [alternative Docker option](https://code.visualstudio.com/remote/advancedcontainers/docker-options), like Docker on a remote host or Docker compliant CLI.


2. **Start Docker:** Run the Docker Desktop application to start Docker. You will know it's running if you look in the activity tray and see the Docker whale icon. Docker might take a few minutes to start. If the whale icon is animated, it is probably still in the process of starting. You can click on the icon to see the status.
3. **Check Docker**: Once Docker is running, you can confirm that everything is working by opening a new terminal window and typing the command: `docker --version`



**Step 3: Install the Dev Containers extension**
1. Open Visual Studio Code, and from the Extensions view (Ctrl+Shift+X), search for and install the "Dev Containers" extension pack.


2. **Check installation:** With the Dev Containers extension installed, you will see a new Status bar item at the far left. The Remote Status bar item can quickly show you in which context VS Code is running (local or remote) and clicking on the item will bring up the Dev Containers commands.
3. **Get the sample:** To create a Docker container, we are going to open a GitHub repository with a Node.js project. Open the Command Palette (F1) to run the command Dev Containers: Try a Dev Container Sample...and select the Node sample `vscode-remote-try-node` from the list.
4. **Wait for the container to build:** The window will then reload, but since the container does not exist yet, VS Code will create one and clone the sample repository into an isolated container volume. This may take some time, and a progress notification will provide status updates. Fortunately, this step isn't necessary the next time you open the folder since the container will already exist. After the container is built, VS Code automatically connects to it and maps the project folder from your local file system into the container.
5. **Check the container:** Once the container is running and you're connected, you should see your remote context change in the bottom left of the Status bar


**Step 4: Check your environment**

One of the useful things about developing in a container is that you can use specific versions of dependencies that your application needs without impacting your local development environment.
The specific container for this tutorial has Node.js v18 installed, which you can check by opening a new terminal **Terminal** > **New Terminal** (⌃⇧`) and entering:

`node --version; npm --version`


1. **Run the application:**
We can now hit `F5`, which will run the application inside the container. Once the process starts, navigate to http://localhost:3000 and you should see the simple Node.js server running!
2. **Ending your container connection:**
You can end your session in the container and go back to running VS Code locally with File > Close Remote Connection.

To learn how the Dev Container extension works, click [here](https://code.visualstudio.com/docs/devcontainers/tutorial#_how-it-works).

You can also find the tutorial [here](https://code.visualstudio.com/docs/devcontainers/tutorial
).
