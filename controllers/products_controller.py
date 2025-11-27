from flask import request, jsonify
from decorators.products_repository import get_products_repository

@get_products_repository
def get_all_products(repo):
    products = repo.get_all()
    return jsonify([p.to_dict() for p in products])

@get_products_repository
def add_product(repo):
    data = request.get_json()
    name = data.get("name")
    price = data.get("price")

    product = repo.add(name, price)
    return jsonify(product.to_dict()), 201
