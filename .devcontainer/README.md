# Setting Up DevContainer

This repository includes a DevContainer configuration that allows you to set up a development environment. Follow these steps to get started:

**Prerequisites**

Before you begin, ensure that you have the following prerequisites installed on your system:

- Visual Studio Code(https://code.visualstudio.com/)
- Docker(https://www.docker.com/)

**Clone the Repository**
Clone this repository to your local machine using Git:
```bash
git clone <repository-url>
```

**Open the cloned repository in Visual Studio Code:**
```bash
cd <repository-directory>
code .
```

**Install the "Remote - Containers" Extension**

In Visual Studio Code, install the "Remote - Containers" extension if you haven't already. This extension enables you to develop inside a DevContainer:

step -1: Click on the Extensions icon in the left sidebar.

step -2: Search for "Remote - Containers" and install it.

**Reopen in DevContainer**
After installing the "Remote - Containers" extension, you should see a green icon in the bottom-left corner of Visual Studio Code. Click on it, and then select "Reopen in Container." This will use the configuration in .devcontainer/devcontainer.json to build and start your DevContainer.

For any referneces follow the link below :-

https://code.visualstudio.com/docs/devcontainers/tutorial
