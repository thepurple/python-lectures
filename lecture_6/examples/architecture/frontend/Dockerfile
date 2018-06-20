FROM node:latest

ENV DEBIAN_FRONTEND noninteractive

# update system and install packages
RUN apt-get update && apt-get install -y bash sudo vim
RUN echo "alias ll='ls -la --color=auto'" >> ~/.bashrc
RUN echo "syntax on" >> ~/.vimrc

