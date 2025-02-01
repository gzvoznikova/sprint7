import requests
import allure
from data.urls import orders_list_endpoint

class TestGetListOfOrders:
    @allure.title('Получение списка заказов')
    @allure.description('Получение списка заказов')
    def test_get_list_of_orders(self):
        response = requests.get(orders_list_endpoint)
        assert type(response.json()['orders']) == list and 'id' in response.json()['orders'][0]

