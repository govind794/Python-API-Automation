# @Author : Govind Patidar

import pytest
import logging
import sys


class TestAPI:

    @pytest.fixture(scope='function')
    def initialize(self):
        def cleanup():
            logging.info("Cleaning Test Date.")

        yield
        cleanup()

    def test_login_users(self):
        test_name = sys._getframe().f_code.co_name

        logging.info("-------Login User Test Case Start::" + test_name + "------")
        # result =

    def test_login_check(self):
        test_name = sys._getframe().f_code.co_name

        logging.info("-------Login Check Test Case Start::" + test_name + "------")

    def test_logout(self):
        test_name = sys._getframe().f_code.co_name

        logging.info("-------Logout Test Case Start::" + test_name + "------")
