from userInterFace.common import BasePage
from userInterFace.Elements.elements import TextElement, ClickableElement, BasePageElement, HoverableElement, ListElement
from selenium.webdriver.common.by import By

class GetTokenPage(BasePage):
    """A class representing a get token page
    https://s1.lmx.com.pl/gawer/test/"""
    mid_text_element = TextElement(By.XPATH, '/html/body/form/table/tbody/tr[1]/td[2]/input')
    password_text_element = TextElement(By.XPATH, '/html/body/form/table/tbody/tr[2]/td[2]/input')
    orderId_text_element = TextElement(By.XPATH, '/html/body/form/table/tbody/tr[3]/td[2]/input')
    total_text_element = TextElement(By.XPATH,'/html/body/form/table/tbody/tr[4]/td[2]/input')
    currency_text_element = TextElement(By.XPATH,'/html/body/form/table/tbody/tr[5]/td[2]/input')
    get_token_button = ClickableElement(By.XPATH, '/html/body/form/table/tbody/tr[6]/td')

class SendTokenPage(BasePage):
    """A class representing a send token page
        https://s1.lmx.com.pl/gawer/test/payment.php"""
    mid_text_element = TextElement(By.XPATH, '/html/body/form/table/tbody/tr[1]/td[2]/input')
    orderId_text_element = TextElement(By.XPATH, '/html/body/form/table/tbody/tr[2]/td[2]/input')
    token_text_element = TextElement(By.XPATH, '/html/body/form/table/tbody/tr[3]/td[2]/input')
    total_text_element = TextElement(By.XPATH, '/html/body/form/table/tbody/tr[4]/td[2]/input')
    storeType_list_element = ListElement(By.XPATH, '/html/body/form/table/tbody/tr[5]/td[2]/select')
    transType_list_element = ListElement(By.XPATH, '/html/body/form/table/tbody/tr[6]/td[2]/select')
    paymentMethod = ListElement(By.XPATH, '/html/body/form/table/tbody/tr[7]/td[2]/select')
    currency_text_element = TextElement(By.XPATH, '/html/body/form/table/tbody/tr[8]/td[2]/input')
    pay_button = ClickableElement(By.XPATH, '/html/body/form/table/tbody/tr[45]/td/input')


class ChooseMethodPaymentPage(BasePage):
    """A class representing a choose method payment page
        https://testvpos.eservice.com.pl/fim/eservicegate"""
    visa_method_payment_button = ClickableElement(By.XPATH, '//*[@id="main"]/div[2]/div[1]/div[2]/ul/li[1]/a')
    mastercard_method_payment_button = ClickableElement(By.XPATH,'//*[@id="main"]/div[2]/div[1]/div[2]/ul/li[2]/a')
    ipko_method_payment_button = ClickableElement(By.XPATH, '//*[@id="main"]/div[2]/div[5]/div/ul/li[3]/a')
    credit_agricole_method_payment_button = ClickableElement(By.XPATH, '//*[@id="main"]/div[2]/div[2]/div[2]/ul/li[2]/a')
    ca_bank_method_payment_button = ClickableElement(By.XPATH,'//*[@id="main"]/div[2]/div[2]/div[2]/ul/li[3]/a')

class CardDetailsInputPage(BasePage):
    """A class representing a card details input page
            https://testvpos.eservice.com.pl/fim/eservicegate"""
    bin_text_element = TextElement(By.XPATH, '//*[@id="pan"]')
    expire_month_list_element = ListElement(By.XPATH,'/html/body/div/div/div[2]/div[2]/div[1]/div/div/form/div[2]/div/div/div[1]/select')
    expire_year_list_element = ListElement(By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/div/div/form/div[2]/div/div/div[2]/select', True)
    cvv_text_element = TextElement(By.XPATH, '//*[@id="Cvv2Val"]')
    pay_button = ClickableElement(By.XPATH,' //*[@id="btnSbmt"]')


class ResultPage(BasePage):
    """A class representing ok result page
                https://s1.lmx.com.pl/gawer/test/ok.php"""
    order_id = TextElement(By.XPATH, '//*[@id="OrderId"]')
    token = TextElement(By.XPATH,'//*[@id="Token"]')
    payment_method = TextElement(By.XPATH, '//*[@id="PaymentMethod"]')
    # if TextElement(By.XPATH,'//*[@id="TransId"]')!= None:
    #     trans_id = TextElement(By.XPATH,'//*[@id="TransId"]')
    # else:
    #     pass # Is that stupid or no?
    response = TextElement(By.XPATH,'//*[@id="Response"]')
    errMsg_text_element = TextElement(By.XPATH, '//*[@id="ErrMsg"]')

class CreditAgricoleStatusPage(BasePage):
    """A class representing test bank status simulator
                   https://testvpos.eservice.com.pl/testbank/index.php"""
    declined_btn = ClickableElement(By.XPATH,'/html/body/form[1]/input[9]')
    pending_btn = ClickableElement(By.XPATH,'/html/body/form[2]/input[9]')
    approved_btn = ClickableElement(By.XPATH,'/html/body/form[3]/input[9]')

class CCloginPage(BasePage):
    """A class representing CC login page
                       https://testvpos.eservice.com.pl:19446/controlcenter/report/admin.login"""
    acq_uid_text_element = TextElement(By.XPATH, '//*[@id="acqUid"]')
    username_text_element = TextElement(By.XPATH, '//*[@id="loginName"]')
    password_text_element = TextElement(By.XPATH, '//*[@id="userPassword"]')
    log_in_btn = ClickableElement(By.XPATH,'//*[@id="loginForm"]/div/input[2]')

class CCNavBarPage(BasePage):
    """A class representing CC navigation bar
    https://testvpos.eservice.com.pl:19446/controlcenter/report/admin.action"""
    merchant_administration_panel_btn = ClickableElement(By.XPATH, '//*[@id="header"]/div[2]/ul/li[2]/a')
    transaction_report_btn = ClickableElement(By.XPATH,'//*[@id="header"]/div[2]/ul/li[3]/a')
    login_to_merchant_panel = ClickableElement(By.XPATH,'//*[@id="header"]/div[2]/ul/li[1]/a')
    user_managment_btn = ClickableElement(By.XPATH,'//*[@id="header"]/div[2]/ul/li[4]/a')
    content_managment_btn = ClickableElement(By.XPATH,'//*[@id="header"]/div[2]/ul/li[5]/a')
    system_btn = ClickableElement(By.XPATH,'//*[@id="current"]/a')

class CCMerchantAdministrationPanel(BasePage):
    """A class representing CC Merchant Administration Panel
    https://testvpos.eservice.com.pl:19446/controlcenter/report/dim.seek?FPT=Q5JB-RZ5E-D5XK-549E-Q37P-BG55-EACT-7TM8"""
    update_merchant_btn = ClickableElement(By.XPATH,'//*[@id="navigation"]/li[1]/ul/li[3]/a')
    update_merchant_search_text_element = TextElement(By.XPATH,'//*[@id="right"]/div[2]/div[2]/div[2]/form/table/tbody/tr[1]/td[2]/input')
    update_merchant_search_btn = ClickableElement(By.XPATH, '//*[@id="right"]/div[2]/div[2]/div[2]/form/table/tbody/tr[2]/td/input')

class CCUpdateMerchantPage(BasePage):
    """A class representing CC Update Merchant Page
        https://testvpos.eservice.com.pl:19446/controlcenter/report/eservice.merchantDetails"""
    amount_limit_text_element = TextElement(By.XPATH, '//*[@id="amountLimit"]')
    etransfer_limit_text_element = TextElement(By.XPATH,'//*[@id="etransferLimit"]')
    submit_btn = ClickableElement(By.XPATH,'//*[@id="eservice.merchantDetails"]/input[4]')


class BOIPAloginPage(BasePage):
    """A class representing BOIPA IE login page
                       https://testvpos.eservice.com.pl/boipa/report/user.login?language=en&FPT=I0M4-Y03Q-LAJ8-TGZP-954G-LK2Z-Q7H7-S7H1"""
    merchant_id_text_element = TextElement(By.XPATH, '//*[@id="criteria"]')
    username_text_element = TextElement(By.XPATH, '//*[@id="loginName"]')
    password_text_element = TextElement(By.XPATH, '//*[@id="userPassword"]')
    log_in_btn = ClickableElement(By.XPATH,'//*[@id="formLogin"]/div/div/input[1]')

