from userInterFace.Pages.pages import GetTokenPage, SendTokenPage, ChooseMethodPaymentPage, CardDetailsInputPage, \
    ResultPageWithError, CreditAgricoleStatusPage, CCloginPage, CCHomePage, CCMerchantAdministrationPanel, \
    CCUpdateMerchantPage, \
    BOIPAloginPage, SendTokenBOIPAPage, DCCCardDetailsPayPage, ResultPage, PaHomePage, PaOrdersPage, PaTransactionsPage
from data.structures.test_data import GetTokenData, SendTokenData, CardDetailsData, LoginPageData, \
    UpdateSearchMerchantData, UpdateMerchantData, BOIPAloginData
from constants import *
from selenium.webdriver.common.by import By


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
    send_token_page.transType_list_element = send_token_data.trans_type
    send_token_page.storeType_list_element = send_token_data.store_type
    if send_token_data.order_id:
        send_token_page.orderId_text_element = send_token_data.order_id
    else:
        send_token_data.order_id = send_token_page.orderId_text_element.get_attribute('textContent')
    send_token_page.pay_button.click()


def fill_send_token_data_BOIPA(webdriver, send_token_data: SendTokenData):
    send_token_page = SendTokenBOIPAPage(webdriver)
    send_token_page.mid_text_element = send_token_data.mid
    send_token_page.total_text_element = send_token_data.total_amount
    send_token_page.currency_text_element = send_token_data.currency
    send_token_page.paymentMethod = send_token_data.payment_method
    send_token_page.transType_list_element = send_token_data.trans_type
    send_token_page.storeType_list_element = send_token_data.store_type
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


def fill_card_details(webdriver, card_details_data: CardDetailsData):
    card_details_page = CardDetailsInputPage(webdriver)
    card_details_page.bin_text_element = card_details_data.bin
    card_details_page.cvv_text_element = card_details_data.cvv
    card_details_page.expire_month_list_element = card_details_data.expire_month
    card_details_page.expire_year_list_element = card_details_data.expire_year
    card_details_page.pay_button.click()


def DCC_fill_card_details(webdriver, card_details_data: CardDetailsData):
    card_details_page = CardDetailsInputPage(webdriver)
    card_details_page.bin_text_element = card_details_data.bin
    card_details_page.cvv_text_element = card_details_data.cvv
    card_details_page.expire_month_list_element = card_details_data.expire_month
    card_details_page.expire_year_list_element = card_details_data.expire_year


def dcc_select_currency(webdriver, orginal_card_curr=None):
    dcc_select_currency_page = DCCCardDetailsPayPage(webdriver)
    if orginal_card_curr:
        dcc_select_currency_page.card_currency_pay_button.click()
    else:
        dcc_select_currency_page.payment_currency_pay_button.click()


def show_result(webdriver, ass_errMsg=None, ass_response=None, show_result_page_class=ResultPageWithError):
    show_result_page = show_result_page_class(webdriver)
    result_order_id = show_result_page.order_id.get_attribute('value')
    result_token = show_result_page.token.get_attribute('value')
    result_payment_method = show_result_page.payment_method.get_attribute('value')
    result_response = show_result_page.response.get_attribute('value')
    if isinstance(show_result_page, ResultPageWithError) and show_result_page.errMsg_text_element.get_attribute(
            'value'):
        result_errmsg = show_result_page.errMsg_text_element.get_attribute('value')
        if ass_errMsg:
            assert ass_errMsg in result_errmsg
            print(result_errmsg)
    if ass_response:
        assert ass_response in result_response
    return [result_order_id, result_token, result_payment_method, result_response]


def show_order_id(webdriver):
    result_page = ResultPageWithError(webdriver)
    result_order_id = result_page.order_id.get_attribute('value')
    return result_order_id


def select_approved_status_credit_agricole(webdriver):
    select_status_page = CreditAgricoleStatusPage(webdriver)
    select_status_page.approved_btn.click()


def select_declined_status_credit_agricole(webdriver):
    select_status_page = CreditAgricoleStatusPage(webdriver)
    select_status_page.declined_btn.click()


def select_pending_status_credit_agricole(webdriver):
    select_status_page = CreditAgricoleStatusPage(webdriver)
    select_status_page.pending_btn.click()


def log_in_to_CC(webdriver, login_page_data: LoginPageData):
    log_in_page = CCloginPage(webdriver)
    log_in_page.password_text_element = login_page_data.password
    log_in_page.acq_uid_text_element = login_page_data.acq_uid
    log_in_page.username_text_element = login_page_data.username
    log_in_page.log_in_btn.click()


def select_merchant_administration_panel(webdriver):
    navbar_page = CCHomePage(webdriver)
    navbar_page.merchant_administration_panel_btn.click()


def select_report_section(webdriver, merchantId: UpdateSearchMerchantData):
    navbar_page = CCHomePage(webdriver)
    navbar_page.login_to_merchant_panel.click()
    navbar_page.filter_merchant_text_element = merchantId.merchant_id
    navbar_page.login_to_merchant_center_btn.click()
    navbar_page.filter_merchant_result_btn.click()


def select_update_merchant_section(webdriver, merchantId: UpdateSearchMerchantData):
    merchant_administration_bar = CCMerchantAdministrationPanel(webdriver)
    merchant_administration_bar.update_merchant_btn.click()
    merchant_administration_bar.update_merchant_search_text_element = merchantId.merchant_id
    merchant_administration_bar.update_merchant_search_btn.click()


def update_merchant_limits(webdriver, merchant_limits: UpdateMerchantData):
    update_merchant_page = CCUpdateMerchantPage(webdriver)
    update_merchant_page.etransfer_limit_text_element = merchant_limits.etransfer_limit
    update_merchant_page.amount_limit_text_element = merchant_limits.amount_limit
    update_merchant_page.driver.execute_script("arguments[0].scrollIntoView();", update_merchant_page.submit_btn)
    update_merchant_page.submit_btn.click()


def log_in_to_BOIPAIE(webdriver, boipaIE_log_in_data: BOIPAloginData):
    boipaIE_log_in_page = BOIPAloginPage(webdriver)
    boipaIE_log_in_page.merchant_id_text_element = boipaIE_log_in_data.mid
    boipaIE_log_in_page.password_text_element = boipaIE_log_in_data.password
    boipaIE_log_in_page.username_text_element = boipaIE_log_in_data.username
    boipaIE_log_in_page.log_in_btn.click()


def select_PA_home_section(webdriver, section):
    pa_home_page = PaHomePage(webdriver)
    if section == "order":
        pa_home_page.menu_orders_btn.click()
    elif section == "transactions":
        pa_home_page.menu_transactions_btn.click()
    elif section == "MOTO":
        pa_home_page.menu_virtual_terminal_btn.click()


def select_PA_orders_lastweek_all(webdriver):
    pa_orders_page = PaOrdersPage(webdriver)
    pa_orders_page.qa_lastweek_all_btn.click()

def select_PA_transactions_lastweek_all(webdriver):
    pa_trasactions_page = PaTransactionsPage(webdriver)
    pa_trasactions_page.qa_lastweek_btn.click()


def check_order_lists_in_order_section(webdriver, global_order_list, order_list2):
    rows = len(webdriver.find_elements(By.XPATH,
                                       '/ html / body / div[2] / div / div[2] / div[2] / form[1] / table / tbody / tr'))  # count number of rows
    cols = len(webdriver.find_elements(By.XPATH,
                                       '/ html / body / div[2] / div / div[2] / div[2] / form[1] / table / thead / tr / th'))  # count number of columns

    print(rows)
    print(cols)

    # All value from column append to list
    for r in range(1, rows):
        value = webdriver.find_element(By.XPATH,
                                       '/ html / body / div[2] / div / div[2] / div[2] / form[1] / table / tbody / tr[' + str(
                                           r) + ']/td[3] / a').text
        print(value)
        order_list2.append(value)

    check = all(item in order_list2 for item in global_order_list)

    if check is True:
        print("The list {} contains all elements of the list {}".format(order_list2, global_order_list))
    else:
        print("No, List1 doesn't have all elements of the List2.")

    assert check is True


def check_order_lists_in_transaction_section(webdriver, global_order_list, order_list2):
    rows = len(webdriver.find_elements(By.XPATH,
                                       '/html/body/div[2]/div/div[2]/div[2]/table[1]/tbody/tr'))  # count number of rows
    cols = len(webdriver.find_elements(By.XPATH,
                                       '/ html / body / div[2] / div / div[2] / div[2] / table[1] / thead / tr / th'))  # count number of columns

    print(rows)
    print(cols)

    # All value from column append to list
    for r in range(1, rows):
        value = webdriver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/table[1]/tbody/tr[' + str(
            r) + ']/td[4] / a').text
        order_list2.append(value)

    check = all(item in order_list2 for item in global_order_list)

    if check is True:
        print("The list {} contains all elements of the list {}".format(order_list2, global_order_list))
    else:
        print("No, List1 doesn't have all elements of the List2.")

    assert check is True
