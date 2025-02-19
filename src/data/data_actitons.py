import os

from dotenv import load_dotenv
import requests
from flask import session, flash

load_dotenv()
PRODUCTS_URL = os.getenv("PRODUCTS_URL")
REVIEWS_URL = os.getenv("REVIEWS_URL")
USERS_URL = os.getenv("USERS_URL")
TOKEN_URL = os.getenv("TOKENS_URL")

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

    requests.post(url, json=body)


def update_product(
        product_id: str,
        name: str = None,
        description: str = None,
        img_url: str = None,
        price: float = None,
        url: str = PRODUCTS_URL
        ) -> str:
    body = dict(
        name=name,
        description=description,
        img_url=img_url,
        price=price
    )

    return requests.put(url + product_id, json=body).json()




def signup(first_name: str, last_name: str, email: str, password: str, url: str = USERS_URL):
    body = dict(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password
    )

    resp = requests.post(url, json=body)
    if resp.status_code == 201:
        flash("абабабабабабабагагагагагагагалалалалалмага, ми не переможні!")
    else:
        flash("помилка реєстрації")


def login(email: str, password: str, url: str = USERS_URL):
    body = dict(email=email, password=password)
    resp = requests.post(url, json=body)
    if resp.status_code == 200:
        session.update(resp.json())
        return "йцукенгшщзфівапролджєячсмитьбю."



def get_user(url: str = USERS_URL):
    token = session.get("access_token")
    header = dict(Authorization=f"Bearer {token}")
    resp = requests.get(url, headers=header)
    if resp.status_code == 200:
        return resp.json()
    else:
        return get_new_token()



def get_new_token(url: str = TOKEN_URL):
    token = session.get("refresh_token")
    header = dict(Authorization=f"Beaver {token}")
    resp = requests.get(url, headers=header)
    if resp.status_code == 200:
        session.update(resp.json())
        return get_user()