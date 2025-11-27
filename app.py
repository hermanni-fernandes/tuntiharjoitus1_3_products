from flask import Flask
from controllers import products_controller

app = Flask(__name__)

# Tuotteiden reitit
app.add_url_rule("/api/products", "get_products", products_controller.get_all_products, methods=["GET"])
app.add_url_rule("/api/products/<int:product_id>", "get_product", products_controller.get_product_by_id, methods=["GET"])
app.add_url_rule("/api/products", "add_product", products_controller.add_product, methods=["POST"])
app.add_url_rule("/api/products/<int:product_id>", "update_product", products_controller.update_product, methods=["PUT"])
app.add_url_rule("/api/products/<int:product_id>", "delete_product", products_controller.delete_product, methods=["DELETE"])

if __name__ == "__main__":
    app.run(debug=True, port=5000)
