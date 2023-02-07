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
    webdriver.get(boipaUK)
    boipaUK_login_data = BOIPAloginData(mid=boipaUK_credentials["mid"], password=boipaUK_credentials["password"], \
                                        username=boipaUK_credentials["username"])
    log_in_to_BOIPAIE(webdriver, boipaUK_login_data)

def test_11cvisa(webdriver, token_data_container):
    webdriver.get(boipaIE_pay_url)
    this_token_data = GetTokenData(total_amount='1')
    fill_token_data(webdriver, this_token_data)
    this_send_token_data = SendTokenData(total_amount='1', store_type="3d_pay_hosting")
    fill_send_token_data_BOIPA(webdriver, this_send_token_data)
    choose_visa_payment_method(webdriver)
    credit_card_visa = CardDetailsData(expire_month=VISA1["MONTH"], expire_year=VISA1["YEAR"], cvv=VISA1["CVV"], bin=VISA1["BIN"])
    fill_card_details(webdriver, credit_card_visa)
    token_data_container.extend(show_result(webdriver, ass_response="Approved"))

def test_11cmc(webdriver, token_data_container):
    webdriver.get(boipaIE_pay_url)
    this_token_data = GetTokenData(total_amount='1')
    fill_token_data(webdriver, this_token_data)
    this_send_token_data = SendTokenData(total_amount='1', store_type="3d_pay_hosting")
    fill_send_token_data_BOIPA(webdriver, this_send_token_data)
    choose_mas_payment_method(webdriver)
    credit_card_mc = CardDetailsData(expire_month=MAS1["MONTH"], expire_year=MAS1["YEAR"], cvv=MAS1["CVV"], bin=MAS1["BIN"])
    fill_card_details(webdriver, credit_card_mc)
    token_data_container.extend(show_result(webdriver, ass_response="Approved"))

def test_11dvisa(webdriver, token_data_container):
    webdriver.get(boipaUK_pay_url)
    this_token_data = GetTokenData(total_amount='1')
    fill_token_data(webdriver, this_token_data)
    this_send_token_data = SendTokenData(total_amount='1', store_type="3d_pay_hosting")
    fill_send_token_data_BOIPA(webdriver, this_send_token_data)
    choose_visa_payment_method(webdriver)
    credit_card_visa = CardDetailsData(expire_month=VISA1["MONTH"], expire_year=VISA1["YEAR"], cvv=VISA1["CVV"], bin=VISA1["BIN"])
    fill_card_details(webdriver, credit_card_visa)
    token_data_container.extend(show_result(webdriver, ass_response="Approved"))

def test_11dmc(webdriver, token_data_container):
    webdriver.get(boipaUK_pay_url)
    this_token_data = GetTokenData(total_amount='1')
    fill_token_data(webdriver, this_token_data)
    this_send_token_data = SendTokenData(total_amount='1', store_type="3d_pay_hosting")
    fill_send_token_data_BOIPA(webdriver, this_send_token_data)
    choose_mas_payment_method(webdriver)
    credit_card_mc = CardDetailsData(expire_month=MAS1["MONTH"], expire_year=MAS1["YEAR"], cvv=MAS1["CVV"], bin=MAS1["BIN"])
    fill_card_details(webdriver, credit_card_mc)
    token_data_container.extend(show_result(webdriver, ass_response="Approved"))