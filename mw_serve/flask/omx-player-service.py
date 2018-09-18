from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
# from omxplayer.player import OMXPlayer

app = Flask(__name__)
api = Api(app)

CORS(app)

AUDIO_PATH_MLP = "/opt/02_Planets_Part1_Treatment.mlp"
AUDIO_PATH_TEST = "/opt/demo_5ch/ChID-BLITS-EBU-Narration441-16b.wav"
# player = OMXPlayer(AUDIO_PATH_MLP, args=['--layout', '5.1', '-w', '-o', 'hdmi'])

@app.route("/")
def hello():
    return jsonify({'text':'World, Hello?'})  

class GetTrackList(Resource):
  def get(self):
     
      return jsonify({'text':'No tracks found!'})     

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
   app.run(port=5002)