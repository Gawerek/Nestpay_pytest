from userInterFace.Pages.pages import GetTokenPage, SendTokenPage, ChooseMethodPaymentPage, CardDetailsInputPage, \
    ResultPage, CreditAgricoleStatusPage, CCloginPage,CCNavBarPage, CCMerchantAdministrationPanel
from data.structures.test1_data import GetTokenData, SendTokenData, CardDetailsData, LoginPageData,UpdateSearchMerchantData
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


def choose_lukas_payment_method(webdriver):
    choose_payment_page = ChooseMethodPaymentPage(webdriver)
    lukas_btn = choose_payment_page.credit_agricole_method_payment_button
    lukas_btn.click()


# def fill_card_details_Visa(webdriver):
#     card_details_page = CardDetailsInputPage(webdriver)
#     card_details_page.bin_text_element = VISA1["BIN"]
#     card_details_page.cvv_text_element = VISA1["CVV"]
#     card_details_page.expire_month_list_element = VISA1["MONTH"]
#     card_details_page.expire_year_list_element = VISA1["YEAR"]
#     card_details_page.pay_button.click()

def fill_card_details(webdriver, card_details_data: CardDetailsData):
    card_details_page = CardDetailsInputPage(webdriver)
    card_details_page.bin_text_element = card_details_data.bin
    card_details_page.cvv_text_element = card_details_data.cvv
    card_details_page.expire_month_list_element = card_details_data.expire_month
    card_details_page.expire_year_list_element = card_details_data.expire_year
    card_details_page.pay_button.click()


# def fill_card_details_MAS(webdriver):
#     card_details_page = CardDetailsInputPage(webdriver)
#     card_details_page.bin_text_element = MAS1["BIN"]
#     card_details_page.cvv_text_element = MAS1["CVV"]
#     card_details_page.expire_month_list_element = MAS1["MONTH"]
#     card_details_page.expire_year_list_element = MAS1["YEAR"]
#     card_details_page.pay_button.click()


def show_result(webdriver):
    show_result_page = ResultPage(webdriver)
    result_order_id = show_result_page.order_id.get_attribute('value')
    result_token = show_result_page.token.get_attribute('value')
    result_payment_method = show_result_page.payment_method.get_attribute('value')
    result_response = show_result_page.response.get_attribute('value')
    # result_trans_id = show_result_page.trans_id.get_attribute('value')
    if show_result_page.trans_id.get_attribute('value'):
        result_trans_id = show_result_page.trans_id.get_attribute('value')
    else:
        pass
    return [result_order_id, result_token, result_payment_method, result_response, result_trans_id]
    # print(result_order_id, end=" order_id ")
    # print(result_token, end=" token ")
    # print(result_payment_method, end=" payment method ")
    # print(result_response, end=" result response ")
    # print(result_trans_id, end=" result transId ")


def select_approved_status_credit_agricole(webdriver):
    select_status_page = CreditAgricoleStatusPage(webdriver)
    select_status_page.approved_btn.click()


def select_declined_status_credit_agricole(webdriver):
    select_status_page = CreditAgricoleStatusPage(webdriver)
    select_status_page.declined_btn.click()


def select_pending_status_credit_agricole(webdriver):
    select_status_page = CreditAgricoleStatusPage(webdriver)
    select_status_page.pending_btn.click()

def log_in_to_CC(webdriver, login_page_data : LoginPageData):
    log_in_page = CCloginPage(webdriver)
    log_in_page.password_text_element = login_page_data.password
    log_in_page.acq_uid_text_element = login_page_data.acq_uid
    log_in_page.username_text_element = login_page_data.username
    log_in_page.log_in_btn.click()

def select_merchant_administration_panel(webdriver):
    navbar_page = CCNavBarPage(webdriver)
    navbar_page.merchant_administration_panel_btn.click()

def select_update_merchant_section(webdriver, merchantId: UpdateSearchMerchantData):
    merchant_administration_bar = CCMerchantAdministrationPanel(webdriver)
    merchant_administration_bar.update_merchant_btn.click()
    merchant_administration_bar.update_merchant_search_text_element = merchantId.merchant_id
    merchant_administration_bar.update_merchant_search_btn.click()




