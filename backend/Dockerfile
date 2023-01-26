FROM python:3.7-slim

COPY ./ /app

WORKDIR /app

COPY backend/requirements.txt pwd

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

RUN pip3 install --upgrade pip && pip3 install -r backend/requirements.txt --no-cache-dir

CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000"]