# How To use the DevConatiners.

In this section we are going learn how to run Visual Studio Code in a Docker container using the Dev Containers extension.
Running VS Code inside a Docker container can be useful for many reasons, but in this walkthrough we'll focus on using a Docker container to set up a development environment that is separate from your local environment.

## Table of Contents
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Getting Sample](#GETTING-SAMPLE)
- [Development Environment](#development-environment)
- [License](#license)

## Getting Started

### Prerequisites

1. **INSTALL VS CODE** : You need [Visual Studio Code](https://code.visualstudio.com/) installed.
2. **INSTALL DOCKER**
   1. [Docker](https://www.docker.com/products/docker-desktop/) is needed to create and manage your containers.
   2. Download and install Docker Desktop, or an alternative Docker option, like Docker on a remote host or Docker compliant        CLI
   3. Run the Docker Desktop application to start Docker. You will know it's running if you look in the activity tray and          see the Docker whale icon.

      ![docker-status](https://github.com/Manavbangotra/Python/assets/87271558/792766c3-2d68-461d-8e22-cfa7e22c0d23)
   
   4. Once Docker is running, you can confirm that everything is working by opening a new terminal window and typing the           command
     > docker --version

### Installation of DevConatiners Extension

Go onto the Extenion section in VS Code and Search for Dev Containers extension and Click on INTSALL!
![dev-containers-extension](https://github.com/Manavbangotra/Python/assets/87271558/cf3fd5e6-c5a2-4b11-91a7-20bb033b8db2)

**Check installation**
With the Dev Containers extension installed, you will see a new Status bar item at the far left.
![remote-status-bar](https://github.com/Manavbangotra/Python/assets/87271558/31947513-1749-45b3-9b53-df004025234d)

The Remote Status bar item can quickly show you in which context VS Code is running (local or remote) and clicking on the item will bring up the Dev Containers commands.
<img width="606" alt="dev-containers-commands-simple" src="https://github.com/Manavbangotra/Python/assets/87271558/d97ecec1-0dfa-4f4c-bd94-d020f5013351">

### GETTING-SAMPLE
To create a Docker container, we are going to open a GitHub repository with a Node.js project.
Open the Command Palette (F1) to run the command Dev Containers: Try a Dev Container Sample... and select the Node sample from the list.
![select-a-sample](https://github.com/Manavbangotra/Python/assets/87271558/86431325-7005-4e0f-b1f8-f2f37979b8fd)
Note: There are other dev container samples such as vscode-remote-try-python or vscode-remote-try-java, but this tutorial will use vscode-remote-try-node.

**Wait for the container to build**
The window will then reload, but since the container does not exist yet, VS Code will create one and clone the sample repository into an isolated container volume. This may take some time, and a progress notification will provide status updates. Fortunately, this step isn't necessary the next time you open the folder since the container will already exist.

![dev-container-progress](https://github.com/Manavbangotra/Python/assets/87271558/d465e2dc-a3f1-43cc-9301-93fb1cf6525c)

After the container is built, VS Code automatically connects to it and maps the project folder from your local file system into the container.

**Check the container**
Once the container is running and you're connected, you should see your remote context change in the bottom left of the Status bar.

![connected](https://github.com/Manavbangotra/Python/assets/87271558/acc3275c-e8d1-46d2-bc4e-8b6b978fe99d)

## Development Environment

One of the useful things about developing in a container is that you can use specific versions of dependencies that your application needs without impacting your local development environment.

The specific container for this tutorial has Node.js v18 installed, which you can check by opening a new terminal Terminal > New Terminal (Ctrl+Shift+`) and entering:

> node --version; npm --version

This should show the following versions.

![version-check-updated](https://github.com/Manavbangotra/Python/assets/87271558/769ea7ea-7416-43c9-83fc-2c4c29ef1ef7)

**Run the application**
We can now hit F5, which will run the application inside the container. Once the process starts, navigate to http://localhost:3000 and you should see the simple Node.js server running!

![hello-remote-world](https://github.com/Manavbangotra/Python/assets/87271558/9c0e4e07-207e-48e8-878d-b5d59bcbcbd3)

**Ending your container connection**
You can end your session in the container and go back to running VS Code locally with File > Close Remote Connection.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.



