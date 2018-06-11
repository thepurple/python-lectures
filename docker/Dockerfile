FROM python:3.6.4

ENV TERM='xterm-256color'

RUN apt-get update && apt-get upgrade -y && apt-get install -y vim
ADD /src /src

WORKDIR /src

CMD ["python", "test.py"]
