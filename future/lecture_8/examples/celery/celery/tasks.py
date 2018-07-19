import requests
from celery import Celery
from time import sleep

app = Celery("tasks")
app.config_from_object("celeryconfig")


@app.task(name="tasks.fetch_url")
def fetch_url(url):
    sleep(10)
    try:
        resp = requests.get(url)
        print(f"{url} - {resp.status_code}")
    except requests.ConnectionError as e:
        print("{} - Connection Error".format(url))


@app.task
def add(x, y):
    sleep(5)
    return x + y


def func(urls):
    for url in urls:
        fetch_url.apply_async((url,))


if __name__ == "__main__":
    func([
        "http://google.com",
        "https://facebook.com",
        "https://twitter.com",
        "https://some-fake.url"
    ])
    add.delay(2, 2)
