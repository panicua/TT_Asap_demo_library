FROM python:3.10-alpine3.20
LABEL authors="panicua"

ENV PYTHONUNBUFFERED 1

WORKDIR /asap_demo_library

ENV PYTHONPATH=${PYTHONPATH}:/asap_demo_library/management/commands

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
