class ProductsService:
    def __init__(self, products_repo):
        self.products_repo = products_repo

    def get_all_products(self):
        return self.products_repo.get_all()

    def get_product_by_id(self, product_id):
        return self.products_repo.get_by_id(product_id)
