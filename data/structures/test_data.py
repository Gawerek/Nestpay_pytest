from constants import merchant1, merchant_password, POL_currency, default_total_amount, VISA1, MAS1
from userInterFace.Pages.pages import ChooseMethodPaymentPage


class GetTokenData:
    def __init__(self, mid=None, total_amount=None, currency=None, order_id=None, password=None):
        self.mid = mid if mid else merchant1
        self.total_amount = total_amount if total_amount else default_total_amount
        self.currency = currency if currency else POL_currency
        self.order_id = order_id
        self.password = password if password else merchant_password


class SendTokenData:
    def __init__(self, mid=None, total_amount=None, currency=None,
                 order_id=None, payment_method=None, trans_type=None, token=None, store_type = None):
        self.token = token if token else token
        self.mid = mid if mid else merchant1
        self.total_amount = total_amount if total_amount else default_total_amount
        self.currency = currency if currency else POL_currency
        self.order_id = order_id = order_id
        self.payment_method = payment_method if payment_method else ''
        self.trans_type = trans_type if trans_type else 'Auth'
        self.store_type = store_type if store_type else '3d_pay_hosting'


class CardDetailsData:
    def __init__(self, expire_month, bin, expire_year, cvv):
        self.bin = bin
        self.expire_month = expire_month
        self.expire_year = expire_year
        self.cvv = cvv

class LoginPageData:
    def __init__(self, acq_uid, username, password):
        self.acq_uid = acq_uid
        self.username = username
        self.password = password

class UpdateSearchMerchantData:
    def __init__(self, merchant_id):
        self.merchant_id = merchant_id

class UpdateMerchantData:
    def __init__(self, amount_limit=None, etransfer_limit=None):
        self.etransfer_limit = etransfer_limit
        self.amount_limit = amount_limit







