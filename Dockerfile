FROM ubuntu:14.04

MAINTAINER Diego Dukão

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y software-properties-common
RUN apt-add-repository ppa:kivy-team/kivy
RUN add-apt-repository ppa:mc3man/trusty-media
RUN apt-get update
RUN apt-get install -y python-pip \
    build-essential \
    git \
    python-dev \
    ffmpeg \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    zlib1g-dev \
    vim \
    python-kivy \
    kivy-examples

