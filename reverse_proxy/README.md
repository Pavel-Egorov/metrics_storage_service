# Metrics storage reverse proxy

The reverse proxy is just an Nginx instance with included configuration file which will be filled on startup.

To configure reverse proxy you should pass a number of envs:
```
HOSTNAME=metrics-storage.com
STATIC_PATH=/files/static
MEDIA_PATH=/files/media
SERVICE_SOCKET_PATH=/sockets/metrics_storage_service.sock
SSL_CERT_PATH=/certs/server.key
SSL_KEY_PATH=/certs/server.key
```
and init script will fill nginx.conf file with it.

## Building

To build Docker image just run:
```bash
docker build -t local/reverse-proxy:1.0 .
```
