import os
import sys

# ******************** COMMON ********************

APP_ID = os.environ['APP_ID']

APP_NAME = os.environ['APP_NAME']

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = os.environ['DEBUG']

ALLOWED_HOSTS = ['*']

PROJECT_APPS = [
    'api_impl.apps.APIImplConfig',
]

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'suit',
    'django.contrib.admin',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOCAL_PATHS = [os.path.join(BASE_DIR, 'locale')]

# ******************** ADMIN ********************

SUIT_CONFIG = {
    'ADMIN_NAME': APP_NAME + ' Admin',
    'SEARCH_URL': '',
    'MENU': (
        {'app': 'api_impl', 'label': 'Entities', 'icon': 'icon-globe'},
    ),
}

# ******************** LOGGING ********************

LOGGER_NAME = os.environ['LOGGER_NAME']

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
            'level': os.environ['LOGGING_LEVEL'],
        },
    },
}
