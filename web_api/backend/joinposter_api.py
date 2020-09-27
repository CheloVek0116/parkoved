import os
import requests
from enum import Enum
import urllib

APP_ID = os.environ.get('JP_APP_ID')
APP_SECRET = os.environ.get('JP_APP_SECRET')

DEFAULT_URL = os.environ.get('JP_DEFAULT_URL', 'https://parkoved1.joinposter.com/api/')
CLIENTS_URL = f'{DEFAULT_URL}clients.'
MENU_URL = f'{DEFAULT_URL}menu.'


class CLIENT_ACTIONS(Enum):
    CREATE_CLIENT = f'{CLIENTS_URL}createClient'


class MENU_ACTIONS(Enum):
    GET_PRODUCTS = f'{MENU_URL}getProducts'
    GET_PRODUCT = f'{MENU_URL}getProduct'
    GET_CATEGORIES = f'{MENU_URL}getCategories'


class JPApi:

    def __init__(self, token: str) -> None:
        self.token = token
        self.query_params = {
            'token': self.token,
            'format': 'json'
        }

    def get_url(self, action, parameters: dict) -> str:
        return f'{action}?{urllib.parse.urlencode(parameters)}'

    def create_client(self, data: dict):
        url = self.get_url(CLIENT_ACTIONS.CREATE_CLIENT.value, {'token': self.token})
        res = requests.post(url, data).json()
        return res

    def get_products(self, cat_id: int):
        params = {
            'token': self.token,
            'type': 'products',
            'category_id': cat_id
        }
        url = self.get_url(MENU_ACTIONS.GET_PRODUCTS.value, params)
        res = requests.get(url).json()
        return res

    def get_product(self, product_id: int):
        params = {
            'token': self.token,
            'product_id': product_id
        }
        url = self.get_url(MENU_ACTIONS.GET_PRODUCT.value, params)
        res = requests.get(url).json()
        return res

    def get_categories(self, fiscal: int = 0):
        params = {
            'token': self.token,
            'fiscal': fiscal
        }
        url = self.get_url(MENU_ACTIONS.GET_CATEGORIES.value, params)
        res = requests.get(url).json()
        return res
