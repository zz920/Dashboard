from conf.custom_env import getenv

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': getenv('DEFAULT_DATABASE_NAME'),
        'USER': getenv('DEFAULT_DATABASE_USERNAME'),
        'PASSWORD': getenv('DEFAULT_DATABASE_PASSWORD'),
        'HOST': getenv('DEFAULT_DATABASE_HOST'),
        'PORT': getenv('DEFAULT_DATABASE_PORT', type=int),
    },
    'psql_souq_uae': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': getenv('PSQL_SOUQ_UAE_DATABASE_NAME'),
        'USER': getenv('PSQL_SOUQ_UAE_DATABASE_USERNAME'),
        'PASSWORD': getenv('PSQL_SOUQ_UAE_DATABASE_PASSWORD'),
        'HOST': getenv('PSQL_SOUQ_UAE_DATABASE_HOST'),
        'PORT': getenv('PSQL_SOUQ_UAE_DATABASE_PORT', type=int),
    },
    'psql_souq_ksa': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': getenv('PSQL_SOUQ_KSA_DATABASE_NAME'),
        'USER': getenv('PSQL_SOUQ_KSA_DATABASE_USERNAME'),
        'PASSWORD': getenv('PSQL_SOUQ_KSA_DATABASE_PASSWORD'),
        'HOST': getenv('PSQL_SOUQ_KSA_DATABASE_HOST'),
        'PORT': getenv('PSQL_SOUQ_KSA_DATABASE_PORT', type=int),
    },
    # remote
    'mongo_souq_uae': {
        'ENGINE': 'djongo',
        'NAME': getenv('MONGO_SOUQ_UAE_DATABASE_NAME'),
        'USER': getenv('MONGO_SOUQ_UAE_DATABASE_USERNAME'),
        'PASSWORD': getenv('MONGO_SOUQ_UAE_DATABASE_PASSWORD'),
        'HOST': getenv('MONGO_SOUQ_UAE_DATABASE_HOST'),
        'PORT': getenv('MONGO_SOUQ_UAE_DATABASE_PORT', type=int),
        'AUTH_SOURCE': getenv('MONGO_SOUQ_UAE_DATABASE_NAME'),
        'ENFORCE_SCHEMA': False,
    },
    # remote
    'mongo_souq_ksa': {
        'ENGINE': 'djongo',
        'NAME': getenv('MONGO_SOUQ_KSA_DATABASE_NAME'),
        'USER': getenv('MONGO_SOUQ_KSA_DATABASE_USERNAME'),
        'PASSWORD': getenv('MONGO_SOUQ_KSA_DATABASE_PASSWORD'),
        'HOST': getenv('MONGO_SOUQ_KSA_DATABASE_HOST'),
        'PORT': getenv('MONGO_SOUQ_KSA_DATABASE_PORT', type=int),
        'AUTH_SOURCE': getenv('MONGO_SOUQ_KSA_DATABASE_NAME'),
        'ENFORCE_SCHEMA': False,
    },
}

DATABASE_ROUTERS = ('dbrouter.CustomDBRouter', )
