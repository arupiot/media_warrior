# sample build command: sudo docker build -t mw_rclone .
# sample run command: sudo docker run -d -p 80:80 arupiot/media_warrior_base:develop
# running resin.io rpi image on ubuntu with qemu
# (but) resin images have qemu built in anyway...
# sudo docker run -v /usr/bin/qemu-arm-static:/usr/bin/qemu-arm-static --rm -ti resin/rpi-raspbian

# get media warrior rpi image. (QEMU/Python/dbus/etc)
FROM mw_rpi_base

RUN [ "cross-build-start" ]
# ADD media-warrior-07dec249ae7a.json /opt/GCP
# ADD rclone1.43.1_expect.sh /
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

RUN mkdir /media/usb

RUN apt-get install git && \
    git clone --single-branch -b mw-23 https://github.com/arupiot/media_warrior.git /opt/media_warrior && \
    apt-get -y install expect && \
    apt-get install man && \
    apt-get install p7zip-full && \
    curl -L https://rclone.org/install.sh | bash && \
    rclone --version

WORKDIR /opt/media_warrior/mw_rclone
RUN expect rclone1.43.1_expect.sh
# rclone sync arupiot-expect:mlp_samples_test /opt/media_warrior/mlp_samples -v -P

# TODO:
# set up rclone cron job
# set up rclone chronjob (updated every evening?)


RUN [ "cross-build-end" ]
