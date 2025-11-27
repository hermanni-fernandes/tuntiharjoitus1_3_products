# controllers/products_controller.py

from flask import jsonify, request
from models import Tuote

# väliaikainen tietovarasto (vain tehtävä 1 varten)
tuotteet = []
seuraava_id = 1

def get_all_products():
    return jsonify([
        {
            "id": t.id,
            "nimi": t.nimi,
            "kuvaus": t.kuvaus,
            "hinta": t.hinta
        }
        for t in tuotteet
    ])

def get_product_by_id(product_id):
    for t in tuotteet:
        if t.id == product_id:
            return jsonify({
                "id": t.id,
                "nimi": t.nimi,
                "kuvaus": t.kuvaus,
                "hinta": t.hinta
            })
    return jsonify({"error": "Tuotetta ei löydy"}), 404

def add_product():
    global seuraava_id

    data = request.get_json()
    nimi = data.get("nimi")
    kuvaus = data.get("kuvaus")
    hinta = data.get("hinta")

    if not nimi or not kuvaus or hinta is None:
        return jsonify({"error": "Kaikki kentät ovat pakollisia"}), 400

    tuote = Tuote(nimi, kuvaus, hinta, _id=seuraava_id)
    tuotteet.append(tuote)
    seuraava_id += 1

    return jsonify({
        "id": tuote.id,
        "nimi": tuote.nimi,
        "kuvaus": tuote.kuvaus,
        "hinta": tuote.hinta
    })

def update_product(product_id):
    data = request.get_json()

    for t in tuotteet:
        if t.id == product_id:
            t.nimi = data.get("nimi", t.nimi)
            t.kuvaus = data.get("kuvaus", t.kuvaus)
            t.hinta = data.get("hinta", t.hinta)

            return jsonify({
                "id": t.id,
                "nimi": t.nimi,
                "kuvaus": t.kuvaus,
                "hinta": t.hinta
            })
    return jsonify({"error": "Tuotetta ei löydy"}), 404

def delete_product(product_id):
    for t in tuotteet:
        if t.id == product_id:
            tuotteet.remove(t)
            return "", 204
    return jsonify({"error": "Tuotetta ei löydy"}), 404
