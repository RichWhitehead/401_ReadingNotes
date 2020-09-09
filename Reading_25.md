# Reading 31

## What is Docker?
Docker is an open source project that makes it easy to create containers and container-based apps. Originally built for Linux, Docker now runs on Windows and MacOS as well. To understand how Docker works, let’s take a look at some of the components you would use to create Docker-containerized applications.

Dockerfile
Each Docker container starts with a Dockerfile. A Dockerfile is a text file written in an easy-to-understand syntax that includes the instructions to build a Docker image. A Dockerfile specifies the operating system that will underlie the container, along with the languages, environmental variables, file locations, network ports, and other components it needs—and, of course, what the container will actually be doing once we run it.

## Docker image

Once you have your Dockerfile written, you invoke the Docker build utility to create an image based on that Dockerfile. Whereas the Dockerfile is the set of instructions that tells build how to make the image, a Docker image is a portable file containing the specifications for which software components the container will run and how. Because a Dockerfile will probably include instructions about grabbing some software packages from online repositories, you should take care to explicitly specify the proper versions, or else your Dockerfile might produce inconsistent images depending on when it’s invoked. But once an image is created, it’s static.

## What are containers?

One of the goals of modern software development is to keep applications on the same host or cluster isolated from one another so they don’t unduly interfere with each other’s operation or maintenance. This can be difficult, thanks to the packages, libraries, and other software components required for them to run. One solution to this problem has been virtual machines, which keep applications on the same hardware entirely separate, and reduce conflicts among software components and competition for hardware resources to a minimum. But virtual machines are bulky—each requires its own OS, so is typically gigabytes in size—and difficult to maintain and upgrade.

