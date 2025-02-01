import requests
import allure
from data.urls import create_courier_endpoint
from data.urls import login_courier_endpoint
from data.data_create_courier import generation_new_data_courier
from conftest import registered_courier_data
import logging
import json

class TestCreateCourier:

    @allure.title('Создание курьера')
    @allure.step('Проверка создания курьера')
    def test_create_courier(self, registered_courier_data):
        data = generation_new_data_courier()
        data.pop("firstName")
        payload = data
        logging.info(f"Data for courier creation: {data}")
        print(data)

        response = requests.post(create_courier_endpoint, data=payload)
        assert response.status_code == 201
        assert response.json() == {"ok": True}

        login_payload = {
            "login": payload["login"],
            "password": payload["password"]
        }
        login_response = requests.post(login_courier_endpoint, data=login_payload)
        assert login_response.status_code == 200

        courier_id = login_response.json().get("id")
        assert courier_id is not None

        delete_response = requests.delete(f"{create_courier_endpoint}/{courier_id}")
        assert delete_response.status_code == 200


    @allure.title('Проверка невозможности создать курьера. дублирующие логины')
    @allure.description('Проверка, что нельзя создать дублирующего курьера')
    def test_create_courier_duplicate_login(self, registered_courier_data):
        payload = registered_courier_data
        response = requests.post(create_courier_endpoint, data=payload)
        assert response.status_code == 409
        assert response.json().get("message") == "Этот логин уже используется. Попробуйте другой."


    @allure.title('Проверка невозможности создать курьера. Нет обязательных полей')
    @allure.description('Проверка заполнения без обязательных полей. Курьер не создан')
    def test_create_courier_without_password(self):
        data = generation_new_data_courier()
        payload = {
            "login": data["login"],
            "firstName": data["firstName"]
        }
        response = requests.post(create_courier_endpoint, data=payload)

        assert response.status_code == 400
        assert response.json().get("message") == "Недостаточно данных для создания учетной записи"