from utils.httpmethods import HttpMethods
import json
from utils.db_test import PostgresqlConnect
import random

""""Тестовый метод тестирования API Agro bank"""

base_url = 'https://dev-api.agrobank.uz'  # Base URL - основная ссылка для тестов


class CardsLogic(HttpMethods):

    def get_client_humo_cards(self):
        get_path = '/service/card/v1/cards'
        parameters = '?pin=31401740560010'

        get_url = base_url + get_path + parameters
        print(get_url)

        get_result = self.get(get_url)
        print(json.dumps(get_result.json(), indent=4))
        return get_result

    def get_client_uzcard_cards(self):
        get_path = '/service/card/v1/cards'
        parameters = '?pin=30902726520011'

        get_url = base_url + get_path + parameters
        print(get_url)

        get_result = self.get(get_url)
        print(json.dumps(get_result.json(), indent=4))
        return get_result

    def get_client_union_pay_cards(self):
        get_path = '/service/card/v1/cards'
        parameters = '?pin=40411800200019'

        get_url = base_url + get_path + parameters
        print(get_url)

        get_result = self.get(get_url)
        print(json.dumps(get_result.json(), indent=4))
        return get_result

    def post_create_cardid(self):
        post_path = '/service/card/v1/create-cardId'
        post_url_create_cardid = base_url + post_path
        print(post_url_create_cardid)

        cbs_id, card_number, reversed_expire_date = PostgresqlConnect.take_value_from_card_id_table()  # Переменные взяты из БД

        post_body = {
            "cbsId": cbs_id,
            "branch": "00394",
            "cardNumber": card_number,
            "expiryDate": reversed_expire_date
        }
        print("Тело запроса - " + str(post_body))
        print("БД - "f"{cbs_id} {card_number} {reversed_expire_date}")

        post_result = self.post(post_url_create_cardid, post_body)
        print(json.dumps(post_result.json(), indent=4))
        return post_result
