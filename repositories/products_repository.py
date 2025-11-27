# repositories/products_repository.py

import sqlite3
from models import Tuote

class ProductsRepository:

    def __init__(self, con):
        self.con = con

    def all(self):
        cur = self.con.cursor()
        cur.execute("SELECT * FROM products")
        rows = cur.fetchall()
        cur.close()

        products = []
        for row in rows:
            products.append(Tuote(row[1], row[2], row[3], row[0]))

        return products

    def get_by_id(self, product_id):
        cur = self.con.cursor()
        cur.execute("SELECT * FROM products WHERE id = ?", (product_id,))
        row = cur.fetchone()
        cur.close()

        if row is None:
            return None

        return Tuote(row[1], row[2], row[3], row[0])
