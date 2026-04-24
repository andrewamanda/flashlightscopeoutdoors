# settings.py

# Celery settings
CELERY_BROKER_URL = 'django-db'  # Using the Django database (MySQL) as the broker
CELERY_RESULT_BACKEND = 'django-db'  # Using the Django database for storing task results

# Optional configuration to store periodic task schedules in the database
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers.DatabaseScheduler'

