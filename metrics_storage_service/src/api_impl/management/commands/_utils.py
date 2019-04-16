import subprocess
import sys
from time import monotonic, sleep

import psycopg2
from django.conf import settings
from django.core.management.base import BaseCommand as _BaseCommand


class BaseCommand(_BaseCommand):
    db_preferences = {
        **settings.DATABASES['default'],
    }

    def handle(self):
        raise NotImplementedError

    def _wait_for_db(self, timeout=15):
        start_time = monotonic()
        connection = None

        name = self.db_preferences['NAME']
        user = self.db_preferences['USER']
        password = self.db_preferences['PASSWORD']
        host = self.db_preferences['HOST']
        port = self.db_preferences['PORT']

        while monotonic() - start_time < timeout:
            try:
                connection = psycopg2.connect(database=name, user=user, password=password, host=host, port=port)
                cursor = connection.cursor()
                cursor.execute('SELECT 1')

                self._print_new_stage(f'connection to DB {name} ({host}/{port}) is established')

                return
            except psycopg2.Error:
                self._print_new_stage(f'Wait for Database for {int(monotonic() - start_time)} seconds')
                sleep(1)
            finally:
                if connection is not None:
                    connection.close()

    @staticmethod
    def _call_external_command(command):
        return subprocess.check_call(command, stdout=sys.stdout, stderr=sys.stderr)

    @staticmethod
    def _print_new_stage(state_description):
        print(state_description.upper())
