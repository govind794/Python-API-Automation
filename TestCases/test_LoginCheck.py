import pytest
import json
import requests
import os
from requests.auth import HTTPBasicAuth

from Environment.api import API
from Environment.init import Init
from Environment.bodyParam import *
from Utility.Login import *
from Utility.APITest import APITest

os.environ['OUTPUT_PATH'] = '/Users/govind794/PycharmProjects/PytestAPI/Resources/login.txt'

auth = [
    (Init.username, Init.password)
]


@pytest.fixture()
def api_Response():
    url = Init.BaseUrl + '/' + API.login
    # file = open("/Users/govind794/PycharmProjects/PytestAPI/Resources/login_param.json", 'r')
    # json_input = file.read()
    print(login_param())
    return requests.post(url, json=login_param())


@pytest.fixture()
def api_Response_Body(api_Response):
    response = json.loads(api_Response.text)
    if response["success"] == True:
        assert response["success"] == True
        return response
    else:
        raise AssertionError("API Response: ", response)


def test_status_code(api_Response):
    if api_Response.status_code == 200:
        print('status_code of response is:' + str(api_Response.status_code))
        assert 200 == api_Response.status_code
    else:
        raise AssertionError("API response:" + str(api_Response.status_code))


def test_loginByDrivezy(api_Response_Body):
    print('\n ---------Login by email test case---------')
    if api_Response_Body["success"] == True:
        assert api_Response_Body["success"] == True
        response = api_Response_Body["response"]
        id = response['id']
        email_id = response['email']
        print(f"\n User id: {id} \n Email id: {email_id}")
        setData = open(os.environ['OUTPUT_PATH'], 'w')
        setData.write(str({"id": id, "email_id": email_id}) + '\n')
        setData.close()
        assert True
    else:
        raise AssertionError("API Response:", api_Response_Body)


@pytest.mark.parametrize("username, password", auth)
def test_loginCheck(username, password):
    print('\n ---------Login check test case---------')
    url = Init.BaseUrl + '/' + API.loginCheck
    json_response = requests.get(url, auth=HTTPBasicAuth(username, password))
    api_response = json.loads(json_response.text)
    if api_response["success"] == True:
        assert api_response["success"] == True
        response_body = api_response["response"]
        id = response_body['id']
        email_id = response_body['email']
        print(f'\n User id: {id} \n Email id: {email_id}')
        getData = open(os.environ['OUTPUT_PATH'], 'r')
        login = getData.read()
        print(login[2])
        # assert login[0] == id
        # assert login[1] == email_id
    else:
        raise AssertionError("API Response:", api_response)


def test_logout():
    print('\n ---------Logout test case---------')
    url = Init.BaseUrl + '/' + API.logout
    json_response = requests.get(url)
    response = json.loads(json_response.text)
    if response["success"] == True:
        assert response["success"] == True
        assert "Successfully Logged out" == response["response"]
        print(f"\n Response: {response['response']}")
    else:
        raise AssertionError("API Response", response)

