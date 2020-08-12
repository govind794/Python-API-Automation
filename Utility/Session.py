'''
DateTime : 08/07/2020 09:54 AM
Author   : Govind Patidar
File     : Session.py
'''

''' Cookies and header value send in API request '''

import requests

from Utility import Log
from Utility import Config


class Session():
    # define constructor for config and log class
    def __init__(self):
        self.config = Config.Config()
        self.log = Log.Logs

    def get_session(self, env):
        '''
        :param env:
        :return:
        '''

        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            "Content-Type": "application/json"
        }

        if env == "dubeg":
            login_url = 'https://' + self.config.loginHost_release
            param = self.config.loginInfo_release

            session_dubeg = requests.session()
            response = session_dubeg.post(login_url, param, headers=headers)

            print(response.cookies)

            self.log.debug('cookies: %s' % response.cookies.get_dict())
            return response.cookies.get_dict()

        elif env == "release":
            login_url = 'https://' + self.config.loginHost_release
            param = self.config.loginInfo_release

            session_dubeg = requests.session()
            response = session_dubeg.post(login_url, param, headers=headers)

            print(response.cookies)

            self.log.debug('cookies: %s' % response.cookies.get_dict())
            return response.cookies.get_dict()

        else:
            print("get cookies error.")
            self.log.error("Get cookies error, please checkout!!")


if __name__ == '__main__':
    debugSession = Session()
    debugSession.get_session('debug')
