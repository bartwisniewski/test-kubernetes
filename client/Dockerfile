FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY clientproject/ .

CMD python manage.py runserver 0.0.0.0:8000