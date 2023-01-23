import time

from data.structures.test_data import *
from userInterFace.Actions.actions import *
from constants import *

def test_6(webdriver):
    webdriver.get(auto_api_url)
    time.sleep(50)