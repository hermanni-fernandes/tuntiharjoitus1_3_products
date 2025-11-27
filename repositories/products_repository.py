import sqlite3
from models import Product

class ProductsRepository:
    def __init__(self, con):
        self.con = con

    def get_all(self):
        cur = self.con.cursor()
        cur.execute("SELECT id, nimi, kuvaus, hinta FROM products")
        rows = cur.fetchall()

        products = []
        for row in rows:
            products.append(Product(row[1], row[2], row[3], row[0]))
        return products

    def get_by_id(self, product_id):
        cur = self.con.cursor()
        cur.execute("SELECT id, nimi, kuvaus, hinta FROM products WHERE id = ?", (product_id,))
        row = cur.fetchone()

        if row is None:
            return None

        return Product(row[1], row[2], row[3], row[0])
