from conf.custom_env import getenv

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': getenv('DEFAULT_DATABASE_NAME'),
        'USER': getenv('DEFAULT_DATABASE_USERNAME'),
        'PASSWORD': getenv('DEFAULT_DATABASE_PASSWORD'),
        'HOST': getenv('DEFAULT_DATABASE_HOST'),
        'PORT': getenv('DEFAULT_DATABASE_PORT', type=int),
    },
    'souq': {
        'ENGINE': 'djongo',
        'NAME': getenv('SOUQ_DATABASE_NAME'),
        'USER': getenv('SOUQ_DATABASE_USERNAME'),
        'PASSWORD': getenv('SOUQ_DATABASE_PASSWORD'),
        'HOST': getenv('SOUQ_DATABASE_HOST'),
        'PORT': getenv('SOUQ_DATABASE_PORT', type=int),
        'AUTH_SOURCE': getenv('SOUQ_DATABASE_NAME'),
    }
}

DATABASE_ROUTERS = ('dbrouter.CustomDBRouter', )
