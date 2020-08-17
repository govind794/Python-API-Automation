'''
DateTime : 08/07/2020 09:54AM
Author   : Govind Patidar
File     : APIRequest.py
'''

import requests
from requests.auth import HTTPBasicAuth

from Utility import Session
from Utility import Log


class APIRequest:

    def __init__(self, env):
        '''
        :param env:
        '''
        self.session = Session.Session()
        self.get_session = self.session.get_session(env)
        self.log = Log.Logs()

    def get_request_methods(self, url, data, header):
        '''
        :param url:
        :param data:
        :param header:
        :return:
        '''
        if not url.startswith('https://'):
            url = f"https:// {url}"
            print(url)

        try:
            if data is None:
                response = requests.get(url=url, headers=header, cookies=self.get_session)
            else:
                response = requests.get(url=url, auth=HTTPBasicAuth(data['username'], data['password']), headers=header,
                                        cookies=self.get_session)

        except requests.RequestException as e:
            print(f"RequestException url: {url}")
            print(e)
            return ()

        except Exception as e:
            print(f"Exception url: {url}")
            print(e)
            return ()

        consuming_time = response.elapsed.microseconds / 1000
        total_time = response.elapsed.total_seconds()

        self.log.info(f"Response consuming time: {consuming_time}")
        self.log.info(f"Response total time: {total_time}")

        response_dicts = {}
        response_dicts['code'] = response.status_code

        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''

        response_dicts['consuming_time'] = consuming_time
        response_dicts['total_time'] = total_time

        return response_dicts

    def post_request_method(self, url, data, header):
        '''
        This method use for post api request
        :param url:
        :param data:
        :param header:
        :return:
        '''
        if not url.startswith('https://'):
            url = f"https:// {url}"
            print(url)

        try:
            if data is None:
                response = requests.post(url=url, headers=header, cookies=self.get_session)
            else:
                response = requests.post(url=url, json=data, headers=header, cookies=self.get_session)

        except requests.RequestException as e:
            print(f"RequestException url: {url}")
            print(e)
            return ()

        except Exception as e:
            print(f"Exception url: {url}")
            print(e)
            return ()

        consuming_time = response.elapsed.microseconds / 1000
        total_time = response.elapsed.total_seconds()

        self.log.info(f"Response consuming time: {consuming_time}")
        self.log.info(f"Response total time: {total_time}")

        response_dicts = {}
        response_dicts['code'] = response.status_code

        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''

        response_dicts['consuming_time'] = consuming_time
        response_dicts['total_time'] = total_time

        return response_dicts
