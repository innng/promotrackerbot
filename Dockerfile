FROM python:3.7.2

ARG TOKEN
ENV TELEGRAM_BOT_TOKEN $TOKEN

COPY . /app
WORKDIR /app

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
RUN /root/.poetry/bin/poetry install

CMD ["/root/.poetry/bin/poetry", "run", "python", "promotrackerbot/__main__.py"]
