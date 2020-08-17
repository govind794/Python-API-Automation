from Resources.Params import LoginFlow
from Utility.Config import Config
from Utility import APIRequest
from Utility import Asserts
from Utility import Log
import pytest

log = Log.Logs()


class TestLoginFlow:

    # @pytest.fixture()
    # def setUp(self, action):
    #     print("---------Test Case Star-----------")
    #     conf = Config()
    #     data = LoginFlow()
    #
    #     test = Asserts.Assertions()
    #     request = APIRequest.APIRequest(action)
    #
    #     host = conf.loginHost_debug
    #     req_url = 'https://' + host
    #     urls = data.url
    #     params = data.data
    #     headers = data.header
    #
    #     auth = params
    #     yield
    #     print("---------Test Case Complete-----------")

    def test_Login(self, action):
        '''
        This test case create for basic login in drivezy
        :param action:
        :return:
        '''

        conf = Config()
        data = LoginFlow()

        test = Asserts.Assertions()
        request = APIRequest.APIRequest(action)

        host = conf.loginHost_debug
        req_url = 'https://' + host
        urls = data.url
        params = data.data
        headers = data.header

        api_url = req_url + urls[0]
        response = request.post_request_method(api_url, params[0], headers[0])

        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'success', 'True')
        assert test.assert_text(response['body']['response']['email'], params[0]['username'])
        assert test.assert_time(response['consuming_time'], 1000)

    def test_LoginCheck(self, action):
        '''
        This test case create for login user after check login success full
        :param action:
        :return:
        '''
        conf = Config()
        data = LoginFlow()

        test = Asserts.Assertions()
        request = APIRequest.APIRequest(action)

        host = conf.loginHost_debug
        req_url = 'https://' + host
        urls = data.url
        params = data.data
        headers = data.header

        api_url = req_url + urls[1]
        response = request.get_request_methods(api_url, params[1], headers[1])

        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'success', 'True')
        assert test.assert_text(response['body']['response']['email'], params[1]['username'])
        assert test.assert_time(response['consuming_time'], 1000)

    def test_Logout(self, action):
        '''
        This test case create for logout user successfully
        :param action:
        :return:
        '''
        conf = Config()
        data = LoginFlow()

        test = Asserts.Assertions()
        request = APIRequest.APIRequest(action)

        host = conf.loginHost_debug
        req_url = 'https://' + host
        urls = data.url
        headers = data.header

        api_url = req_url + urls[2]

        response = request.get_request_methods(api_url, None, headers[2])

        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'success', 'True')
        assert test.assert_text(response['body']['response'], 'Successfully Logged out')
        assert test.assert_time(response['consuming_time'], 1000)
