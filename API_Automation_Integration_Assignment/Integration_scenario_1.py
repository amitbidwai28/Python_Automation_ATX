import requests
import allure
import pytest
import json


def test_update_req_1(create_token, create_booking_id):
    print("Token ->", create_token)
    print("Booking ID -> ", create_booking_id)
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking_id)
    PUT_URL = base_url + base_path

    cookie = "token=" + create_token

    # To Do: Calling open function to read json file from resource.json in same directory

    with open('API_Automation_Integration_Assignment/Test_Data/resource.json', 'r') as file_object:
        json_str = json.load(file_object)

    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }

    json_payload = json_str

    # To Do: Saving response into the response object and verify the first name

    response = requests.patch(url=PUT_URL, headers=headers, json=json_payload)
    assert response.status_code == 200
    data = response.json()
    # print(data)
    assert data["firstname"] == "Sameer"
    print("First Integration Scenario has passed")
