FROM resin/rpi-raspbian:stretch

# sample build command: sudo docker build -t mw_rpi_base .
# get resin.io stretch raspbian image. Has QEMU built in
# mw_rpi_base dockerfile
# Resin.io (balena) base image
# python3-dev
# python3-pip
# dbus dev libraries
# ifmetric
# ntp

RUN [ "cross-build-start" ]

RUN apt-get update && apt-get install -y --no-install-recommends \
   apt-utils wget libfreetype6 dbus dbus-*dev libsmbclient libssh-4 \
   libpcre3 fonts-freefont-ttf fbset \
   && apt-get clean \
   && apt-get -y install omxplayer \
   build-essential python3-dev \
   python3-pip \
   ntp \
   ifmetric

RUN [ "cross-build-end" ]
