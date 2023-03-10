import time

from data.structures.test_data import *
from userInterFace.Actions.actions import *
from constants import *

def test_2a(webdriver, order_list):
    webdriver.get(CC_URL)
    this_login_data = LoginPageData(acq_uid=CC_acqUid, username=CC_loginName, password=CC_password)
    log_in_to_CC(webdriver, this_login_data)
    this_merchant_id_value = UpdateSearchMerchantData(merchant_id=merchant1)
    select_report_section(webdriver, this_merchant_id_value)
    webdriver.switch_to.window(webdriver.window_handles[-1])
    select_PA_home_section(webdriver, section="transactions")
    select_PA_transactions_lastweek_all(webdriver)
    check_order_lists_in_transaction_section(webdriver, global_order_list=order_list, order_list2=orderlist2)

def test_2b(webdriver, order_list):
    webdriver.get(CC_URL)
    this_login_data = LoginPageData(acq_uid=CC_acqUid, username=CC_loginName, password=CC_password)
    log_in_to_CC(webdriver, this_login_data)
    this_merchant_id_value = UpdateSearchMerchantData(merchant_id=merchant1)
    select_report_section(webdriver, this_merchant_id_value)
    webdriver.switch_to.window(webdriver.window_handles[-1])
    select_PA_home_section(webdriver,section="order")
    select_PA_orders_lastweek_all(webdriver)
    check_order_lists_in_order_section(webdriver, global_order_list=order_list, order_list2=orderlist2)

def test_2c(webdriver, order_list):
    webdriver.get(CC_URL)
    this_login_data = LoginPageData(acq_uid=CC_acqUid, username=CC_loginName, password=CC_password)
    log_in_to_CC(webdriver, this_login_data)
    this_merchant_id_value = UpdateSearchMerchantData(merchant_id=merchant1)
    select_merchant_administration_panel(webdriver)
    search_merchant_administration_panel(webdriver, this_merchant_id_value)
    webdriver.switch_to.window(webdriver.window_handles[-1])
    select_PA_home_section(webdriver, section="transactions")
    select_PA_transactions_lastweek_all(webdriver)
    check_order_lists_in_transaction_section(webdriver, global_order_list=order_list, order_list2=orderlist2)


def test_2d(webdriver, order_list):
    webdriver.get(CC_URL)
    this_login_data = LoginPageData(acq_uid=CC_acqUid, username=CC_loginName, password=CC_password)
    log_in_to_CC(webdriver, this_login_data)
    this_merchant_id_value = UpdateSearchMerchantData(merchant_id=merchant1)
    select_merchant_administration_panel(webdriver)
    search_merchant_administration_panel(webdriver, this_merchant_id_value)
    webdriver.switch_to.window(webdriver.window_handles[-1])
    select_PA_home_section(webdriver, section="transactions")
    select_PA_transactions_lastweek_all(webdriver)
    check_order_lists_in_order_section(webdriver, global_order_list=order_list, order_list2=orderlist2)
