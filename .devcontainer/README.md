## Getting started
Develop your code in a tailor-made customised dockerised environment. You can either use docker or docker compose to build and run your image. For more information on the list of installed packages, take a look at the Dockerfile and requirements.txt.

## Prerequisites

Docker Installation (Linux-Ubuntu)

1.Update and install dependencies
  ```sh
  sudo apt-get update
  sudo apt-get install ca-certificates curl gnupg lsb-release
  ```

2.Set up the Docker repository
  ```sh
  sudo mkdir -p /etc/apt/keyrings
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
  echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  ```

3.Install the docker engine
  ```sh
  sudo apt update
  sudo apt-get install docker-ce docker-ce-cli containerd.io docker-builx-plugin
  ```

4.Verify the installation
  ```sh
  docker version
  ```

## Setup your environment

1.Run the following with the required input values
  ```sh
  export IMAGE_NAME=<Enter the name of your image>
  export IMAGE_VERSION=<Enter the version of your image>
  export ABSOLUTE_PATH_TO_WORKDIR=<Enter the absolute path to the work directory>
  export WORKDIR=<Enter the workspace name inside the container>
  ```

2.Build the image
  ```sh
  make build
  ```

3.Setup your environment. (Ensure that you are in your working directory)
  ```sh
  make setup-env
  ```

4.Cleanup your workspace after your development activities (Optional)
  ```sh
  make cleanup
  ```



