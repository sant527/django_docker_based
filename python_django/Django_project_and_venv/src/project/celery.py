import os
from celery import Celery
import django

import sys

print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHAAAAAAAAAAAAAAARRRRRRRRRRRRRRRREEEEEEEEEEEEEEEEEEEEEE")

# when we run 
#celery -A basic_django worker --loglevel=debug
# it will run this file.


#get current folder name:
dirname = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
settings_str = (dirname) +".settings"
print(settings_str)

#we have to set the DJANGO_SETTINGS_MODULE so that the when we run 
# celery -A basic_django worker --loglevel=debug, it will look for the env varaible
# and it will activate the django and then get all the tasks. in all the installed apps.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_str)
print(os.environ.get('DJANGO_SETTINGS_MODULE'))

# This we will need for using the logging config defined in settings.py
# We can use custom logging we created for django here also.
from django.conf import settings
from django.utils.log import configure_logging
configure_logging(settings.LOGGING_CONFIG, settings.LOGGING)


#This defines the celery app instance
redis = 'redis://:gauranga@redis:6379/0'
app = Celery(dirname, 
	broker=redis, 
	backend=redis
	)

# list all the repeated tasks
app.conf.beat_schedule = {
	#"warm_weather_shutdown_every_5_minutes": {
	#"task": "boiler.tasks.warm_temperature_shutdown",
	#"schedule": 300.0
	#}
}

app.autodiscover_tasks()

# also ad



#Celery instance is assign to app variable by convention. Keep your project
#simple and #consistent. Celery instance should be named same as project. For
#example if project’s name is "gift-catalogue” then app =
#Celery('gift-catalogue', broker=redis, backend=redis)