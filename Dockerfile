FROM python:3.6

ENV PYTHONUNBUFFERED 1

WORKDIR /djangotodo

COPY . ./

RUN pip3 install -r requirements.txt
