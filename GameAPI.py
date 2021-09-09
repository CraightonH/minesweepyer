from flask import Flask, request, jsonify
import json
from Game import Game

api = Flask(__name__)
game = Game()

@api.route('/api/help')
def help():
    return Game().help()

@api.route('/api/game', methods=['GET', 'POST'])
def get_game():
    global game
    if request.method == 'POST':
        print('found post')
        json_request = request.get_json()
        del game
        game = Game(cols=json_request["columns"], rows=json_request["rows"], mines=json_request["mines"])
    return json.dumps(game.getGameBoard())

@api.route('/api/game/solution', methods=['GET'])
def get_game_solution():
    global game
    return json.dumps(game.getSolutionBoard())

@api.route('/api/game/flag', methods=['PUT'])
def putFlag():
    global game
    json_request = request.get_json()
    return str(game.addFlag((json_request["row"], json_request["column"])))

@api.route('/api/game/reveal', methods=['PUT'])
def reveal():
    global game
    json_request = request.get_json()
    return str(game.revealLocation((json_request["row"], json_request["column"])))

@api.route('/api/game/uncover', methods=['PUT'])
def uncover():
    global game
    json_request = request.get_json()
    return str(game.uncoverSafeLocations((json_request["row"], json_request["column"])))

if __name__ =='__main__':
    api.run()
    