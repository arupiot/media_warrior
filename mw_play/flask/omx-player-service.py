from flask import Flask, request, send_from_directory, render_template
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
from flask_restful import reqparse

# from omxplayer.player import OMXPlayer
# from pathlib import Path
# from time import sleep

import os
import sys
import time
import subprocess

# Kill all old omxplayers

player = None

os.system("killall omxplayer.bin")

app = Flask(__name__,  static_folder='static')
api = Api(app)

TRACK_BASE_PATH = "/media/usb/demo/"
AUDIO_PATH_TEST_MP4 = "5.1_AAC_Test.mp4"

CORS(app)
TRACK_ARRAY = [ {"name" : "02_Planets_Part1_Treatment.mlp", "id":"0"}, \
                {"name": AUDIO_PATH_TEST_MP4, "id":"1"}, \
                {"name":"the sound bath", "id":"2"}, \
                {"name":"the planets", "id":"3"}, \
                {"name":"tales of bath", "id":"4"}, \
                {"name":"the good hour", "id":"5"}, \
                {"name":"tailor made", "id":"6"}, \
                {"name":"synaesthsia", "id":"7"}, \
                {"name":"hard days night", "id":"8"}, \
                {"name":"the comforter", "id":"9"}, \
                {"name":"validation facial", "id":"10"}]

# player = OMXPlayer(AUDIO_PATH_MLP, args=['--layout', '5.1', '-w', '-o', 'hdmi'])

# serve the angular app

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists("static/" + path):
        return send_from_directory('static/', path)
    else:
        return send_from_directory('static/', 'index.html')

def getIdInput():
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=int, help='error with id')
    args = parser.parse_args()
    return args

def findArm():
    if os.uname().machine == 'armv7l':
        return True
    return False

if findArm():
    from omxplayer.player import OMXPlayer
    from pathlib import Path
    from time import sleep

class GetTrackList(Resource):
  def get(self):
      
      return jsonify(TRACK_ARRAY)   

class GetSingleTrack(Resource):
    def get(self):
        args = getIdInput()
        return jsonify(TRACK_ARRAY[args["id"]]["name"])  

class PlaySingleTrack(Resource):
    def get(self):
        global player
        if findArm():
            
            args = getIdInput()
            pathToTrack = TRACK_BASE_PATH + TRACK_ARRAY[args["id"]]["name"]
            print("Playing: " + pathToTrack)

            player = OMXPlayer(pathToTrack, args=['-w'])
            sleep(2.5)
            print("metadata: " + str(player.metadata()))
            print("Duration: " + str(player.metadata()['mpris:length']/1000/1000))

            sleep(5)
            
            print("Dur after 5: " + str(player.duration()))
            
            return jsonify("Playing track: " + TRACK_ARRAY[args["id"]]["name"] + " length: " + str(player.metadata()['mpris:length']/1000/1000)) 
        return jsonify("(Playing) You don't seem to be on a media_warrior...")

class PauseTrack(Resource):
    def get(self):
        global player
        if findArm():
            # Pause the track
            if player.can_pause():
                player.pause()
            
            return jsonify("Pause successful!") 
        return jsonify("(Pausing) You don't seem to be on a media_warrior...")
        
class Stop(Resource):
    def get(self):
        if findArm():
            # For the moment, kill every omxplayer process
            os.system("killall omxplayer.bin")
            print('omxplayer processes killed!')
            
            return jsonify("omxplayer processes killed") 


api.add_resource(GetTrackList, '/get-track-list')
api.add_resource(GetSingleTrack, '/get-single-track')
api.add_resource(PlaySingleTrack, '/play-single-track')
api.add_resource(PauseTrack, '/pause-track')
api.add_resource(Stop, '/stop')



if __name__ == '__main__':
   app.run(debug=True, port=80, host='0.0.0.0')
