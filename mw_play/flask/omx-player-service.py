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

app = Flask(__name__,  static_folder='static')
api = Api(app)

CORS(app)
TRACK_ARRAY = [ {"name" : "karma", "id":"0"}, \
                {"name":"the spell", "id":"1"}, \
                {"name":"the sound bath", "id":"2"}, \
                {"name":"the planets", "id":"3"}, \
                {"name":"tales of bath", "id":"4"}, \
                {"name":"the good hour", "id":"5"}, \
                {"name":"tailor made", "id":"6"}, \
                {"name":"synaesthsia", "id":"7"}, \
                {"name":"hard days night", "id":"8"}, \
                {"name":"the comforter", "id":"9"}, \
                {"name":"validation facial", "id":"10"}]
AUDIO_PATH_MLP = "/opt/media_warrior/mlp_samples/hard-rock.mlp"
AUDIO_PATH_TEST = "/opt/demo/test.mp4"
# player = OMXPlayer(AUDIO_PATH_MLP, args=['--layout', '5.1', '-w', '-o', 'hdmi'])

if findWindows() == False:
    from omxplayer.player import OMXPlayer
    from pathlib import Path
    from time import sleep

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

def findWindows():
    if sys.platform.startswith("win32"):
        return True
    return False

class GetTrackList(Resource):
  def get(self):
      
      return jsonify(TRACK_ARRAY)   

class GetSingleTrack(Resource):
    def get(self):
        args = getIdInput()
        return jsonify(TRACK_ARRAY[args["id"]]["name"])  

class PlaySingleTrack(Resource):
    def get(self):
        if findWindows() == False:
            player = OMXPlayer(AUDIO_PATH_MLP, args=['--layout', '5.1', '-w', '-o', 'hdmi'])

            sleep(30)

            player.quit()
            args = getIdInput()
            return jsonify("Playing track: " + TRACK_ARRAY[args["id"]]["name"]) 
        return jsonify("cannot play tracks on windows!")


class Stop(Resource):
    def get(self):
        return jsonify({'text':'Stopping funky music'}) 


api.add_resource(GetTrackList, '/get-track-list')
api.add_resource(GetSingleTrack, '/get-single-track')
api.add_resource(PlaySingleTrack, '/play-single-track')
api.add_resource(Stop, '/stop')



if __name__ == '__main__':
   app.run(debug=True, port=80, host='0.0.0.0')