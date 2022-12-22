import time

import pytest

from time import sleep
from userInterFace.Actions import actions
from data.structures.test1_data import GetTokenData, SendTokenData,CardDetailsData
from constants import *
# @pytest.mark.parametrize("token_data", [
#     GetTokenData(total_amount='10'),
#     GetTokenData(),
#     GetTokenData(currency='987')
# ])
# def test_1a(webdriver, token_data_container, token_data):

def test_1a(webdriver, token_data_container):
    webdriver.get("https://s1.lmx.com.pl/gawer/test/")
    this_token_data = GetTokenData(total_amount='10')
    # token_data_container.append(this_token_data)
    actions.fill_token_data(webdriver, this_token_data)
    this_send_token_data = SendTokenData(total_amount='10')
    actions.fill_send_token_data(webdriver, this_send_token_data)
    actions.choose_visa_payment_method(webdriver)
    credit_card_visa = CardDetailsData(expire_month=VISA1["MONTH"], expire_year=VISA1["YEAR"], cvv=VISA1["CVV"], bin=VISA1["BIN"])
    actions.fill_card_details(webdriver, credit_card_visa)
    token_data_container.extend(actions.show_result(webdriver))
    # token_data_container = {**token_data_container, **actions.show_result(webdriver)}


def test_1b(webdriver, token_data_container):
    webdriver.get("https://s1.lmx.com.pl/gawer/test/")
    this_token_data = GetTokenData(total_amount='1')
    # token_data_container.append(this_token_data)
    actions.fill_token_data(webdriver, this_token_data)
    this_send_token_data = SendTokenData(total_amount='1')
    actions.fill_send_token_data(webdriver, this_send_token_data)
    actions.choose_mas_payment_method(webdriver)
    credit_card_MAS = CardDetailsData(expire_month=MAS1["MONTH"], expire_year=MAS1["YEAR"], cvv=MAS1["CVV"], bin=MAS1["BIN"])
    actions.fill_card_details(webdriver, credit_card_MAS)
    token_data_container.extend(actions.show_result(webdriver))

def test_1c(webdriver, token_data_container):
    webdriver.get("https://s1.lmx.com.pl/gawer/test/")
    this_token_data = GetTokenData(total_amount='1', currency=EUR_currency)
    actions.fill_token_data(webdriver, this_token_data)
    this_send_token_data = SendTokenData(total_amount='1', currency=EUR_currency)
    actions.fill_send_token_data(webdriver, this_send_token_data)
    actions.choose_visa_payment_method(webdriver)
    credit_card_visa = CardDetailsData(expire_month=VISA1["MONTH"], expire_year=VISA1["YEAR"], cvv=VISA1["CVV"], bin=VISA1["BIN"])
    actions.fill_card_details(webdriver, credit_card_visa)
    token_data_container.extend(actions.show_result(webdriver))

def test_1d(webdriver, token_data_container):
    webdriver.get("https://s1.lmx.com.pl/gawer/test/")
    this_token_data = GetTokenData(total_amount='1', currency=EUR_currency)
    actions.fill_token_data(webdriver, this_token_data)
    this_send_token_data = SendTokenData(total_amount='1', currency=EUR_currency)
    actions.fill_send_token_data(webdriver, this_send_token_data)
    actions.choose_mas_payment_method(webdriver)
    credit_card_MAS = CardDetailsData(expire_month=MAS1["MONTH"], expire_year=MAS1["YEAR"], cvv=MAS1["CVV"], bin=MAS1["BIN"])
    actions.fill_card_details(webdriver, credit_card_MAS)
    token_data_container.extend(actions.show_result(webdriver))

def test_1e(webdriver, token_data_container):
    webdriver.get("https://s1.lmx.com.pl/gawer/test/")
    this_token_data = GetTokenData(total_amount='10')
    # token_data_container.append(this_token_data)
    actions.fill_token_data(webdriver, this_token_data)
    this_send_token_data = SendTokenData(total_amount='10', trans_type="Auth")
    actions.fill_send_token_data(webdriver, this_send_token_data)
    actions.choose_visa_payment_method(webdriver)
    credit_card_visa = CardDetailsData(expire_month=VISA1["MONTH"], expire_year=VISA1["YEAR"], cvv=VISA1["CVV"], bin=VISA1["BIN"])
    actions.fill_card_details(webdriver, credit_card_visa)
    token_data_container.extend(actions.show_result(webdriver))

def test_1f(webdriver, token_data_container):
    webdriver.get("https://s1.lmx.com.pl/gawer/test/")
    this_token_data = GetTokenData(total_amount='1')
    actions.fill_token_data(webdriver, this_token_data)
    this_send_token_data = SendTokenData(total_amount='1', trans_type="Auth")
    actions.fill_send_token_data(webdriver, this_send_token_data)
    actions.choose_mas_payment_method(webdriver)
    credit_card_MAS = CardDetailsData(expire_month=MAS1["MONTH"], expire_year=MAS1["YEAR"], cvv=MAS1["CVV"], bin=MAS1["BIN"])
    actions.fill_card_details(webdriver, credit_card_MAS)
    token_data_container.extend(actions.show_result(webdriver))

def test_1g(webdriver, token_data_container):
    webdriver.get("https://s1.lmx.com.pl/gawer/test/")
    this_token_data = GetTokenData(total_amount='1', currency=EUR_currency)
    actions.fill_token_data(webdriver, this_token_data)
    this_send_token_data = SendTokenData(total_amount='1', currency=EUR_currency, trans_type="Auth")
    actions.fill_send_token_data(webdriver, this_send_token_data)
    actions.choose_visa_payment_method(webdriver)
    credit_card_visa = CardDetailsData(expire_month=VISA1["MONTH"], expire_year=VISA1["YEAR"], cvv=VISA1["CVV"], bin=VISA1["BIN"])
    actions.fill_card_details(webdriver, credit_card_visa)
    token_data_container.extend(actions.show_result(webdriver))

# def test_1j(webdriver, token_data_container):
#     webdriver.get("https://s1.lmx.com.pl/gawer/test/")
#     this_token_data = GetTokenData(total_amount='1')
#     actions.fill_token_data(webdriver, this_token_data)
#     this_send_token_data = SendTokenData(total_amount='1')
#     actions.fill_send_token_data(webdriver, this_send_token_data)
#     actions.choose_lukas_payment_method(webdriver)
#     print("")

