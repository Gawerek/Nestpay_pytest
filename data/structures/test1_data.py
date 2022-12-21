from constants import merchant1, merchant_password, POL_currency, default_total_amount, VISA1, MAS1
from userInterFace.Pages.pages import ChooseMethodPaymentPage


class GetTokenData:
    def __init__(self, mid=None, total_amount=None, currency=None, order_id=None, password=None):
        self.mid = mid if mid else merchant1
        self.total_amount = total_amount if total_amount else default_total_amount
        self.currency = currency if currency else POL_currency
        self.order_id = order_id = order_id
        self.password = password if password else merchant_password


class SendTokenData:
    def __init__(self, mid=None, total_amount=None, currency=None,
                 order_id=None, payment_method=None, trans_type=None, token=None):
        self.token = token if token else token
        self.mid = mid if mid else merchant1
        self.total_amount = total_amount if total_amount else default_total_amount
        self.currency = currency if currency else POL_currency
        self.order_id = order_id = order_id
        self.payment_method = payment_method if payment_method else ''
        self.trans_type = trans_type if trans_type else 'Auth'


class CardDetailsDataVisa:
    def __int__(self, expire_month=VISA1["MONTH"], number=VISA1["BIN"], expire_year=VISA1["YEAR"], cvv=VISA1["CVV"]):
        self.number = number
        self.expire_month = expire_month
        self.expire_year = expire_year
        self.cvv = cvv



