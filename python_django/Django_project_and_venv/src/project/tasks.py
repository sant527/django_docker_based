from project import celery_app


@celery_app.task
def warm_temperature_shutdown():
	print("Celery testing")