# Metrics storage service

The service stores and process advertising metrics.

## Architecture

Service itself is a regular Django project with one application `api_impl`.
Project is deployed with uwsgi which interacts with nginx via unix socket to provide access to API and etc.
SSL support is configured on nginx level.

All dependencies are installed and managed via `pipenv`.

Service is started via custom manage.py command `start`.

Project has `utils` module with `log` decorator to trace functions calls for debugging.
Output is written to stdout.

## Configuring

To configure service you should pass a number of envs:
```
APP_ID=metrics_storage_service
APP_NAME - human readable service name
DJANGO_SETTINGS_MODULE=metrics_storage_service.settings
DEBUG - empty string to disable debug
SECRET_KEY - Django secret key
LOGGING_LEVEL - logging level, for examle INFO
DATABASE_HOST - PostgreSQL host
DATABASE_PORT - PostgreSQL port, for example 5432
LOGGER_NAME - logger name
DATABASE_NAME - database name to use
DATABASE_USER_NAME - database user to use
DATABASE_PASSWORD - database password to use
ADMIN_USER_NAME - superuser username to use
ADMIN_EMAIL - superuser email to use
ADMIN_PASSWORD - superuser password to use
```

## Building

To build Docker image just run:
```bash
docker build -t local/metrics-storage:1.0 ./metrics_storage_service
```
