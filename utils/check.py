import json
from requests import Response

"""Методы для проверки запросов"""


class Check:

    """"Проверка статус кода"""
    @staticmethod  # Обязательная проверка на статус !!
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("Успешно!!! Статус код = " + str(response.status_code))
        else:
            print("ОШИБКА!!! Статус код = " + str(response.status_code))

    """Проверка, что указанное значение присутствует в поле"""
    @staticmethod
    def check_value_in_the_field(response: Response, field_name, expected_word):
        check = response.json()
        check_info = check.get(field_name)
        if check_info is not None and expected_word in str(check_info):
            print('Слово ' + expected_word + ' присутствует в поле!!!')
        else:
            print('Слово ' + expected_word + ' не присутствует в поле!!!')
            return


class GetValue:

    """"Берем значение из указанного поля"""
    @staticmethod
    def get_value_from_field(response: Response, get_field_name):
        check = response.json()
        check_info = check.get(get_field_name)
        return check_info

    """"Берем значение указанного поля из указанного индекса объекта полученного списка"""
    @staticmethod
    def get_value_from_item_of_list(response: Response, field_of_list, index, get_value_from_field):
        response_check = response.json()
        first_index_value_from_list = response_check.get(field_of_list, [])[index]
        get_value_from_field = first_index_value_from_list.get(get_value_from_field)
        return get_value_from_field

