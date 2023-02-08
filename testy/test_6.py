import time
import codecs
import os

from data.structures.test_data import *
from userInterFace.Actions.actions import *
from constants import *

def test_6(webdriver):
    webdriver.get(auto_api_url)
    time.sleep(50)
    completeName = os.path.join("C:\\autoTestyNESTPAY\\Nestpay_pytest\\data", "web-scraping-test6.html")
    file_object = codecs.open(completeName, "w", "utf-8")
    html = webdriver.page_source
    file_object.write(html)