import json
from app import app


def load_categories():
    with open('%s/data/categories.json' % app.root_path, encoding='utf-8') as f:
        return json.load(f)


def load_products(category_id=None):
    with open('%s/data/product.json' % app.root_path, encoding='utf-8') as f:
        return json.load(f)


    if category_id:
          products = [p for p in products if p['category_id']== int(category_id)]
    return products