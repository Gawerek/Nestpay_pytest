import time

from data.structures.test_data import *
from userInterFace.Actions.actions import *
from constants import *

def test_9a(webdriver, token_data_container):
    webdriver.get(BASE_URL)
    this_token_data = GetTokenData()
    fill_token_data(webdriver, this_token_data)
    this_send_token_data = SendTokenData(store_type='3d_pay_hosting_pm', payment_method='VISA')  # Zmienić w skrypcie wartości dla selecta na string
    fill_send_token_data(webdriver, this_send_token_data)
    credit_card_visa = CardDetailsData(expire_month=VISA1["MONTH"], expire_year=VISA1["YEAR"], cvv=VISA1["CVV"], bin=VISA1["BIN"])
    fill_card_details(webdriver, credit_card_visa)
    token_data_container.extend(show_result(webdriver, ass_response="Approved"))

def test_9b(webdriver, token_data_container):
    webdriver.get(BASE_URL)
    this_token_data = GetTokenData()
    fill_token_data(webdriver, this_token_data)
    this_send_token_data = SendTokenData(store_type="3d_pay_hosting", payment_method='')
    fill_send_token_data(webdriver, this_send_token_data)
    choose_visa_payment_method(webdriver)
    credit_card_visa = CardDetailsData(expire_month=VISA1["MONTH"], expire_year=VISA1["YEAR"], cvv=VISA1["CVV"], bin=VISA1["BIN"])
    fill_card_details(webdriver, credit_card_visa)
    token_data_container.extend(show_result(webdriver, ass_response="Approved"))

def test_9c(webdriver, token_data_container):
    webdriver.get(BASE_URL)
    this_token_data = GetTokenData()
    fill_token_data(webdriver, this_token_data)
    this_send_token_data = SendTokenData(store_type="3d_pm", payment_method='VISA')
    fill_send_token_data(webdriver, this_send_token_data)
    show_result(webdriver, ass_errMsg="Akceptant nie obsługuje tego typu transakcji")

def test_9d(webdriver, token_data_container):
    webdriver.get(BASE_URL)
    this_token_data = GetTokenData()
    fill_token_data(webdriver, this_token_data)
    this_send_token_data = SendTokenData(store_type="3d_pm")
    fill_send_token_data(webdriver, this_send_token_data)
    show_result(webdriver, ass_errMsg="Akceptant nie obsługuje tego typu transakcji")