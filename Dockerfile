FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /api
WORKDIR /api
COPY . /api/

RUN apt-get -y update
RUN apt-get -y install binutils libproj-dev gdal-bin

RUN pip install -r requirements.txt

EXPOSE 8000
