from flask import Flask, jsonify, request 

app = Flask(__name__)

playlist = [
    {"id": 1, " titulo": "baby", "artista": "Justin bieber"},
    {"id": 2, " titulo": "naqela mesa", "artista": "Nelson golçales"}

]

@app.route("/musica/<int:id>", methods=["GET"])
def get_musica(id):
    for musica in playlist:
        if music['id']== id:   
            return jsonify

@app.route('/musicas', methods=['GET'])
def get_musicas():
    return jsonify({"playlist": playlist, "total": len(playlist)})
app.run()

@app.route('/musicas', methods=['POST'])
def add_musica():
    nova_musica = request.json

    nova_musica["id"] = len(playlist) + 1

    playlist.append(nova_musica)
    return jsonify({"mensagem": "Musica adicionada!", "musica": nova_musica}), 201