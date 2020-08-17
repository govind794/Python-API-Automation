from Utility import Log
import json


class Assertions:
    def __init__(self):
        self.log = Log.Logs()

    def assert_code(self, status, expected_code):
        '''
        status code check
        :param status:
        :param expected_code:
        :return:
        '''
        try:
            if status == 200 or status == 201 or status == 202:
                print("\n Test Passed - Successfull " + str(status))
            elif status == 400 or status == 401 or status == 402 or status == 403 or status == 404:
                print("\n Test Failed - client error " + str(status))
            elif status == 500 or status == 501 or status == 502:
                print("\n Test Failed - Server error " + str(status))

            assert status == expected_code
            self.log.info(f"Status code: {status}")

            return True
        except:
            self.log.error(f"statusCode error, expected_code is {expected_code} statusCode is {status}")

    def assert_body(self, body, body_msg, expected_msg):
        '''
        This method use for check assert body response value
        :param body:
        :param body_msg:
        :param expected_msg:
        :return:
        '''
        try:
            msg = body[f"{body_msg}"]
            assert f"{msg}" == f"{expected_msg}"
            self.log.info(f"Success: {msg}")

            return True

        except:
            self.log.error(
                "Response body msg != expected_msg, expected_msg is %s, body_msg is %s" % (expected_msg, body_msg))

    def assert_in_text(self, body, expected_msg):
        '''
        :param body:
        :param expected_msg:
        :return:
        '''
        try:
            text = json.dumps(body, ensure_ascii=False)
            assert expected_msg in text

            return True

        except:
            self.log.error("Response body Does not contain expected_msg, expected_msg is %s" % expected_msg)

    def assert_text(self, body, expected_msg):
        '''
        response body message
        :param body:
        :param expected_msg:
        :return:
        '''
        try:
            assert body == expected_msg
            self.log.info(f"Response body: {body} expected_msg: {expected_msg}")

            return True

        except:
            self.log.error("Response body != expected_msg, expected_msg is %s, body is %s" % (expected_msg, body))

    def assert_time(self, time, expected_time):
        '''
        response time check
        :param time:
        :param expected_time:
        :return:
        '''
        try:
            assert time < expected_time
            self.log.info("Response time < expected_time, expected_time is %s, time is %s" % (expected_time, time))

            return True

        except:
            self.log.error("Response time > expected_time, expected_time is %s, time is %s" % (expected_time, time))
