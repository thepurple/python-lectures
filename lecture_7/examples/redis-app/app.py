import time

import redis
from flask import Flask


app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


def redis_tries(fn):
    def wrapper():
        retries = 5
        while True:
            try:
                return fn()
            except redis.exceptions.ConnectionError as exc:
                if retries == 0:
                    raise exc
                retries -= 1
                time.sleep(0.5)

    return wrapper


@redis_tries
def get_hit_count():
    return cache.incr('hits')


# def get_hit_count():
#     retries = 5
#     while True:
#         try:
#             return cache.incr('hits')
#         except redis.exceptions.ConnectionError as exc:
#             if retries == 0:
#                 raise exc
#             retries -= 1
#             time.sleep(0.5)


@redis_tries
def reset_hit_count():
    cache.set('hits', 0)
    return 0


@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)


@app.route('/reset')
def reset():
    count = reset_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
