broker_url = 'redis://redis:6379/0'
celery_imports = ('celery_tasks', )

ceery_result_backend = 'redis'
celery_result_persistent = True
celery_task_result_expires = None

celery_default_queue = 'default'

celery_queues = {
    'default': {
        'binding_key': 'task.#',
    },
    'compute': {
        'binding_key': 'compute.#',
    },
    'result': {
        'binding_key': 'result.#',
    },
}
celery_default_exchange = 'tasks'
celery_default_exchange_type = 'topic'
celery_default_routing_key = 'task.default'

celery_routes = {
    'tasks.compute': {
        'queue': 'compute',
        'routing_key': 'compute.a_result'
    },
    'tasks.handle_result': {
        'queue': 'result',
        'routing_key': 'result.handle',
    },
}
