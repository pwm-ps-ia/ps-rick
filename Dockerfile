FROM python:3.10

RUN apt-get update -y
RUN apt-get install cron -y

RUN mkdir /code
WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install -U pipenv
RUN pip install -U gunicorn
RUN pip install -U psycopg2
RUN pip install -U python-crontab

COPY . /code/


RUN pipenv install --system

RUN python3 manage.py migrate --no-input
RUN python3 manage.py collectstatic --no-input

EXPOSE 8000