# Step by Step instructions for new user to use DevContainer

## Step 1: Install Visual Studio Code

Download and install **Visual Studio Code** from the [official website](https://code.visualstudio.com/).

## Step 2: Install Docker

Ensure **Docker** is installed on your machine. You can download it from the [official Docker website](https://docs.docker.com/get-docker/).

## Step 3: Open a Project in Visual Studio Code

Open the project you want to work on in **Visual Studio Code**.

## Step 4: Install the Remote Development Extension Pack

Install the **Remote Development** extension pack in **Visual Studio Code**. This pack includes extensions that enable you to work with development environments in containers, WSL, or SSH. You can find the extension pack [here](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack).

## Step 5: Open the Command Palette

Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS) to open the **Command Palette**.

## Step 6: Choose a DevContainer Configuration

Type and select **"Remote-Containers: Add Development Container Configuration Files"** from the **Command Palette**. Choose a predefined configuration (e.g., Node.js, Python, etc.) or select **"Other"** to create a custom configuration.

## Step 7: Customize the DevContainer Configuration (Optional)

If you selected **"Other,"** customize the `devcontainer.json` file according to your project's needs, specifying the required tools, extensions, and settings for the DevContainer.

## Step 8: Reopen the Project in a DevContainer

Open the **Command Palette** again and select **"Remote-Containers: Reopen in Container."** Visual Studio Code will build the Docker image, set up the DevContainer, and reopen your project within the container.

## Step 9: Work in the DevContainer

You are now working within the **DevContainer.** Make your changes, write code, and use the integrated tools and extensions.

## Step 10: Save and Commit Your Work

Save your changes within the **DevContainer.** All changes are saved to your local workspace and are persistent across container restarts.

## Step 11: Stop or Restart the DevContainer

To stop the **DevContainer,** click on the bottom-left corner where it says **"DevContainer"** and choose **"Stop Container."** To restart, use **"Reopen in Container"** again.
