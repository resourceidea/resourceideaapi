FROM python:3-slim

ARG APP_ENV

ENV APP_ENV=${APP_ENV} \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.0.5

RUN pip install "poetry=${POETRY_VERSION}"

WORKDIR /code
COPY poetry.lock pyproject.toml manage.py /code/

RUN poetry config virtualenvs.create false \
    && poetry install $(test "$APP_ENV" == production && echo "--no-dev") --no-interaction --no-ansi

COPY . /code