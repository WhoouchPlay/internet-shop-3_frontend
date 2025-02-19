import os

from dotenv import load_dotenv
import requests


load_dotenv()
PRODUCTS_URL = os.getenv("PRODUCTS_URL")
REVIEWS_URL = os.getenv("REVIEWS_URL")


def get_products(url: str = PRODUCTS_URL) -> list[dict]:
    return requests.get(url).json()


def get_product(product_id: str, url: str = PRODUCTS_URL) -> dict:
    return requests.get(url + product_id).json()


def add_product(name: str, description: str, img_url: str, price: float, url: str = PRODUCTS_URL) -> str:
    body = dict(
        name=name,
        description=description,
        img_url=img_url,
        price=price
    )
    return requests.post(url, json=body)


def update_product(
    product_id: str,
    name: str,
    description: str,
    img_url: str,
    price: float,
    url: str = PRODUCTS_URL
) -> str:
    body = dict(
        name=name,
        description=description,
        img_url=img_url,
        price=price
    )
    return requests.put(url + product_id, json=body).json()