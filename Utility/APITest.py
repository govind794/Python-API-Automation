import requests

from Environment.init import Init
from Environment.api import API

class APITest:
    url = Init.BaseUrl + '/' + API.loginCheck
    auth_headers = {}

    def __init__(self, api_key=None):
        # Sometimes we don't want to authorize requests
        if api_key:
            self.auth_headers = {'Authorization': api_key}

    def _construct_headers(self, headers):
        # Allows to combine authorization header with per-request custom headers
        if isinstance(headers, dict):
            return {**self.auth_headers, **headers}
        return self.auth_headers

    def get_specific_project(self, headers=None):
        return requests.get(f'{self.url}', headers=self._construct_headers(headers))
