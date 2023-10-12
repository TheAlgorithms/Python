        Using Visual Studio Code in a Docker Container

This guide will show you how to run Visual Studio Code inside a Docker container with the help of the Dev Containers extension. Don't worry if you're new to Docker; you don't need any prior knowledge for this.

Why Use Docker with VS Code?
Running VS Code in a Docker container has many benefits. In this tutorial, we'll focus on creating a separate development environment that won't interfere with your local setup.

Prerequisites:
Before you begin, make sure you have Visual Studio Code installed on your machine.

Install Docker:
To work with containers, you'll need Docker. You can either use Docker Desktop or another Docker option, such as Docker on a remote host or a Docker-compliant command-line interface (CLI).

Docker Desktop: Download and install Docker Desktop. You'll know it's running when you see the Docker whale icon in your system tray. It might take a few minutes to start, so be patient.
Check Docker: Once Docker is running, open a new terminal window and type the following command to check if Docker is installed:

------------------CODE------------------
docker --version
# Example output: Docker version 18.09.2, build 6247962
----------------------------------------

Install the Dev Containers Extension:
The Dev Containers extension allows you to run VS Code inside a Docker container. After installation, you'll see a new item in the Status bar on the far left.

Getting the Sample Project:
To create a Docker container, we'll use a sample Node.js project from a GitHub repository. Here's how to do it:

1- Open the Command Palette (F1).
2- Run the command "Dev Containers: Try a Dev Container Sample..."
3- Choose the "Node" sample from the list.
OBS.: Please note that there are other samples available, but this tutorial focuses on "vscode-remote-try-node."

Building the Container:
After selecting the sample, your VS Code window will reload. Since the container doesn't exist yet, VS Code will create one and clone the sample repository into it. This might take some time, and you'll see a progress notification. However, this step won't be necessary the next time you open the folder because the container will already exist.

Checking the Container:
Once the container is running and connected, you'll notice a change in your VS Code's status bar at the bottom left.

Verifying Your Environment:
Developing in a container allows you to use specific versions of dependencies without affecting your local environment. This tutorial's container has Node.js version 18 installed. You can check it by opening a new terminal (Terminal > New Terminal) and entering:

------------------CODE------------------
node --version; npm --version
# Example output: v18.12.1
#                   8.19.2
----------------------------------------

Running the Application:
Now, you can press F5 to run the application inside the container. Once the process starts, open a web browser and navigate to http://localhost:3000 to see the Node.js server in action.

Ending the Container Connection:
When you're done, you can disconnect from the container and return to using VS Code locally by going to "File" > "Close Remote Connection."

How It Works:
Congratulations! You've completed this tutorial. It's just the beginning of what you can do with dev containers. Next, you can explore opening an existing folder in a container or working with GitHub repositories or pull requests in a container. For more remote development options, check out the other Remote Development extensions like "Remote - SSH" and "WSL," or install the "Remote Development Extension Pack."

Troubleshooting Tip:
If you encounter issues with the context when using the "Dev Containers: Try a Dev Container Sample..." command, check your Docker context. Fresh Docker installations have a 'default' context, and you can switch back to it using the following commands:

------------------CODE------------------
# List available contexts and mark the default context with '*'
docker context list
# Switch to the 'default' context
docker context use default
----------------------------------------
