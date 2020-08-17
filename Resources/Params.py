'''
DateTime : 15/07/2020 5:53PM
Author   : Positive
File     : Params
'''

import os
from Resources import yaml_read
from Utility import Log

log = Log.Logs()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


def get_paramater(name):
    data = yaml_read.GetAPIParam().get_param()
    param = data[name]

    return param


class LoginFlow:
    log.info('Yaml Path:' + path_dir + '/Resources/Params/login_flow.yml')
    params = get_paramater('Login_Flow')
    print(params)
    url = []
    data = []
    header = []

    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])


class GoogleFlow:
    log.info('Yaml Path:' + path_dir + '/Resources/Params/google_login_flow.yml')
    params = get_paramater('Google_Login_Flow')

    url = []
    data = []
    header = []

    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])


class FacebookFlow:
    log.info('Yaml Path:' + path_dir + '/Resources/Params/facebook_login_flow.yml')
    params = get_paramater('Facebook_Login_Flow')

    url = []
    data = []
    header = []

    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])


class RegularBookingFlow:
    log.info('Yaml Path:' + path_dir + '/Resources/Params/facebook_login_flow.yml')
    params = get_paramater('Regular_Booking_Flow')

    url = []
    data = []
    header = []

    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])
