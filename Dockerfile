FROM python:3.7-alpine

MAINTAINER AShraf

ENV PYTHONBUFFERED 1



COPY ./requirments.txt /requirments.txt

RUN pip install -r /requirments.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user