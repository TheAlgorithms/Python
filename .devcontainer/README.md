https://code.visualstudio.com/docs/devcontainers/tutorial


# Tutorial: Using Dev Containers with Visual Studio Code

## Introduction

Welcome to the Dev Containers tutorial! In this step-by-step guide, we'll explore running Visual Studio Code within a Docker container using the Dev Containers extension. This tutorial is beginner-friendly, requiring no prior knowledge of Docker.

## Prerequisites

Before we dive in, make sure you have the following:

- [Visual Studio Code](https://code.visualstudio.com/) installed.
- [Docker](https://www.docker.com/) installed, either Docker Desktop or an alternative Docker option.

## Getting Started

### 1. Install Docker

Download and install Docker Desktop or choose an alternative Docker option. Once installed, start Docker. You can confirm it's running by looking for the Docker whale icon in the activity tray.

### 2. Check Docker

Open a new terminal and run the following command to verify Docker installation:

```bash
docker --version
# Example output: Docker version 18.09.2, build 6247962
```

### 3. Install Dev Containers Extension

In Visual Studio Code, install the Dev Containers extension. You'll know it's installed when you see a new Remote Status bar item at the far left.

## Setting up a Sample Node.js Project

### 4. Get the Sample

1. Open the Command Palette (F1).
2. Run `Dev Containers: Try a Dev Container Sample...`.
3. Select the Node sample from the list.

### 5. Wait for Container

After selecting the sample, VS Code will create a Docker container and clone the Node.js project into it. This might take some time, and a progress notification will keep you updated.

### 6. Check Container

Verify the container connection by checking the status in the bottom left of the Status bar. Your remote context should change accordingly.

### 7. Check Environment

Open a new terminal (Ctrl+Shift+`) and enter the following to check Node.js and npm versions:

```bash
node --version; npm --version
# Example output: Node.js version check
```

## Running the Application

### 8. Run Application

1. Press F5 to run the application inside the container.
2. Visit http://localhost:3000 to see the Node.js server in action.

### 9. End Container Connection

To return to running VS Code locally, go to File > Close Remote Connection.

## Understanding Dev Containers Extension

### 10. How it Works

The Dev Containers extension uses `.devcontainer` files, mainly `devcontainer.json`, to configure and set up containers. These files specify the container image, settings, and customizations.

### 11. Architecture

The `devcontainer.json` file includes options like `image`, `dockerfile`, `features`, and more. Let's explore the structure and key options.

### 12. Options Summary

Key options in `devcontainer.json` include `image`, `dockerfile`, `features`, `customizations`, `settings`, `extensions`, `forwardPorts`, `portsAttributes`, `postCreateCommand`, and `remoteUser`. We'll briefly discuss their roles.

## Conclusion

Congratulations! You've successfully completed this tutorial. Feel free to explore more with dev containers, such as opening existing folders or GitHub repositories in containers.

## Troubleshooting

If you encounter any issues:

- **Verify Docker Context:**
  - Check your Docker context, especially if not using a fresh Docker install. Fresh installs usually have a 'default' context.