from requests import Response
from utils.httpmethods import HttpMethods
from utils.agro_api import CardsLogic
from utils.check import Check
from utils.check import GetValue

"""Запуск наших тестов"""


class TestRunLogicCards:

    def test_get_client_cards_humo(self, token):
        cards_logic = CardsLogic(token=token)
        print("Метод GET CLIENT HUMO CARDS")

        result_get_humo: Response = cards_logic.get_client_humo_cards()

        """Взятие данных из ответа запроса"""
        expire_date = GetValue.get_value_from_item_of_list(result_get_humo, 'cards', 0, 'expiryDate')
        payment_system = GetValue.get_value_from_item_of_list(result_get_humo, 'cards', 0, 'paymentSystem')

        """"Проверки для данных"""
        Check.check_status_code(result_get_humo, 200)

        print("Метод GET CLIENT UZCARD CARDS")
        result_get_uzcard: Response = cards_logic.get_client_uzcard_cards()

        """"Проверки для данных"""
        Check.check_status_code(result_get_uzcard, 200)

        print("Метод GET CLIENT UNION PAY CARDS")
        result_get_union_pay: Response = cards_logic.get_client_union_pay_cards()

        """"Проверки для данных"""
        Check.check_status_code(result_get_union_pay, 200)

    def test_create_card_id(self, token):
        cards_logic = CardsLogic(token=token)

        print("Метод POST Create CardID")
        result_post_create_card_id = Response = cards_logic.post_create_cardid()

        Check.check_status_code(result_post_create_card_id, 200)
