FROM python:3
EXPOSE 5000
###############################################################################
# HELP
#
# # build docker image
# docker build -t flask-test .
#
# # run docker image in background
# docker run -d -p 5000:5000 flask-test
#
# # run docker image with attached volume (for development)
# docker run --rm -p 5000:5000 -v $(pwd)/src:/backend flask-test
#
# # run docker image with attached volume (for development) and bash
# docker run --rm -p 5000:5000 -v $(pwd)/src:/backend -it flask-test bash
#
###############################################################################

ENV TERM='xterm-256color'

# update system and install packages
RUN apt-get update # && apt-get upgrade -y
RUN apt-get install -y sudo vim sqlite
RUN echo "alias ll='ls -la --color=auto'" >> ~/.bashrc
RUN echo "syntax on" >> ~/.vimrc

# copy code and install python requirements
ADD /src /backend
RUN pip install -r /backend/requirements.txt

# add user `user` and add sudo access without password
RUN adduser --disabled-password --gecos '' user
RUN adduser user sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# user settings
USER user
RUN echo "alias ll='ls -la --color=auto'" >> ~/.bashrc

WORKDIR /backend

CMD ["python", "app.py"]
