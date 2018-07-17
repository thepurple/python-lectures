import requests
from celery import Celery

app = Celery('app', broker='redis://redis:6379/0')


@app.task
def fetch_url(url):
    try:
        resp = requests.get(url)
        print(f"{url} - {resp.status_code}")
    except requests.ConnectionError as e:
        print("{} - Connection Error".format(url))


def func(urls):
    for url in urls:
        fetch_url.delay(url)


if __name__ == "__main__":
    func([
        "http://google.com",
        "https://facebook.com",
        "https://twitter.com",
        "https://some-fake.url"
    ])
