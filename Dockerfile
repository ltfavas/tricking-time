FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED=1

RUN pip install pipenv
WORKDIR /app

COPY trickingtime /app/trickingtime
COPY Pipfile /app/Pipfile
COPY Pipfile.lock /app/Pipfile.lock
COPY .env /app/.env

RUN pipenv lock -r > requirements.txt
RUN pip install -r requirements.txt

RUN rm /app/trickingtime/manage.py
RUN mv /app/trickingtime/prod_manage.py /app/trickingtime/manage.py

RUN rm /app/trickingtime/config/wsgi.py
RUN mv /app/trickingtime/config/prod_wsgi.py /app/trickingtime/config/wsgi.py

RUN rm /app/trickingtime/config/asgi.py
RUN mv /app/trickingtime/config/prod_asgi.py /app/trickingtime/config/asgi.py



