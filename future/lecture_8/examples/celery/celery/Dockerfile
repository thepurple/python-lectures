FROM python:3.6.6

ADD . /code

WORKDIR /code
RUN pip install -r requirements.txt

# add alias for ls -la
RUN echo "alias ll='ls -la --color=auto'" >> ~/.bashrc

CMD ["celery", "worker", "-A", "tasks:app", "-l", "info", "-c", "2", "-Q", "celery,urls,add"]
