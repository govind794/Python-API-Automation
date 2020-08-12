'''
DateTime : 06/07/2020 04:20PM
Author   : Govind Patidar
File     : Config.py
'''

import os
from configparser import ConfigParser
from Utility import Log


class Config:
    # Titles:
    TITLE_DEBUG = "privete_debug"
    TITLE_RELEASE = "online_release"
    TITLE_EMAIL = "mail"

    # Values:
    VALUE_TESTER = "tester"
    VALUE_ENVIRONMENT = "environement"
    VELUE_VERSION = "version"
    VALUE_HOST = "host"
    VALUE_LOGIN_HOST = "loginHost"
    VALUE_LOGIN_INFO = "loginInfo"

    # Mail
    VALUE_SMTP_SERVER = "smtpserver"
    VALUE_SENDER = "sender"
    VALUE_RECEIVER = "receiver"
    VALUE_USERNAME = "username"
    VALUE_PASSWORD = "password"

    # Path
    path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

    # Set all file path log, xml report and html report
    def __init__(self):
        self.config = ConfigParser()
        self.logs = Log.Logs()
        self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
        self.xml_report_path = Config.path_dir + 'Report/xml'
        self.html_report_path = Config.path_dir + 'Report/html'

        # File path not found
        if not os.path.exists(self.conf_path):
            raise FileNotFoundError("File not found!")

        # Set all private debug and value for testing
        self.config.read(self.conf_path, encoding='utf-8')
        self.tester_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_TESTER)
        self.environment_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_ENVIRONMENT)
        self.versionCode_debug = self.get_conf(Config.TITLE_DEBUG, Config.VELUE_VERSION)
        self.host_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_HOST)
        self.loginHost_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_LOGIN_HOST)
        self.loginInfo_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_LOGIN_INFO)

        self.tester_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_TESTER)
        self.environment_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_ENVIRONMENT)
        self.versionCode_release = self.get_conf(Config.TITLE_RELEASE, Config.VELUE_VERSION)
        self.host_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_HOST)
        self.loginHost_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_LOGIN_HOST)
        self.loginInfo_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_LOGIN_INFO)

    # Get conf file data
    def get_conf(self, title, value):
        '''
        :param title:
        :param value:
        :return:
        '''
        return self.config.get(title, value)

    # Set conf file data and file open and return write value
    def set_conf(self, title, value, text):
        '''
        :param title:
        :param value:
        :param text:
        :return:
        '''
        self.config.set(title, value, text)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

    def add_conf(self, title):
        '''
        :param title:
        :return:
        '''
        self.config.add_section(title)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)
