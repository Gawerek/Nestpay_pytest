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
    mastercard_method_payment_button = ClickableElement(By.XPATH, '//*[@id="main"]/div[2]/div[5]/div/ul/li[2]/a')
    ipko_method_payment_button = ClickableElement(By.XPATH, '//*[@id="main"]/div[2]/div[5]/div/ul/li[3]/a')
    credit_agricole_method_payment_button = ClickableElement(By.XPATH, '//*[@id="main"]/div[2]/div[5]/div/ul/li[4]/a')
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
    trans_id = TextElement(By.XPATH,'//*[@id="TransId"]')
    response = TextElement(By.XPATH,'//*[@id="Response"]')




