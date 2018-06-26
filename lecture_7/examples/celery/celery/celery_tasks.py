import time
from celery import Celery
from celery.task import task

app = Celery('app')
app.config_from_object("celeryconfig")


@task
def add(x, y):
    return x + y


@task(ignore_result=True)
def compute(x, y):
    """
    Perform a computation, calling another task to handle the results.
    """
    time.sleep(5)
    return handle_result.delay(x * y).task_id


@task(ignore_result=True)
def handle_result(result):
    """
    Handle the result of compute.

    :param result:
    :return:
    """
    print(result)


if __name__ == "__main__":
    pass
