import os
import sys
from django.conf import settings

# ******************** COMMON ********************

APP_ID = os.environ['APP_ID']

APP_NAME = os.environ.get('APP_NAME', 'Metrics Storage')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = os.environ.get('DEBUG', False)

ALLOWED_HOSTS = ['*']

PROJECT_APPS = [
    'api_impl.apps.APIImplConfig',
]

INSTALLED_APPS = [
    'django_db_prefix',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'suit',
    'django.contrib.admin',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'rest_framework',
]

INSTALLED_APPS += PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = f'{APP_ID}.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {'context_processors': [
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ]},
    },
]

WSGI_APPLICATION = f'{APP_ID}.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_USER_NAME'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST': os.environ['DATABASE_HOST'],
        'PORT': os.environ['DATABASE_PORT'],
    },
}

DB_PREFIX = f'{APP_ID}_'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

DATE_FORMAT = 'd.m.Y'

REST_DATE_FORMAT = '%d.%m.%Y'

DATE_INPUT_FORMATS = settings.DATE_INPUT_FORMATS + [REST_DATE_FORMAT]

USE_I18N = False

USE_L10N = False

USE_TZ = True

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOCAL_PATHS = [os.path.join(BASE_DIR, 'locale')]

# ******************** REST FRAMEWORK ********************

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 50,
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}

# ******************** ADMIN ********************

SUIT_CONFIG = {
    'ADMIN_NAME': APP_NAME + ' Admin',
    'SEARCH_URL': '',
    'MENU': (
        {'app': 'api_impl', 'label': 'Entities', 'icon': 'icon-globe'},
    ),
}

# ******************** LOGGING ********************

LOGGER_NAME = os.environ.get('LOGGER_NAME', 'service_logger')

LOGGING_MODE = 'DEBUG'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,

    'formatters': {
        'verbose': {
            '()': 'logging_json_formatter.AppendJSONFormatter',
            'format': '%(message)s %(asctime)s',
            'limit_keys_to': ['levelname', 'call_id', 'function', 'input_data', 'result'],
        },
    },

    'handlers': {
        'console': {
            'level': LOGGING_MODE,
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'verbose',
        },
    },

    'loggers': {
        LOGGER_NAME: {
            'handlers': ['console'],
            'level': os.environ.get('LOGGING_LEVEL', 'INFO'),
        },
    },
}
