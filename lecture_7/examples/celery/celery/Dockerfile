FROM python:3

ADD . /code

WORKDIR /code
RUN pip install -r requirements.txt

CMD ["celery", "worker", "-A", "app:app", "-l", "info", "-c", "4"]
