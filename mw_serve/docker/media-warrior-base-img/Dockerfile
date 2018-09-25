# sample build command: sudo docker build -t media-warrior-base .
# sample run command: sudo docker run -d -p 5002:5002 media-warrior-base-run
# running resin.io rpi image on ubuntu with qemu
# (but) resin images have qemu built in anyway...
# sudo docker run -v /usr/bin/qemu-arm-static:/usr/bin/qemu-arm-static --rm -ti resin/rpi-raspbian

# (probably) get resin.io rpi image with preinstalled node
FROM resin/raspberry-pi-node

RUN [ "cross-build-start" ]

# apt-get update or equivalent

RUN apt-get update 
RUN sudo apt-get dist-upgrade

# install python 3.x
# install packages needed for Flask/omxplayer etc

RUN apt-get install python3
RUN apt-get -y install python3-pip
RUN pip3 install flask
RUN pip3 install -U flask-cors
RUN pip3 install Flask-RESTful
RUN pip3 install Flask-Jsonpify


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

# don't build angular app on the pi, it takes too long
# we serve the dist from the flask app

# serve Flask from 5002
WORKDIR /opt/media_warrior/mw_serve/flask
ENTRYPOINT ["python3"]
CMD ["omx-player-service.py"]

EXPOSE 5002

RUN [ "cross-build-end" ]
