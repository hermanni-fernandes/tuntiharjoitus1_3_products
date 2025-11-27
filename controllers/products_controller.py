# controllers/products_controller.py

from flask import jsonify
from decorators.products_repository import get_products_repository

@get_products_repository
def get_all_products(repo):
    products = repo.all()
    return jsonify([p.to_dict() for p in products])

@get_products_repository
def get_product_by_id(repo, product_id):
    product = repo.get_by_id(product_id)

    if product is None:
        return jsonify({"error": "tuotetta ei löytynyt"}), 404

    return jsonify(product.to_dict())
