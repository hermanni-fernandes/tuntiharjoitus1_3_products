from flask import jsonify
from decorators.products_service import get_products_service

@get_products_service
def get_all_products(products_service):
    products = products_service.get_all_products()
    return jsonify([p.to_dict() for p in products])

@get_products_service
def get_product_by_id(products_service, product_id):
    product = products_service.get_product_by_id(product_id)

    if product is None:
        return jsonify({"error": "product not found"}), 404

    return jsonify(product.to_dict())
