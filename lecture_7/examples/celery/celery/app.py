import requests
from celery import Celery

app = Celery('app', broker='redis://redis:6379/0')


@app.task
def fetch_url(url):
    resp = requests.get(url)
    print(resp.status_code)
    # TODO place result into redis


def func(urls):
    for url in urls:
        fetch_url.delay(url)


if __name__ == "__main__":
    func([
        "http://google.com",
        "https://facebook.com",
        "https://twitter.com",
        "https://alexa.com"
    ])

# import time
#
# from celery.task import task
#
#
# @task
# def add(x, y):
#     return x + y
#
#
# @task(ignore_result=True)
# def compute(x, y):
#     """
#     Perform a computation, calling another task to handle the results.
#     """
#     time.sleep(5)
#     return handle_result.delay(x * y).task_id
#
#
# @task(ignore_result=True)
# def handle_result(result):
#     """
#     Handle the result of compute.
#
#     :param result:
#     :return:
#     """
#     print(result)
#
# if __name__ == "__main__":
#     pass
