# app.py

from flask import Flask
from controllers import products_controller

app = Flask(__name__)

# GET kaikki tuotteet
app.add_url_rule(
    "/api/products",
    "get_products",
    products_controller.get_all_products,
    methods=["GET"]
)

# GET tuote ID:n perusteella
app.add_url_rule(
    "/api/products/<int:product_id>",
    "get_product_by_id",
    products_controller.get_product_by_id,
    methods=["GET"]
)

if __name__ == "__main__":
    app.run(debug=True)
