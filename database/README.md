# Metrics storage database

This database just a regular PostgreSQL in Docker with init script which automatically create databases and users from envs on startup.

To configure databases and users you should pass a number of envs:
```
DATABASE_NAME_service_name=service_name
DATABASE_PASSWORD_service_name=very_secret_pass
DATABASE_USER_NAME_service_name=service_name
```
and init script will create database 'service_name', user 'service_name' with password 'very_secret_pass' and configure access rights for the user to created database.

## Building

To build Docker image just run:
```bash
docker build -t local/postgres:1.0 .
```
