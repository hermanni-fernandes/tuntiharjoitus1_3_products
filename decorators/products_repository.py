from factories.products_factory import create_products_repository

def get_products_repository(route_handler):
    def wrapper(*args, **kwargs):
        repo = create_products_repository()
        return route_handler(repo, *args, **kwargs)
    return wrapper
