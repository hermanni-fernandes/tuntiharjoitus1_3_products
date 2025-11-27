# decorators/products_repository.py

import sqlite3
from factories.products_factory import create_products_repository

def get_products_repository(route_handler_func):
    def wrapper(*args, **kwargs):

        with sqlite3.connect("products.db") as con:

            repo = create_products_repository(con)

            return route_handler_func(repo, *args, **kwargs)

    return wrapper
