import time

from data.structures.test_data import *
from userInterFace.Actions.actions import *
from constants import *

def test_11a(webdriver):
    webdriver.get(boipaIE)
    boipaIE_login_data = BOIPAloginData(mid=boipaIE_credentials["mid"], password=boipaIE_credentials["password"], \
                                        username=boipaIE_credentials["username"])
    log_in_to_BOIPAIE(webdriver, boipaIE_login_data)

def test_11b(webdriver):
    webdriver.get(boipaIE)
    boipaUK_login_data = BOIPAloginData(mid=boipaUK_credentials["mid"], password=boipaUK_credentials["password"], \
                                        username=boipaUK_credentials["username"])
    log_in_to_BOIPAIE(webdriver, boipaUK_login_data)