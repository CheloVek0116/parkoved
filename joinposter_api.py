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


class JPApi:

    def __init__(self, token: str) -> None:
        self.token = token
        self.query_params = {
            'token': self.token,
            'format': 'json'
        }

    def get_url(self, action, parameters: dict) -> str:
        return f'{action}?{urllib.parse.urlencode(parameters)}'

    def create_client(self, data: dict) -> int:
        url = self.get_url(CLIENT_ACTIONS.CREATE_CLIENT.value, {'token': self.token})
        res = requests.post(url, data).json()
        return res


if __name__ == '__main__':
    jp = JPApi('495627:1047981decc723d9fa67ff05d0052bb2')
    jp.create_client({
        'client_name': 'Попова Елена Андреевна',
        'client_sex': 2,
        'client_groups_id_client': 1,
        'card_number': '00000000022',
        'discount_per': 0,
        'phone': '+380519911124',
        'email': 'contact@joinposter.com',
        'birthday': '1986-11-23',
        'bonus': 10,
        'total_payed_sum': 417000,
    })
