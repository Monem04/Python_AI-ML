from celery import Celery

celery_app = Celery(
    'practice_api',
    broker="amqp://guest:guest@127.0.0.1:5672/%2f",
    #broker="amqp://guest:guest@localhost:5672//",
    backend=None,
    include=[
        "services.practice_service04"
    ]
)

celery_app.conf.update(
    task_serializer='json',
    result_serializer='json',
    accept_content=['json'],
    timezone="UTC",
    enable_utc=True,
    control_queues_exclusive=True,
    events_queues_exclusive=True,
    worker_enable_remote_control=False,
    task_acks_late=True,
)