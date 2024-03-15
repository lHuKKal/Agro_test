# import allure
import requests

# from utils.logger import Logger

"""Список HTTP методов"""


class HttpMethods:

    def __init__(self, token):
        self.headers = {
            'content-type': 'application/json',
            'Authorization': f'Barrier {token}'
        }
        self.cookie = ''

    def get(self, url):
        # with allure.step("GET"):  # к методу подключен Allure и можно добавить описание данного запроса
        # Logger.add_request(url, method="GET")
        result = requests.get(url, headers=self.headers, cookies=self.cookie)
        # Logger.add_response(result)
        return result

    def post(self, url, body):
        # with allure.step("POST"):
        # Logger.add_request(url, method="POST")
        result = requests.post(url, json=body, headers=self.headers, cookies=self.cookie)
        # Logger.add_response(result)
        return result

    def put(self, url, body):
        # with allure.step("PUT"):
        # Logger.add_request(url, method="PUT")
        result = requests.put(url, json=body, headers=self.headers, cookies=self.cookie)
        # Logger.add_response(result)
        return result

    def delete(self, url, body):
        # with allure.step("DELETE"):
        # Logger.add_request(url, method="DELETE")
        result = requests.delete(url, json=body, headers=self.headers, cookies=self.cookie)
        # Logger.add_response(result)
        return result

    def patch(self, url, body):
        # with allure.step("PATCH"):
        # Logger.add_request(url, method="PATCH")
        result = requests.patch(url, json=body, headers=self.headers, cookies=self.cookie)
        # Logger.add_response(result)
        return result
