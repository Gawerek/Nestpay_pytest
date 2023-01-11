import time

from data.structures.test_data import *
from userInterFace.Actions.actions import *
from constants import *

def test_7a(webdriver, token_data_container):
    webdriver.get(BASE_URL)
    this_token_data = GetTokenData(total_amount='1', currency=EUR_currency)
    fill_token_data(webdriver, this_token_data)
    this_send_token_data = SendTokenData(total_amount='1', currency=POL_currency)
    fill_send_token_data(webdriver, this_send_token_data)
    print(show_result(webdriver, "Złe dane autentykujące akceptanta"))

def test_7b(webdriver, token_data_container):
    webdriver.get(BASE_URL)
    this_token_data = GetTokenData(total_amount='10', currency=POL_currency)
    fill_token_data(webdriver, this_token_data)
    this_send_token_data = SendTokenData(total_amount='1', currency=POL_currency)
    fill_send_token_data(webdriver, this_send_token_data)
    print(show_result(webdriver, "Złe dane autentykujące akceptanta"))

def test_7c(webdriver, token_data_container):
    webdriver.get(BASE_URL)
    this_token_data = GetTokenData(total_amount='1', order_id='Order123')
    fill_token_data(webdriver, this_token_data)
    this_send_token_data = SendTokenData(total_amount='1', order_id='Order1239548712')
    fill_send_token_data(webdriver, this_send_token_data)
    print(show_result(webdriver, "Złe dane autentykujące akceptanta"))

def test_7d(webdriver, token_data_container):
    webdriver.get(BASE_URL)
    this_token_data = GetTokenData(total_amount='1000', currency=EUR_currency, mid=merchant1)
    fill_token_data(webdriver, this_token_data)
    this_send_token_data = SendTokenData(total_amount='1000', currency=EUR_currency, mid=merchant2)
    fill_send_token_data(webdriver, this_send_token_data)
    print(show_result(webdriver, "Złe dane autentykujące akceptanta"))





