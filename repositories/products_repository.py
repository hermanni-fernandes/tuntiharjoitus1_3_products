from models import Tuote

class ProductsRepository:

    def __init__(self):
        # väliaikainen tietovarasto (muistiin)
        self.products = []
        self.next_id = 1

    def get_all(self):
        return self.products

    def get_by_id(self, product_id):
        for p in self.products:
            if p.id == product_id:
                return p
        return None

    def add(self, name, price):
        product = Product(name, price, self.next_id)
        self.products.append(product)
        self.next_id += 1
        return product

    def remove(self, product_id):
        for p in self.products:
            if p.id == product_id:
                self.products.remove(p)
                return True
        return False
