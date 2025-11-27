# factories/services_factory.py

from services.products_service import ProductsService

def create_products_service(products_repo):
    return ProductsService(products_repo)
