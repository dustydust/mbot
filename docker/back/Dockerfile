FROM python:3.7 as intermidiate

ENV PYTHONUNBUFFERED 1

RUN apt-get update
COPY . /data
WORKDIR /data

RUN pip install -r requirements.txt

ENTRYPOINT ["./docker/back/entrypoint.sh"]
