import json

import pytest
import requests
from utils.agro_api import base_url
from utils.check import GetValue
from utils.httpmethods import HttpMethods


@pytest.fixture(scope='session')
def token():
    http_methods = HttpMethods(token)

    post_token_path = "/service/auth/token"
    post_token_url = base_url + post_token_path

    token_body = {
        "username": "develop",
        "password": "development"
    }

    token_result = http_methods.post(post_token_url, token_body)
    access_token = GetValue.get_value_from_field(token_result, 'access_token')
    return access_token
