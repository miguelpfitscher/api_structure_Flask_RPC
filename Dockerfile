FROM python:3.8.5-buster AS base
WORKDIR /usr/src/app
COPY . .
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
ENV FLASK_APP wsgi.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT=3000
ENV GUNICORN_WORKERS=1
ENV GUNICORN_THREADS=8
ENV GUNICORN_TIMEOUT=480
EXPOSE ${FLASK_RUN_PORT}
CMD gunicorn --bind :${FLASK_RUN_PORT} \
 --workers ${GUNICORN_WORKERS} \
 --threads ${GUNICORN_THREADS} \
 --timeout ${GUNICORN_TIMEOUT} \
 --access-logfile - \
 "api:create_app()"