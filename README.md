# Metrics storage

This service store and process advertising metrics.

## Architecture

Service consists of three Docker containers which are deployed via Docker Compose:
1. `metrics-storage` - service itself.
2. `database` - PostgreSQL database to store metrics.
3. `reverse-proxy` - Nginx to provide access to API and server static.

All containers has its own README file where you can find detailed information about each.

## Production deployment

For production deployment you must as minimum:
1. Disable DEBUG if it is enabled.
2. Deploy services via something like Kubernetes to achieve scalability and availability.
3. Restrict access to admin interface. To do it you can deploy it in separate container and different port and configure firewall for example.
4. Configure some storage to store and analyze logs, Graylog + Sentry for example.
5. Configure something like CloudFlare to mitigate DDoS attacks.
6. Configure API to be available only for authorised users.

## Deployment

To deploy service follow below steps from root of the repository.

1. Install latest versions of Docker and Docker-compose.
2. Build required Docker images:
    ```bash
    docker build -t local/metrics-storage:1.0 ./metrics_storage_service
    docker build -t local/postgres:1.0 ./database
    docker build -t local/reverse-proxy:1.0 ./reverse_proxy
    ```
3. Create directory to store Docker volumes somewhere in your system.
4. Create SSL certificates if don't have existing (in below example self-signed certificates will be created, for 
production use smth like LetsEncrypt to create certificates):
    ```bash
    mkdir -p <your_volumes_dir>/certs
    openssl req -x509 -sha256 -nodes -newkey rsa:2048 -days 365 -keyout <your_volumes_dir>/certs/server.key -out <your_volumes_dir>/certs/server.crt
    ```
5. Fill required params in docker-compose-template:
    ```
    VOLUMES_DIRECTORY_PATH - full path to created volumes directory
    DATABASE_PASSWORD - generate secure password for database
    ADMIN_EMAIL - use your email to create superuser
    ADMIN_PASSWORD - generate secure password to access admin interface
    SECRET_KEY - generate secure string
    HOSTNAME - use DNS name of your host (or localhost)
    DATABASE_PASSWORD_metrics_storage - use DB password which you have generated above
    ```
6. Start service:
    ```bash
    cp docker-compose-template docker-compose
    docker-compose up -d
    ```

After performing above steps service will be available on `https://<your_server_dns>`.
Admin interface will be available at `https://<your_server_dns>/admin`.
To access admin interface use `admin` as username and your `ADMIN_PASSWORD` value as password.
