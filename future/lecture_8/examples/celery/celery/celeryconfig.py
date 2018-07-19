broker_url = 'redis://redis:6379/0'
celery_imports = ('celery_tasks', )

celery_result_backend = 'redis'
celery_result_persistent = True
celery_task_result_expires = None

imports = ["tasks"]

celery_default_queue = 'default'

task_routes = {
    'tasks.fetch_url': {
        'queue': 'urls',
    },
    'tasks.add': {
        'queue': 'add',
    },
}
