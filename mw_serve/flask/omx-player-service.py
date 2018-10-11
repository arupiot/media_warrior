from flask import Flask, request, send_from_directory, render_template
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
import os
# from omxplayer.player import OMXPlayer

app = Flask(__name__,  static_folder='static')
api = Api(app)

CORS(app)

AUDIO_PATH_MLP = "/opt/02_Planets_Part1_Treatment.mlp"
AUDIO_PATH_TEST = "/opt/demo_5ch/ChID-BLITS-EBU-Narration441-16b.wav"
# player = OMXPlayer(AUDIO_PATH_MLP, args=['--layout', '5.1', '-w', '-o', 'hdmi'])

# serve the angular app

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists("static/" + path):
        return send_from_directory('static/', path)
    else:
        return send_from_directory('static/', 'index.html')

class GetTrackList(Resource):
  def get(self):
      trackArray = ["karma", \
                    "the spell", \
                    "the sound bath", \
                    "the planets", \
                    "tales of bath", \
                    "the good hour", \
                    "tailor made", \
                    "synaesthsia", \
                    "hard days night", \
                    "the comforter", \
                    "validation facial"]
    #   trackList = { "track1":"KArmA", \
    #                 "track2":"ThE SpElL", \
    #                 "track3":"THe sOUnD BaTh", \
    #                 "track4":"ThE PlANEtS", \
    #                 "track5":"tALEs Of BaTH", \
    #                 "track6":"ThE gOOd HoUR", \
    #                 "track7":"TaIlOR MaDE", \
    #                 "track8":"SYnAEsTHeSIA", \
    #                 "track9":"HArD dAYS nIGHT", \
    #                 "track10":"THe CoMFOrTER", \
    #                 "track11":"VAlIdATiON fACiAL" }
      return jsonify(trackArray)     

class Play(Resource):
    def get(self):
        return jsonify({'text':'Playing funky music'}) 


class Stop(Resource):
    def get(self):
        return jsonify({'text':'Stopping funky music'}) 


api.add_resource(GetTrackList, '/get-track-list')
api.add_resource(Play, '/play')
api.add_resource(Stop, '/stop')


if __name__ == '__main__':
   app.run(debug=True, port=5002, host='0.0.0.0')
