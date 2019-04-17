from django.apps import AppConfig
from django.conf import settings


class APIImplConfig(AppConfig):
    name = 'api_impl'
    verbose_name = settings.APP_NAME
