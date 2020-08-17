import allure
import pytest

from Utility.Config import Config


@pytest.fixture()
def action():
    conf = Config()
    env = conf.environment_debug
    host = conf.host_debug
    tester = conf.tester_debug
    # allure.environment(environment=env)
    # allure.environment(hostname=host)
    # allure.environment(tester=tester)
    return env
