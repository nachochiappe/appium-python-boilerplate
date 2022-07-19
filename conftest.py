import pytest
import os
import yaml
from appium import webdriver

if os.path.exists(os.path.dirname(__file__) + "/yaml/config.yml"):
    env = os.environ.get('env', 'testing')
    env = env.lower()
    if env in ['testing']:
        CONFIG = yaml.safe_load(open(os.path.dirname(__file__) + "/yaml/config.yml", "r"))[env]
        # TEST_DATA = yaml.safe_load(open(os.path.dirname(__file__) + "/yaml/{}.yml".format(env)))
    else:
        raise("Invalid Environment")
else:
    raise("config.yml does not exist")

platform = (CONFIG['platform'])

@pytest.fixture()
def setup(request):
    desired_caps = {
        "platformName": (CONFIG[platform]['platformName']),
        "platformVersion": (CONFIG[platform]['platformVersion']),
        "deviceName": (CONFIG[platform]['deviceName']),
        "automationName": (CONFIG[platform]['automationName']),
        "app": (CONFIG[platform]['folder']),
    }
    url = 'http://localhost:4723/wd/hub'
    request.instance.driver = webdriver.Remote(url, desired_caps)

    def teardown():
        request.instance.driver.quit()
    request.addfinalizer(teardown)