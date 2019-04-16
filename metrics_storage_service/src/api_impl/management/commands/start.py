import os

from django.contrib.auth.models import User
from django.core.management import call_command

from ._utils import BaseCommand


class Command(BaseCommand):
    help = 'Start service'

    def handle(self, *args, **options):
        call_command('collectstatic', clear=True, interactive=False)
        self._print_new_stage('static files are collected')

        self._wait_for_db()

        call_command('migrate', fake_initial=True, interactive=False)
        self._print_new_stage('database migration are completed')

        superuser_username = os.environ['ADMIN_USER_NAME']
        superuser_email = os.environ['ADMIN_EMAIL']
        superuser_password = os.environ['ADMIN_PASSWORD']

        if not User.objects.filter(username=superuser_username).exists():
            User.objects.create_superuser(superuser_username, superuser_email, superuser_password)
            self._print_new_stage(f'new superuser user {superuser_username} have been created')

        self._call_external_command(['uwsgi', '--ini', 'uwsgi.ini'])
