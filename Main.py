from allrequests import *

@app.route('/games', methods=['GET'])
def get_games():
    return jsonify(Games.get_all_games())


@app.route('/games/<int:id>', methods=['GET'])
def get_game_by_id(id):
    return_value = Games.get_game(id)
    return jsonify(return_value)


@app.route('/games', methods=['POST'])
def add_game():
    request_data = request.get_json()
    Games.add_game(request_data['name'], request_data['genre'],
                   request_data['score'], request_data['image'])
    response = Response("Game Added To The List", 201, mimetype='application/json')
    return response


@app.route('/games/<int:id>', methods=['PUT'])
def update_game(id):
    request_data = request.get_json()
    Games.update_game(id, request_data['name'], request_data['genre'], 
                      request_data['score'], request_data['image'])

    response = Response("Game Updated", status=200, mimetype='application/json')
    return response

@app.route('/games/<int:id>', methods=['DELETE'])
def delete_games(id):
    Games.delete_game(id)
    response = Response("Game Removed", status=200, mimetype='application/json')
    return response

if __name__ == "__main__":
    app.run(debug=True)
