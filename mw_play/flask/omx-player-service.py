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
import json

# Kill all old omxplayers

app = Flask(__name__,  static_folder='static')
api = Api(app)

TRACK_BASE_PATH = "/media/usb/demo/"
AUDIO_PATH_TEST_MP4 = "5.1_AAC_Test.mp4"

TEST_TRACK = TRACK_BASE_PATH + AUDIO_PATH_TEST_MP4

CORS(app)

NEW_TRACK_ARRAY = []

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
    parser.add_argument('id', help='error with id')
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
        global NEW_TRACK_ARRAY
        with open('../tracks.json') as data:
            NEW_TRACK_ARRAY = json.load(data)
            for track in NEW_TRACK_ARRAY:
                track['Length'] = '5:00'
            print(NEW_TRACK_ARRAY)
            return jsonify(NEW_TRACK_ARRAY)
 
class GetSingleTrack(Resource):
    def get(self):
        global NEW_TRACK_ARRAY
        args = getIdInput()
        print(args['id'])
        for track in NEW_TRACK_ARRAY:
            if track['ID'] == args['id']:
                return jsonify(track["Name"])

class PlaySingleTrack(Resource):    
    def get(self):
        global player
        if findArm():
            args = getIdInput()
            thisTrack = None
            print('argsid: ', args["id"])
            for track in NEW_TRACK_ARRAY:
                if track["ID"] == args["id"]:
                    thisTrack = track
                    pathToTrack = TRACK_BASE_PATH + track["Name"]
            print("Playing: " + pathToTrack)
            
            print('Spawning player')
            player = OMXPlayer(pathToTrack, args=['--layout', '5.1', '-w', '-o', 'hdmi'])
            sleep(2.5)
            
                
            print("metadata: " + str(player.metadata()))
            print("Duration: " + str(player.metadata()['mpris:length']/1000/1000))

            sleep(5)
            
            print("Dur after 5: " + str(player.duration()))
            
            return jsonify("Playing track: " + track["Name"] + " length: " + str(player.metadata()['mpris:length']/1000/1000))
        
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
        return jsonify("(Killing omxplayer proc) You don't seem to be on a media_warrior...")

api.add_resource(GetTrackList, '/get-track-list')
api.add_resource(GetSingleTrack, '/get-single-track')
api.add_resource(PlaySingleTrack, '/play-single-track')
api.add_resource(PauseTrack, '/pause-track')
api.add_resource(Stop, '/stop')



if __name__ == '__main__':
   app.run(debug=True, port=80, host='0.0.0.0')
