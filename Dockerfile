FROM python:3.7-alpine

LABEL maintainer="Cafu"

RUN pip install pipenv

ENV PROJECT_DIR /usr/local/src/webapp

WORKDIR ${PROJECT_DIR}
COPY ./Pipfile ./Pipfile.lock ${PROJECT_DIR}/
RUN pipenv install --system --deploy
ENV PYTHONUNBUFFERED 1
COPY ./app ${PROJECT_DIR}
RUN adduser -D user
USER user