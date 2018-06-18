FROM python:3
EXPOSE 8000
###############################################################################
# HELP
#
# # build docker image
# docker build -t django-rest .
#
# # run docker image in background
# docker run -d -p 8000:8000 django-rest
#
# # run docker image with attached volume (for development)
# docker run --rm -p 8000:8000 -v $(pwd)/src:/backend django-rest
#
# # run docker image with attached volume (for development) and bash
# docker run --rm -p 8000:8000 -v $(pwd)/src:/backend -it django-rest bash
#
###############################################################################

ENV TERM='xterm-256color'

# update system and install packages
RUN apt-get update # && apt-get upgrade -y
RUN apt-get install -y vim sudo
RUN echo "alias ll='ls -la --color=auto'" >> ~/.bashrc
RUN echo "syntax on" >> ~/.vimrc

# copy code and install python requirements
ADD /src /backend
RUN pip install -r /backend/requirements.txt

WORKDIR /backend

# add user `user` and add sudo access without password
RUN adduser --disabled-password --gecos '' user
RUN adduser user sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER user
RUN echo "alias ll='ls -la --color=auto'" >> ~/.bashrc
RUN echo "syntax on" >> ~/.vimrc

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
