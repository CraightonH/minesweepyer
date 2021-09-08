from flask import Flask, request, jsonify
import json
from Game import Game

class GameAPI:
    game = Game()
    api = Flask(__name__)

    @api.route('/api')
    def index():
        return "API Server Works!"

    @api.route('/api/help')
    def help():
        global game
        return game.help()

    @api.route('/api/game', methods=['GET', 'POST'])
    def get_game():
        global game
        if request.method == 'POST':
            json_request = request.get_json()
            global game
            game = None
            game = Game(cols=json_request["columns"], rows=json_request["rows"], mines=json_request["mines"])
        return json.dumps(game.getGameBoard())

    @api.route('/api/game/solution', methods=['GET'])
    def get_game_solution():
        global game
        return json.dumps(game.getSolutionBoard())

    @api.route('/api/flag', methods=['PUT'])
    def addFlag(self):
        global game
        json_request = request.get_json()

    def run(self):
        api.run()

if __name__ =='__main__':
    api = GameAPI()
    api.run()
    