import requests
import allure
import pytest
import json


def test_delete_req_2(create_token, create_booking_id):
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking_id)
    string_booking_id = str(create_booking_id)
    DELETE_URL = base_url + base_path
    print(DELETE_URL)

    cookie = "token=" + create_token

    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }

    response = requests.delete(url=DELETE_URL, headers=headers)
    assert response.status_code == 201
    print(headers)
    print(response.text)

    print(string_booking_id)
    base_url1 = "https://restful-booker.herokuapp.com"
    base_path1 = "/booking/" + string_booking_id
    get_url = base_url1 + base_path1
    print(get_url)
    response = requests.get(url=get_url)
    assert response.status_code == 404
    print(response)
