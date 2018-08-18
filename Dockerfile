FROM python:3

RUN mkdir /api
WORKDIR /api
COPY . /api/

RUN pip install -r requirements.txt

EXPOSE 8000
