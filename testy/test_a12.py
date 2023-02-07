import time
from constants import *
import pytest
from time import sleep
from userInterFace.Actions import actions
from data.structures.test_data import GetTokenData, SendTokenData,CardDetailsData, LoginPageData, UpdateSearchMerchantData, UpdateMerchantData
from constants import *


def test_12a(webdriver, token_data_container, order_list):
    webdriver.get(BASE_URL)
    this_token_data = GetTokenData(total_amount='10')
    actions.fill_token_data(webdriver, this_token_data)
    this_send_token_data = SendTokenData(total_amount='10', trans_type="PreAuth")
    actions.fill_send_token_data(webdriver, this_send_token_data)
    actions.choose_visa_payment_method(webdriver)
    credit_card_visa = CardDetailsData(expire_month=VISA1["MONTH"], expire_year=VISA1["YEAR"], cvv=VISA1["CVV"], bin=VISA1["BIN"])
    actions.DCC_fill_card_details(webdriver, credit_card_visa)
    actions.dcc_select_currency(webdriver, orginal_card_curr=True)
    token_data_container.extend(actions.show_result(webdriver, ass_response="Approved"))
    order_list.append(actions.show_order_id(webdriver))

def test_12b(webdriver, token_data_container, order_list):
    webdriver.get(BASE_URL)
    this_token_data = GetTokenData(total_amount='10')
    actions.fill_token_data(webdriver, this_token_data)
    this_send_token_data = SendTokenData(total_amount='10')
    actions.fill_send_token_data(webdriver, this_send_token_data)
    actions.choose_visa_payment_method(webdriver)
    credit_card_visa = CardDetailsData(expire_month=VISA1["MONTH"], expire_year=VISA1["YEAR"], cvv=VISA1["CVV"], bin=VISA1["BIN"])
    actions.DCC_fill_card_details(webdriver, credit_card_visa)
    actions.dcc_select_currency(webdriver, orginal_card_curr=True)
    token_data_container.extend(actions.show_result(webdriver, ass_response="Approved"))
    order_list.append(actions.show_order_id(webdriver))

def test_12c(webdriver, token_data_container, order_list):
    webdriver.get(BASE_URL)
    this_token_data = GetTokenData(total_amount='10')
    actions.fill_token_data(webdriver, this_token_data)
    this_send_token_data = SendTokenData(total_amount='10')
    actions.fill_send_token_data(webdriver, this_send_token_data)
    actions.choose_visa_payment_method(webdriver)
    credit_card_visa = CardDetailsData(expire_month=VISA1["MONTH"], expire_year=VISA1["YEAR"], cvv=VISA1["CVV"], bin=VISA1["BIN"])
    actions.DCC_fill_card_details(webdriver, credit_card_visa)
    actions.dcc_select_currency(webdriver)
    token_data_container.extend(actions.show_result(webdriver, ass_response="Approved"))
    order_list.append(actions.show_order_id(webdriver))



def test_12d(webdriver, token_data_container, order_list):
    webdriver.get(BASE_URL)
    this_token_data = GetTokenData(total_amount='10')
    actions.fill_token_data(webdriver, this_token_data)
    this_send_token_data = SendTokenData(total_amount='10', trans_type="PreAuth")
    actions.fill_send_token_data(webdriver, this_send_token_data)
    actions.choose_mas_payment_method(webdriver)
    credit_card_MAS = CardDetailsData(expire_month=MAS1["MONTH"], expire_year=MAS1["YEAR"], cvv=MAS1["CVV"],
                                      bin=MAS1["BIN"])
    actions.DCC_fill_card_details(webdriver, credit_card_MAS)
    actions.dcc_select_currency(webdriver, orginal_card_curr=True)
    token_data_container.extend(actions.show_result(webdriver, ass_response="Approved"))
    order_list.append(actions.show_order_id(webdriver))

def test_12e(webdriver, token_data_container, order_list):
    webdriver.get(BASE_URL)
    this_token_data = GetTokenData(total_amount='10')
    actions.fill_token_data(webdriver, this_token_data)
    this_send_token_data = SendTokenData(total_amount='10')
    actions.fill_send_token_data(webdriver, this_send_token_data)
    actions.choose_mas_payment_method(webdriver)
    credit_card_MAS = CardDetailsData(expire_month=MAS1["MONTH"], expire_year=MAS1["YEAR"], cvv=MAS1["CVV"],
                                      bin=MAS1["BIN"])
    actions.DCC_fill_card_details(webdriver, credit_card_MAS)
    actions.dcc_select_currency(webdriver, orginal_card_curr=True)
    token_data_container.extend(actions.show_result(webdriver, ass_response="Approved"))
    order_list.append(actions.show_order_id(webdriver))

def test_12e(webdriver, token_data_container, order_list):
    webdriver.get(BASE_URL)
    this_token_data = GetTokenData(total_amount='10')
    actions.fill_token_data(webdriver, this_token_data)
    this_send_token_data = SendTokenData(total_amount='10')
    actions.fill_send_token_data(webdriver, this_send_token_data)
    actions.choose_mas_payment_method(webdriver)
    credit_card_MAS = CardDetailsData(expire_month=MAS1["MONTH"], expire_year=MAS1["YEAR"], cvv=MAS1["CVV"],
                                      bin=MAS1["BIN"])
    actions.DCC_fill_card_details(webdriver, credit_card_MAS)
    actions.dcc_select_currency(webdriver)
    token_data_container.extend(actions.show_result(webdriver, ass_response="Approved"))
    order_list.append(actions.show_order_id(webdriver))