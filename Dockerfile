FROM python:latest

MAINTAINER vk
RUN mkdir /automation

COPY ./ /automation
COPY ./setup.py /automation

WORKDIR /automation

RUN python3 setup.py install


