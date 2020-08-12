import requests
import pytest
import json


@pytest.fixture()
def api_Response():
    url = "https://feature3.drivezytest.com/city?includes=venue"
    return requests.get(url)


def test_get_city_check_status_code_equals_200(api_Response):
    response = api_Response
    assert response.status_code == 200


def test_get_city_check_content_type_equals_json(api_Response):
    response = api_Response
    assert response.headers['Content-Type'] == "application/json"


def test_get_city_check_success_equals_true(api_Response):
    response = api_Response
    response_body = response.json()
    assert response_body["success"] == True


def test_get_city_check_city_name(api_Response):
    response = api_Response
    response_body = json.loads(response.text)["response"]
    for i in range(len(response_body)):
        if response_body[i]["name"] == "Bengaluru":
            print("city_id =", response_body[i]["id"])
            print("city_name =", response_body[i]["name"])
            assert response_body[i]["name"] == "Bengaluru"


def test_get_city_check_city_venue(api_Response):
    response = api_Response
    response_body = json.loads(response.text)["response"]
    venue = response_body[1]["venue"]
    for i in range(len(venue)):
        if venue[i]["name"] == "Mahadevapura":
            assert venue[i]["name"] == "Mahadevapura"
