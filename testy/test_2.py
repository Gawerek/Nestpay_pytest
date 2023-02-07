import time

from data.structures.test_data import *
from userInterFace.Actions.actions import *
from constants import *

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

