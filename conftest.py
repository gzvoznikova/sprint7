import pytest
import requests
from data.data_create_courier import register_new_courier_and_return_login_password
from data.urls import create_courier_endpoint
from data.urls import login_courier_endpoint


@pytest.fixture
def registered_courier_data():
    login_pass = register_new_courier_and_return_login_password()
    return {
        "login": login_pass[0],
        "password": login_pass[1],
        "firstName": login_pass[2]
    }

@pytest.fixture
def delete_courier_data():
    login_pass = register_new_courier_and_return_login_password()
    yield {
        "login": login_pass[0],
        "password": login_pass[1]
    }
    response = requests.post(login_courier_endpoint, data=login_pass)
    if response.status_code == 200:
        courier_id = response.json().get("id")
        if courier_id:
            requests.delete(f"{create_courier_endpoint}/{courier_id}")