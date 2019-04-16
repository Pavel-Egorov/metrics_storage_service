import os

from django.apps import AppConfig


class APIImplConfig(AppConfig):
    name = 'api_impl'
    verbose_name = os.environ['APP_NAME']
