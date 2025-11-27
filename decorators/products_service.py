# decorators/products_service.py

import sqlite3
from factories.products_factory import create_products_repository
from factories.services_factory import create_products_service

def get_products_service(route_handler):
    def wrapper(*args, **kwargs):
        with sqlite3.connect("products.db") as con:
            products_repo = create_products_repository(con)
            products_service = create_products_service(products_repo)
            return route_handler(products_service, *args, **kwargs)
    return wrapper
