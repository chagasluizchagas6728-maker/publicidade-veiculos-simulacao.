from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder="static")
CORS(app)

# Simulação: Armazena anúncio na memória (não persiste reiniciando o servidor)
campaign = {"title": "", "image_url": ""}

@app.route("/")
def serve_index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/add_campaign", methods=["POST"])
def add_campaign():
    global campaign
    data = request.json
    campaign["title"] = data.get("title", "")
    campaign["image_url"] = data.get("image_url", "")
    return jsonify({"status": "ok", "campaign": campaign})

@app.route("/get_campaign", methods=["GET"])
def get_campaign():
    return jsonify(campaign)

@app.route("/register_view", methods=["POST"])
def register_view():
    # Aqui poderíamos registrar a visualização em um banco de dados
    return jsonify({"status": "view registered"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
