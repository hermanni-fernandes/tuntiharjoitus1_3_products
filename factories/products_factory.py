# factories/products_factory.py

from repositories.products_repository import ProductsRepository

def create_products_repository(con):
    return ProductsRepository(con)
