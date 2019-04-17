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

## API

Service uses Django REST framework to create API.
After deployment you can find API description in browser on `https://<your_server_dns>`.

API has ordering and filtering abilities, you can find its description in browser.
Additionally for ordering and filtering service has ability to retrieve only a subset of model fields.
To specify fields send `fields` params with a request.
For example request `id` and `country` of metrics:
```
https://127.0.0.1/metrics/?fields=id%2Ccountry
```
Or, for more complex example request `id` and `CPI` of metrics for `test` country, ordered by `id`:
```
https://127.0.0.1/metrics/?country=test&fields=id%2Ccpi&ordering=id
```
If you want to group results send request to `grouped_metrics` endpoint.
By default service will group by all fields.
For example request metrics `total CPI`, `country` and `date` from `10.04.2019` to `18.04.2019` grouped by `date` and `country` ordered by `date`:
```
https://127.0.0.1/grouped_metrics/?groupby=metric_date%2Ccountry&ordering=metric_date&metric_date__gt=10.04.2019&metric_date__lt=18.04.2019
```

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
