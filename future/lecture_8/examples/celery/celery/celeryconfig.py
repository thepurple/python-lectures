broker_url = 'redis://redis:6379/0'

result_persistent = True
result_expires = None

imports = ['tasks']

task_default_queue = 'celery'

task_routes = {
    'tasks.fetch_url': {
        'queue': 'urls',
    },
    'tasks.add': {
        'queue': 'add',
    },
}
