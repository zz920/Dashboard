from dashboard.conf.custom_env import getenv

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': getenv('DATABASE_NAME'),
        'USER': getenv('DATABASE_USERNAME'),
        'PASSWORD': getenv('DATABASE_PASSWORD'),
        'HOST': getenv('DATABASE_HOST'),
        'PORT': getenv('DATABASE_PORT'),
    }
}
