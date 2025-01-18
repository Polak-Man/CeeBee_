from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/receive', methods=['POST'])
def receive_data():
    data = request.get_json()
    file = data.get('file')
    text_input = data.get('textInput')
    name = data.get('name')
    show_pseudo = data.get('showPseudo')
    duration_sec = data.get('durationSec')
    duration_ms = data.get('durationMs')

    # Afficher le contenu reçu
    print(f"Client {name} a reçu :")
    print(f"Fichier : {file}")
    print(f"Texte : {text_input}")
    print(f"Afficher Pseudo : {show_pseudo}")
    print(f"Durée (sec) : {duration_sec}")
    print(f"Durée (ms) : {duration_ms}")

    return jsonify({"message": "Données reçues avec succès"}), 200

if __name__ == '__main__':
    app.run(port=8081)  # Assurez-vous que le port correspond à celui utilisé dans l'API