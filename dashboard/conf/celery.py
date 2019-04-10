from conf.custom_env import getenv


### CELERY ###
BROKER_URL = getenv('REDIS_URL')
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'                                                                    
CELERY_ENABLE_UTC = True   

BROKER_POOL_LIMIT = 3

CELERY_RESULT_BACKEND = 'django-db'
