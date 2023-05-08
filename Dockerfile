FROM python:3.8

ENV PYTHONUNBUFFERED=1

WORKDIR /libapp

COPY  requirements.txt requirements.txt

COPY . .

RUN apt-get update && apt-get install -y python3

RUN pip3 install psycopg2-binary

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
