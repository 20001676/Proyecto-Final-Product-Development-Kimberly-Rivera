from flask import Flask, jsonify, request
import pandas as pd

import config as cfg
import pipeline_predict2 as pp

app = Flask(__name__)

@app.route("/saludar")
def saludar():
    return jsonify({"username": "kimberly"})

#ruta para predecir.
@app.route("/predecir", methods=['POST'])
def predict_from_pp():
    json_data = request.get_json()
    dataframe = pd.json_normalize(json_data)
    data = dataframe

    data = data[cfg.FEATURES]

    resultado = pp.predict(data)
    print(resultado)
    return jsonify({"Prediccion": resultado})

    