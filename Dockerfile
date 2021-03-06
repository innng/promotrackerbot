FROM python:3.8.2

ARG TELEGRAM_BOT_TOKEN
ENV TELEGRAM_TOKEN ${TELEGRAM_BOT_TOKEN}

ARG REDIS_DOCKER_HOST
ENV REDIS_HOST ${REDIS_DOCKER_HOST}

ARG REDIS_DOCKER_PORT
ENV REDIS_PORT ${REDIS_DOCKER_PORT}

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
RUN /root/.poetry/bin/poetry config virtualenvs.create false

COPY . /app
WORKDIR /app

RUN /root/.poetry/bin/poetry install
