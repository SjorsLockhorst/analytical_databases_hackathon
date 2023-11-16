# Dev environment instructions

## Prerequisit
In order to use the provided dev containter, ensure that you have installed the official "devcontainer" extention for VSCode. You can find it by searching for "dev containers" in the extension marketplace in VSCode. It's the one by Microsoft. 

Next, make sure that you have installed docker and have it running on your machine. You can find instructions for your operating system [on the official site](https://docs.docker.com/engine/install/).

## Setting up the .devcontainer
Now that you have Docker running and the devcontainers plugin installted, create an `.env` file in the `.devcontainer` folder. Use the `.env_example` as an example for what the file should contain. 

After this, restart VSCode. You should get a pop-up asking you if you would like to start the dev container. Click yes and wait for the environment to load. All dependencies should be automatically installed and VSCode should have selected the correct interperter.

Happy coding!
