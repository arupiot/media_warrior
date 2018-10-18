from flask import Flask, request, send_from_directory, render_template
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
from flask_restful import reqparse
import os
# from omxplayer.player import OMXPlayer

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
      
      return jsonify(TRACK_ARRAY)   

class GetSingleTrack(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, help='error with id')
        args = parser.parse_args()
        print(args)
        return jsonify(TRACK_ARRAY[args["id"]]["name"])  

class Play(Resource):
    def get(self):
        return jsonify({'text':'Playing funky music'}) 


class Stop(Resource):
    def get(self):
        return jsonify({'text':'Stopping funky music'}) 


api.add_resource(GetTrackList, '/get-track-list')
api.add_resource(GetSingleTrack, '/get-single-track')
api.add_resource(Play, '/play')
api.add_resource(Stop, '/stop')


if __name__ == '__main__':
   app.run(debug=True, port=80, host='0.0.0.0')
