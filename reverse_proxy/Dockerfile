FROM nginx:1.14-alpine

COPY uwsgi_params nginx.template start.sh /etc/nginx/

EXPOSE 80 443

CMD ["sh", "/etc/nginx/start.sh"]
