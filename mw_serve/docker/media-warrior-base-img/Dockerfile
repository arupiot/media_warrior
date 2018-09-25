# running resin.io rpi image on ubuntu with qemu
# (but) resin images have qemu built in anyway...
# sudo docker run -v /usr/bin/qemu-arm-static:/usr/bin/qemu-arm-static --rm -ti resin/rpi-raspbian

# (probably) get resin.io rpi image
FROM resin/rpi-raspbian

RUN [ "cross-build-start" ]

# apt-get update or equivalent

RUN apt-get update 
RUN sudo apt-get dist-upgrade

# install python 3.x
# install packages needed for Flask/omxplayer etc

RUN apt-get install python3


# install everything needed to set up the 'Pi as a hotspot

# install rclone

# get gdrive credentials

# run rclone
# Sample Command for rclone:
# rclone sync remote_mlp:mlp-samples-test ./mlp_files/ -v -P

# set up rclone chronjob (updated every evening?)

# copy mw_serve repo
RUN mkdir /opt/media_warrior
RUN apt-get install git
RUN git clone --single-branch -b develop https://github.com/arupiot/media_warrior.git /opt/media_warrior
RUN cd /opt/media_warrior/mw_serve/mw-serve

# build angular app
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
RUN sudo apt-get install -y nodejs
RUN node -v
RUN npm -v
RUN npm install -g @angular/cli
RUN npm install
RUN npm run build
RUN npm run start

# serve Flask from 5002

RUN [ "cross-build-end" ]