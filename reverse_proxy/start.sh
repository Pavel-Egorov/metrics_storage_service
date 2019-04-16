#!/bin/sh -e

for template in /etc/nginx/*.template; do
  cat ${template} | envsubst '\
    ${HOSTNAME} \
    ${STATIC_PATH} \
    ${MEDIA_PATH} \
    ${SERVICE_SOCKET_PATH} \
    ${SSL_CERT_PATH} \
    ${SSL_KEY_PATH} \
' > ${template/.template/.conf}
done

nginx -g 'daemon off;'
