FROM python:3
EXPOSE 8000

ENV TERM='xterm-256color'

# install OS packages
RUN apt-get update && apt-get install -y vim sqlite3 tree sudo

# add user `user` and add sudo access without password
RUN adduser --disabled-password --gecos '' user
RUN adduser user sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER user

# add alias for ls -la
RUN echo "alias ll='ls -la --color=auto'" >> ~/.bashrc

# install pip requirements
ADD /src /src
RUN sudo pip install -r /src/requirements.txt

# change workdir
WORKDIR /src

CMD ["python", "/src/mysite/manage.py", "runserver", "0.0.0.0:8000"]
