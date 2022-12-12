from userInterFace.common import BasePage
from userInterFace.Elements.elements import TextElement, ClickableElement, BasePageElement, HoverableElement, ListElement
from selenium.webdriver.common.by import By

class GetTokenPage(BasePage):
    """A class representing a get token page
    https://s1.lmx.com.pl/gawer/test/"""
    mid_text_element = TextElement(By.XPATH, '/html/body/form/table/tbody/tr[1]/td[2]')
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
    storeType_list_element = ListElement(By.XPATH, '/html/body/form/table/tbody/tr[4]/td[2]/input')
    transType_list_element = ListElement(By.XPATH, '/html/body/form/table/tbody/tr[6]/td[2]/select')
    paymentMethod = ListElement(By.XPATH, '/html/body/form/table/tbody/tr[7]/td[2]/select')
    currency_text_element = TextElement(By.XPATH, '/html/body/form/table/tbody/tr[8]/td[2]/input')
    pay_button = ClickableElement(By.XPATH, '/html/body/form/table/tbody/tr[45]/td/input')


class ChooseMethodPaymentPage(BasePage):
    """A class representing a choose method payment page
        https://testvpos.eservice.com.pl/fim/eservicegate"""
    visa_method_payment_button = ClickableElement(By.XPATH, '//*[@id="main"]/div[2]/div[5]/div/ul/li[1]/a/i')
    mastercard_method_payment_button = ClickableElement(By.XPATH, '//*[@id="main"]/div[2]/div[5]/div/ul/li[2]/a/i')
    ipko_method_payment_button = ClickableElement(By.XPATH, '//*[@id="main"]/div[2]/div[5]/div/ul/li[3]/a/i')
    credit_agricole_method_payment_button = ClickableElement(By.XPATH, '//*[@id="main"]/div[2]/div[5]/div/ul/li[4]/a/i')
    ca_bank_method_payment_button = ClickableElement(By.XPATH,'//*[@id="main"]/div[2]/div[2]/div[2]/ul/li[3]/a/i')

class VisaCardDetailsPage(BasePage):
    """A class representing a VISA card details input page
            https://testvpos.eservice.com.pl/fim/eservicegate"""
    bin_text_element = TextElement(By.XPATH, '//*[@id="pan"]')
    expire_month_list_element = ListElement(By.XPATH,'//*[@id="ExpiresMonth"]')
    expire_year_list_element = ListElement(By.XPATH, '// *[ @ id = "ExpiresYear"]')
    cvv_text_element = TextElement(By.XPATH,'//*[@id="Cvv2Val"]')
    pay_button = ClickableElement(By.XPATH,'//*[@id="btnSbmt"]')
