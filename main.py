from flask import Flask, request, jsonify

app = Flask(__name__)

# Variável para armazenar a localização
current_location = {"latitude": None, "longitude": None}

@app.route("/update", methods=["POST"])
def update_location():
    latitude = request.form.get("latitude")
    longitude = request.form.get("longitude")
    if latitude and longitude:
        global current_location
        current_location = {"latitude": float(latitude), "longitude": float(longitude)}
        return "Localização recebida com sucesso!", 200
    return "Erro: dados inválidos!", 400

@app.route("/location", methods=["GET"])
def get_location():
    return jsonify(current_location)

if __name__ == "__main__":
    import os
    port = int(os.getenv("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
