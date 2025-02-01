import requests
import allure
from data.urls import login_courier_endpoint
from data.data_create_courier import register_new_courier_and_return_login_password

class TestLoginCourier:
    @allure.title('Авторизация курьера')
    @allure.description('Проверка получения ID курьера при авторизации с корректным login и password (код - 200 и ID')
    def test_get_courier_id(self, delete_courier_data):
        payload = delete_courier_data
        response = requests.post(login_courier_endpoint, data=payload)

        assert response.status_code == 200
        assert 'id' in response.json()

    @allure.title('Авторизация курьера не пройдена при отправке неверного password')
    @allure.description('Проверка отправки неверного password при автроизации курьера (код - 404 и "message": "Учетная запись не найдена"')
    def test_get_courier_id(self):
        login_pass = register_new_courier_and_return_login_password()
        payload = {
            "login": login_pass[0],
            "password": login_pass[0]
        }
        response = requests.post(login_courier_endpoint, data=payload)

        assert response.status_code == 404
        assert response.json().get("message") == "Учетная запись не найдена"

    @allure.title('Авторизация курьера не пройдена при отправке не всех обязательных полей')
    @allure.description(
        'Проверка авторизации курьера без поля- password')
    def test_login_courier_without_password(self):
        login_pass = register_new_courier_and_return_login_password()
        payload = {
            "login": login_pass[0],
            "password": ""
        }
        response = requests.post(login_courier_endpoint, data=payload)

        assert response.status_code == 400
        assert response.json().get("message") == "Недостаточно данных для входа"