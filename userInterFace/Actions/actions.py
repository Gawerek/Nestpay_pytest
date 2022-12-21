from userInterFace.Pages.pages import GetTokenPage, SendTokenPage, ChooseMethodPaymentPage, CardDetailsInputPage, \
    ResultPage
from data.structures.test1_data import GetTokenData, SendTokenData, CardDetailsDataVisa
from constants import *


def fill_token_data(webdriver, token_generation_data: GetTokenData):
    token_page = GetTokenPage(webdriver)
    token_page.mid_text_element = token_generation_data.mid
    token_page.password_text_element = token_generation_data.password
    token_page.total_text_element = token_generation_data.total_amount
    token_page.currency_text_element = token_generation_data.currency
    if token_generation_data.order_id:
        token_page.orderId_text_element = token_generation_data.order_id
        print(token_page.orderId_text_element)
    else:
        token_generation_data.order_id = token_page.orderId_text_element.get_attribute('textContent')

    token_page.get_token_button.click()


def fill_send_token_data(webdriver, send_token_data: SendTokenData):
    send_token_page = SendTokenPage(webdriver)
    send_token_page.mid_text_element = send_token_data.mid
    send_token_page.total_text_element = send_token_data.total_amount
    send_token_page.currency_text_element = send_token_data.currency
    send_token_page.paymentMethod = send_token_data.payment_method
    send_token_data.trans_type = send_token_page.transType_list_element
    if send_token_data.order_id:
        send_token_page.orderId_text_element = send_token_data.order_id
    else:
        send_token_data.order_id = send_token_page.orderId_text_element.get_attribute('textContent')
    send_token_page.pay_button.click()


def choose_visa_payment_method(webdriver):
    choose_payment_page = ChooseMethodPaymentPage(webdriver)
    visa_btn = choose_payment_page.visa_method_payment_button
    visa_btn.click()


def choose_mas_payment_method(webdriver):
    choose_payment_page = ChooseMethodPaymentPage(webdriver)
    mas_btn = choose_payment_page.mastercard_method_payment_button
    mas_btn.click()


def fill_card_details_Visa(webdriver):
    card_details_page = CardDetailsInputPage(webdriver)
    card_details_page.bin_text_element = VISA1["BIN"]
    card_details_page.cvv_text_element = VISA1["CVV"]
    card_details_page.expire_month_list_element = VISA1["MONTH"]
    card_details_page.expire_year_list_element = VISA1["YEAR"]
    card_details_page.pay_button.click()

def fill_card_details_MAS(webdriver):
    card_details_page = CardDetailsInputPage(webdriver)
    card_details_page.bin_text_element = MAS1["BIN"]
    card_details_page.cvv_text_element = MAS1["CVV"]
    card_details_page.expire_month_list_element = MAS1["MONTH"]
    card_details_page.expire_year_list_element = MAS1["YEAR"]
    card_details_page.pay_button.click()


def show_result(webdriver):
    show_result_page = ResultPage(webdriver)
    result_order_id = show_result_page.order_id.get_attribute('value')
    result_token = show_result_page.token.get_attribute('value')
    result_payment_method = show_result_page.payment_method.get_attribute('value')
    result_response = show_result_page.response.get_attribute('value')
    result_trans_id = show_result_page.trans_id.get_attribute('value')
    print(result_order_id, end=" order_id ")
    print(result_token, end=" token ")
    print(result_payment_method, end=" payment method ")
    print(result_response, end=" result response ")
    print(result_trans_id, end=" result transId ")
