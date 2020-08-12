import pytest
import json
import requests
import os

from Environment.api import API
from Environment.init import Init
from Utility.Login import *


@pytest.fixture()
def api_Response():
    url = Init.BaseUrl + '/' + API.loginCheck
    return requests.get(url)


@pytest.fixture()
def api_Response_Body(api_Response):
    response = json.loads(api_Response.text)
    if response["success"] == True:
        assert response["success"] == True
        return response
    else:
        raise AssertionError("API Response", response)


def test_loginCheck(api_Response_Body):
    print('\n ---------Login check test case---------')
    user_details = api_Response_Body["response"]
    id = user_details['id']
    email_id = user_details['email']
    print(f'\n User id: {id} \n Email id: {email_id}')
    getData = open(os.environ['OUTPUT_PATH'], 'r')
    login = getData.read()
    assert login[0] == id
    assert login[1] == email_id
