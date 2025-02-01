import requests
import allure
import pytest
from data.urls import orders_list_endpoint
from data.data_create_order import generation_new_data_order


class TestCreateOrder:
    @pytest.mark.parametrize('color', [
        ['BLACK'],
        ['GREY'],
        ['BLACK', 'GRAY'],
        []
    ])
    @allure.title('Создание заказа')
    @allure.description('Проверка создания заказа (код - 201 и track в ответе)')
    def test_create_order(self, color):
        data = generation_new_data_order()

        payload = {
            "firstName": data["firstName"],
            "lastName": data["lastName"],
            "address": data["address"],
            "metroStation": data["metroStation"],
            "phone": data["phone"],
            "rentTime": data["rentTime"],
            "deliveryDate": data["deliveryDate"],
            "comment": data["comment"],
            "color": color
        }

        response = requests.post(orders_list_endpoint, json=payload)
        assert response.status_code == 201
        assert 'track' in response.json()
