# sample build command: sudo docker build -t media-warrior-base .
# sample run command: sudo docker run -d -p 80:80 arupiot/media_warrior_base:develop
# running resin.io rpi image on ubuntu with qemu
# (but) resin images have qemu built in anyway...
# sudo docker run -v /usr/bin/qemu-arm-static:/usr/bin/qemu-arm-static --rm -ti resin/rpi-raspbian

# get resin.io rpi image. Has QEMU built in
FROM resin/rpi-raspbian

RUN [ "cross-build-start" ]

# make dirs

RUN mkdir opt/GCP
# ADD media-warrior-07dec249ae7a.json /opt/GCP
# ADD rclone1.43.1_expect.sh /


# apt-get update or equivalent
# install app-utils? (since apt-get keeps complaining)
# install python 3.x
# install packages needed for Flask/omxplayer etc
# need dbus, it's not in this image
# copy mw_serve repo
# install everything needed to set up the 'Pi as a hotspot
# install expect/rclone
# get gdrive service account details from usb stick
# set up gdrive remote
# creates a remote called arupiot-expect
# && \ /opt/media_warrior/mw_serve/docker/rclone/rclone_expect.sh
# sync with gdrive
# sample mlp are in mlp_samples_test
# RUN rclone lsf arupiot-expect:mlp_samples_test
# Sync songs from the gdrive

RUN apt-get update && apt-get install -y --no-install-recommends \
    apt-utils wget libfreetype6 dbus dbus-*dev libsmbclient libssh-4 \
    libpcre3 fonts-freefont-ttf fbset \
    && apt-get clean \
    && apt-get install omxplayer \
    && apt-get -y install build-essential python3-dev \
    && apt-get -y install python3-pip && \
    pip3 install dbus-python && \
    pip3 install flask && \
    pip3 install -U flask-cors && \
    pip3 install Flask-RESTful && \
    pip3 install Flask-Jsonpify && \
    pip3 install flask-inputs && \
    pip3 install omxplayer-wrapper && \
    mkdir /opt/media_warrior && \
    apt-get install git && \
    git clone --single-branch -b develop https://github.com/arupiot/media_warrior.git /opt/media_warrior && \
    apt-get -y install expect && \
    curl -L https://raw.github.com/pageauc/rclone4pi/master/rclone-install.sh | bash && \
    apt-get install man && \
    apt-get install p7zip-full && \
    curl -L https://rclone.org/install.sh | bash && \
    rclone --version
# expect rclone1.43.1_expect.sh
# rclone sync arupiot-expect:mlp_samples_test /opt/usb -v -P

# TODO:
# set up rclone cron job
# set up rclone chronjob (updated every evening?)

# don't build angular app on the pi, it takes too long
# we serve the dist from the flask app

# serve Flask from 80
WORKDIR /opt/media_warrior/mw_play/flask
ENTRYPOINT ["python3"]
CMD ["omx-player-service.py"]

EXPOSE 80

RUN [ "cross-build-end" ]
