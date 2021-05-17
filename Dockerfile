FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /djangotodo
WORKDIR /djangotodo

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
libsqlite3-dev

RUN pip install -U pip setuptools

COPY requirements.txt /djangotodo/
COPY requirements-opt.txt /djangotodo/

RUN pip install -r /djangotodo/requirements.txt
RUN pip install -r /djangotodo/requirements-opt.txt

ADD . /djangotodo/

EXPOSE 8000