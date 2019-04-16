FROM python:3.7-alpine

RUN apk --update add build-base cmake linux-headers libxslt-dev libxml2-dev libc-dev postgresql-dev libffi-dev
RUN pip install pipenv && rm -rf ~/.cache/pip && rm -rf /tmp/*

WORKDIR /main_project

COPY src/Pipfile src/Pipfile.lock ./
RUN pipenv sync && rm -rf ~/.cache/pipenv && rm -rf /tmp/*

COPY src/ ./

ENTRYPOINT pipenv run start
