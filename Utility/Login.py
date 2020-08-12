import json
import requests

from Environment.init import Init
from Environment.bodyParam import *


def api_Response(api):
    url = Init.BaseUrl + '/' + api
    param = login_param()
    # file = open("/Users/govind794/PycharmProjects/PytestAPI/Resources/login_param.json", 'r')
    # json_input = file.read()
    return requests.post(url, json=param)


def api_Response_Body(login_api):
    response = json.loads(login_api.text)
    if response["success"] == True:
        assert response["success"] == True
        return response
    else:
        raise AssertionError("API Response", response)
