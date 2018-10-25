# sample build command: sudo docker build -t media-warrior-base .
# sample run command: sudo docker run -d -p 80:80 arupiot/media_warrior_base:develop
# running resin.io rpi image on ubuntu with qemu
# (but) resin images have qemu built in anyway...
# sudo docker run -v /usr/bin/qemu-arm-static:/usr/bin/qemu-arm-static --rm -ti resin/rpi-raspbian

# (probably) get resin.io rpi image. Has QEMU built in
FROM resin/rpi-raspbian

RUN [ "cross-build-start" ]

# apt-get update or equivalent

RUN apt-get update 
RUN sudo apt-get dist-upgrade

# install app-utils? (since apt-get keeps complaining)

# install python 3.x
# install packages needed for Flask/omxplayer etc

RUN apt-get -y install python3
RUN apt-get -y install python3-pip
# need dbus, it's not in this image
RUN apt-get install libdbus-1-dev 
RUN apt-get -y install omxplayer
RUN pip3 install flask
RUN pip3 install -U flask-cors
RUN pip3 install Flask-RESTful
RUN pip3 install Flask-Jsonpify
RUN pip3 install flask-inputs
RUN pip3 install omxplayer-wrapper

# copy mw_serve repo
RUN mkdir /opt/media_warrior
RUN apt-get install git
RUN git clone --single-branch -b develop https://github.com/arupiot/media_warrior.git /opt/media_warrior

# install everything needed to set up the 'Pi as a hotspot

# install expect/rclone

RUN apt-get -y install expect
RUN curl -L https://raw.github.com/pageauc/rclone4pi/master/rclone-install.sh | bash

# get gdrive service account details from usb stick

# set up gdrive remote
# creates a remote called arupiot-expect

#RUN /opt/media_warrior/mw_serve/docker/rclone/rclone_expect.sh

# sync with gdrive
# sample mlp are in mlp_samples_test

#RUN rclone lsf arupiot-expect:mlp_samples_test

#Sync songs from the gdrive
WORKDIR /home/pirate
RUN rclone sync arupiot-expect:mlp_samples_test downloads

# set up rclone cron job

# run rclone
# Sample Command for rclone:
# rclone sync remote_mlp:mlp-samples-test ./mlp_files/ -v -P

# set up rclone chronjob (updated every evening?)

# don't build angular app on the pi, it takes too long
# we serve the dist from the flask app

# serve Flask from 80
WORKDIR /opt/media_warrior/mw_serve/flask
ENTRYPOINT ["python3"]
CMD ["omx-player-service.py"]

EXPOSE 80

RUN [ "cross-build-end" ]
