import json
import os
import urllib

import requests
from flask import Flask, request
from flask_cors import CORS

from joinposter_api import JPApi

app: Flask = Flask(__name__)
CORS(app)

APP_ID = os.environ.get('JP_APP_ID')
APP_SECRET = os.environ.get('JP_APP_SECRET')

DEFAULT_URL = os.environ.get('JP_DEFAULT_URL', 'https://parkoved1.joinposter.com/api/')

JP: JPApi = None


@app.route('/jp_auth', endpoint='jp_auth')
def jp_auth():
    global JP
    if not JP:
        q_params = dict(request.args)

        params = {
            'application_id': APP_ID,
            'redirect_uri': 'http://localhost:5002/jp_auth',
        }

        if 'code' in q_params:
            params.update({
                'grant_type': 'authorization_code',
                'application_secret': APP_SECRET,
                'code': q_params['code']
            })
            url = f'{DEFAULT_URL}v2/auth/access_token'
            res = requests.post(url, params).json()

            JP = JPApi(res['access_token'])
            return json.dumps({'access_token': JP.token})

        params.update({'response_type': 'code'})
        return json.dumps({
            'url': f'https://parkoved1.joinposter.com/api/auth?{urllib.parse.urlencode(params)}'
        })
    return json.dumps({'access_token': JP.token})


@app.route('/get_products/<cat_id>', endpoint='get_products')
def get_products(cat_id):
    global JP
    return JP.get_products(cat_id)


@app.route('/get_categories', endpoint='get_categories')
def get_categories():
    global JP
    q_params = dict(request.args)
    fiscal = 0
    if 'fiscal' in q_params:
        fiscal = q_params['fiscal']
    return JP.get_categories(fiscal)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True, threaded=False)
