# running resin.io rpi image on ubuntu with qemu
# (but) resin images have qemu built in anyway...
# sudo docker run -v /usr/bin/qemu-arm-static:/usr/bin/qemu-arm-static --rm -ti resin/rpi-raspbian

# (probably) get resin.io rpi image
FROM resin/rpi-raspbian

RUN [ "cross-build-start" ]

# apt-get update or equivalent

RUN apt-get update 

# install python 3.x
# install packages needed for Flask/omxplayer etc

RUN apt-get install python3
RUN apt-get install git
RUN git clone --single-branch -b develop https://github.com/arupiot/media_warrior.git

# install everything needed to set up the 'Pi as a hotspot

# install rclone

# get gdrive credentials

# run rclone
# Sample Command for rclone:
# rclone sync remote_mlp:mlp-samples-test ./mlp_files/ -v -P

# set up rclone chronjob (updated every evening?)

# copy mw_serve repo

# build angular app

# serve Flask from 5002

RUN [ "cross-build-end" ]