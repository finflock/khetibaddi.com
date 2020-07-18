import requests, base64
import json
from paytmchecksum import PaytmChecksum
from rest_framework.response import Response
from rest_framework import viewsets, filters, status

from .paytm_response_example import Example

MERCHANT_ID = 'YOUR_MERCHANT_ID'
MERCHANT_KEY = 'YOUR_MERCHANT_KEY'
paytm_stage_url = 'https://securegw-stage.paytm.in/theia/api/v1/'
paytm_production_url = 'https://securegw.paytm.in/theia/api/v1/'

paytmParams = dict()


class InitiateTransaction(viewsets.ViewSet):

    def list(self, request):
        get_data = {"Note": "This API will take post method only",
                    "Params": "order_id, cust_id and value as parameters",
                    "Example": {"order_id" : "ORDERID_98765", "cust_id" : "CUST_001", "value" : 1234 },
                    "Response": Example['InitiateTransaction']
                    }
        return Response(get_data, status=status.HTTP_200_OK)

    def create(self, request):
        order_id = str(self.request.GET.get('order_id')) # ORDERID_98765
        cust_id = str(self.request.GET.get('cust_id')) # CUST_001
        value = str(self.request.GET.get('value'))
        paytmParams = dict()

        paytmParams["body"] = {
            "requestType": "Payment",
            "mid": MERCHANT_ID,
            "websiteName": "www.khetibaddi.com",
            "orderId": order_id,
            "callbackUrl": "https://www.khetibaddi.com/callback",
            "txnAmount": {
                "value": value,
                "currency": "INR",
            },
            "userInfo": {
                "custId": cust_id,
            },
        }
        checksum = PaytmChecksum.generateSignature(json.dumps(paytmParams["body"]), MERCHANT_KEY)

        paytmParams["head"] = {
            "signature": checksum
        }

        post_data = json.dumps(paytmParams)
        url = paytm_stage_url + "initiateTransaction?mid={}&orderId={}".format(MERCHANT_ID, order_id)
        response = requests.post(url, data=post_data, headers={"Content-type": "application/json"}).json()

        return Response(response, status=status.HTTP_200_OK)


class UpdateTransaction(viewsets.ViewSet):

    def list(self, request):
        get_data = {"Note": "This API will take post method only",
                    "Params": "order_id, cust_id and value as parameters",
                    "Example": {"order_id" : "ORDERID_98765", "cust_id" : "CUST_001",
                                 "txn_token" : "2f61025f332b444197d8b9d1e509c07e1589794795189", "value" : 1234 },
                    "Response": Example['UpdateTransaction']
                    }
        return Response(get_data, status=status.HTTP_200_OK)

    def create(self, request):
        order_id = str(self.request.GET.get('order_id'))
        cust_id = str(self.request.GET.get('cust_id')) # CUST_001
        txn_token = str(self.request.GET.get('txn_token'))
        value = str(self.request.GET.get('value'))
        paytmParams = dict()

        paytmParams["body"] = {
            "txnAmount": {
                "value": value,
                "currency": "INR",
            },
            "userInfo": {
                "custId": cust_id,
            },
        }
        checksum = PaytmChecksum.generateSignature(json.dumps(paytmParams["body"]), MERCHANT_KEY)

        paytmParams["head"] = {
            "txnToken": txn_token,
            "signature": checksum
        }

        post_data = json.dumps(paytmParams)
        url = paytm_stage_url + "updateTransactionDetail?mid={}&orderId={}".format(MERCHANT_ID, order_id)
        response = requests.post(url, data=post_data, headers={"Content-type": "application/json"}).json()

        return Response(response, status=status.HTTP_200_OK)


class FetchPaymentOptions(viewsets.ViewSet):

    def list(self, request):
        get_data = {"Note": "This API will take post method only",
                    "Params": "order_id, cust_id and value as parameters",
                    "Example": {"order_id" : "ORDERID_98765",
                                 "txn_token" : "2f61025f332b444197d8b9d1e509c07e1589794795189" },
                    "Response": Example['FetchPaymentOptions']
                    }
        return Response(get_data, status=status.HTTP_200_OK)

    def create(self, request):
        order_id = str(self.request.GET.get('order_id'))
        txn_token = str(self.request.GET.get('txn_token'))
        paytmParams = dict()

        paytmParams["head"] = {
            "txnToken": txn_token
        }

        post_data = json.dumps(paytmParams)
        url = paytm_stage_url + "fetchPaymentOptions?mid={}&orderId={}".format(MERCHANT_ID, order_id)
        response = requests.post(url, data=post_data, headers={"Content-type": "application/json"}).json()

        return Response(response, status=status.HTTP_200_OK)


class FetchPCFDetails(viewsets.ViewSet):

    def list(self, request):
        get_data = {"Note": "This API will take post method only",
                    "Params": "order_id, cust_id and value as parameters",
                    "Example": {"order_id" : "ORDERID_98765",
                                 "txn_token" : "2f61025f332b444197d8b9d1e509c07e1589794795189"},
                    "Response": Example['FetchPCFDetails']
                    }
        return Response(get_data, status=status.HTTP_200_OK)

    def create(self, request):
        order_id = str(self.request.GET.get('order_id'))
        txn_token = str(self.request.GET.get('txn_token'))
        paytmParams = dict()

        paytmParams["body"] = {
            "payMethods": [{
                "payMethod": "CREDIT_CARD",
                "instId": "VISA",
            }],
        }

        paytmParams["head"] = {
            "txnToken"	: txn_token
        }

        post_data = json.dumps(paytmParams)
        url = paytm_stage_url + "fetchPcfDetails?mid={}&orderId={}".format(MERCHANT_ID, order_id)
        response = requests.post(url, data=post_data, headers={"Content-type": "application/json"}).json()

        return Response(response, status=status.HTTP_200_OK)


class FetchBinDetails(viewsets.ViewSet):

    def list(self, request):
        get_data = {"Note": "This API will take post method only",
                    "Params": "order_id, cust_id and value as parameters",
                    "Example": {"order_id" : "ORDERID_98765", "cust_id" : "CUST_001",
                                 "txn_token" : "2f61025f332b444197d8b9d1e509c07e1589794795189", "value" : 1234 },
                    "Response": Example['FetchBinDetails']
                    }
        return Response(get_data, status=status.HTTP_200_OK)

    def create(self, request):
        order_id = str(self.request.GET.get('order_id'))
        token = str(self.request.GET.get('token'))
        txn_token = str(self.request.GET.get('txn_token'))
        paytmParams = dict()

        paytmParams["body"] = {
            "bin": "411111"
        }

        paytmParams["head"] = {
            "tokenType": txn_token,
            "token": token
        }

        post_data = json.dumps(paytmParams)
        url = paytm_stage_url + "fetchBinDetail?mid={}&orderId={}".format(MERCHANT_ID, order_id)
        response = requests.post(url, data=post_data, headers={"Content-type": "application/json"}).json()

        return Response(response, status=status.HTTP_200_OK)


class SendOTP(viewsets.ViewSet):

    def list(self, request):
        get_data = {"Note": "This API will take post method only",
                    "Params": "order_id, cust_id and value as parameters",
                    "Example": {"order_id" : "ORDERID_98765", "mobile_number" : "9876543210",
                                 "txn_token" : "2f61025f332b444197d8b9d1e509c07e1589794795189"},
                    "Response": Example['SendOTP']
                    }
        return Response(get_data, status=status.HTTP_200_OK)

    def create(self, request):
        order_id = str(self.request.GET.get('order_id'))
        mobile_number = str(self.request.GET.get('mobile_number'))
        txn_token = str(self.request.GET.get('txn_token'))
        paytmParams = dict()

        paytmParams["body"] = {
            "mobileNumber" : mobile_number
        }

        paytmParams["head"] = {
            "txnToken": txn_token
        }

        post_data = json.dumps(paytmParams)
        url = "https://securegw-stage.paytm.in/login/sendOtp?mid={}&orderId={}".format(MERCHANT_ID, order_id)
        response = requests.post(url, data=post_data, headers={"Content-type": "application/json"}).json()

        return Response(response, status=status.HTTP_200_OK)


class ValidateOTP(viewsets.ViewSet):

    def list(self, request):
        get_data = {"Note": "This API will take post method only",
                    "Params": "order_id, cust_id and value as parameters",
                    "Example": {"order_id" : "ORDERID_98765", "otp" : "987654",
                                 "txn_token" : "2f61025f332b444197d8b9d1e509c07e1589794795189"},
                    "Response": Example['ValidateOTP']
                    }
        return Response(get_data, status=status.HTTP_200_OK)

    def create(self, request):
        order_id = str(self.request.GET.get('order_id'))
        otp = str(self.request.GET.get('otp'))
        txn_token = str(self.request.GET.get('txn_token'))
        paytmParams = dict()

        paytmParams["body"] = {
            "otp" : otp
        }

        paytmParams["head"] = {
            "txnToken": txn_token
        }

        post_data = json.dumps(paytmParams)
        url = "https://securegw-stage.paytm.in/login/validateOtp?mid={}&orderId={}".format(MERCHANT_ID, order_id)
        response = requests.post(url, data=post_data, headers={"Content-type": "application/json"}).json()

        return Response(response, status=status.HTTP_200_OK)


class FetchBalanceInfo(viewsets.ViewSet):

    def list(self, request):
        get_data = {"Note": "This API will take post method only",
                    "Params": "order_id, cust_id and value as parameters",
                    "Example": {"order_id" : "ORDERID_98765",
                                 "txn_token" : "2f61025f332b444197d8b9d1e509c07e1589794795189"},
                    "Response": Example['FetchBalanceInfo']
                    }
        return Response(get_data, status=status.HTTP_200_OK)

    def create(self, request):
        order_id = str(self.request.GET.get('order_id'))
        txn_token = str(self.request.GET.get('txn_token'))
        paytmParams = dict()

        paytmParams["body"] = {
            "paymentMode" : "BALANCE"
        }

        paytmParams["head"] = {
            "txnToken": txn_token
        }

        post_data = json.dumps(paytmParams)
        url = "https://securegw-stage.paytm.in/userAsset/fetchBalanceInfo?mid={}&orderId={}".format(MERCHANT_ID, order_id)
        response = requests.post(url, data=post_data, headers={"Content-type": "application/json"}).json()

        return Response(response, status=status.HTTP_200_OK)


class FetchNBPaymentChannel(viewsets.ViewSet):

    def list(self, request):
        get_data = {"Note": "This API will take post method only",
                    "Params": "order_id, cust_id and value as parameters",
                    "Example": {"order_id" : "ORDERID_98765",
                                 "txn_token" : "2f61025f332b444197d8b9d1e509c07e1589794795189"},
                    "Response": Example['FetchNBPaymentChannel']
                    }
        return Response(get_data, status=status.HTTP_200_OK)

    def create(self, request):
        order_id = str(self.request.GET.get('order_id'))
        txn_token = str(self.request.GET.get('txn_token'))
        paytmParams = dict()

        paytmParams["body"] = {
            "type"     : "MERCHANT"
        }

        paytmParams["head"] = {
            "txnToken": txn_token
        }

        post_data = json.dumps(paytmParams)
        url = paytm_stage_url + "fetchNBPaymentChannels?mid={}&orderId={}".format(MERCHANT_ID, order_id)
        response = requests.post(url, data=post_data, headers={"Content-type": "application/json"}).json()

        return Response(response, status=status.HTTP_200_OK)


class ValidateVPA(viewsets.ViewSet):

    def list(self, request):
        get_data = {"Note": "This API will take post method only",
                    "Params": "order_id, cust_id and value as parameters",
                    "Example": {"order_id" : "ORDERID_98765", "vpa": "7777777777@paytm",
                                 "txn_token" : "2f61025f332b444197d8b9d1e509c07e1589794795189"},
                    "Response": Example['ValidateVPA']
                    }
        return Response(get_data, status=status.HTTP_200_OK)

    def create(self, request):
        order_id = str(self.request.GET.get('order_id'))
        txn_token = str(self.request.GET.get('txn_token'))
        vpa = str(self.request.GET.get('vpa'))
        paytmParams = dict()

        paytmParams["body"] = {
            "vpa"      : vpa
        }

        paytmParams["head"] = {
            "txnToken": txn_token
        }

        post_data = json.dumps(paytmParams)
        url = paytm_stage_url + "vpa/validate?mid={}&orderId={}".format(MERCHANT_ID, order_id)
        response = requests.post(url, data=post_data, headers={"Content-type": "application/json"}).json()

        return Response(response, status=status.HTTP_200_OK)


class ProcessTransaction(viewsets.ViewSet):

    def list(self, request):
        get_data = {"Note": "This API will take post method only",
                    "Params": "order_id, cust_id and value as parameters",
                    "Example": {"order_id" : "ORDERID_98765", "otp": "77777", "paymentMode": "CREDIT CARD",
                                 "txn_token" : "2f61025f332b444197d8b9d1e509c07e1589794795189", "card_info": 411111111111},
                    "Response": Example['ProcessTransaction']
                    }
        return Response(get_data, status=status.HTTP_200_OK)

    def create(self, request):
        order_id = str(self.request.GET.get('order_id'))
        txn_token = str(self.request.GET.get('txn_token'))
        payment_mode = str(self.request.GET.get('payment_mode'))
        card_info = str(self.request.GET.get('card_info'))
        otp = str(self.request.GET.get('otp'))
        paytmParams = dict()

        paytmParams["body"] = {
            "requestType" : "NATIVE",
            "mid"         : MERCHANT_ID,
            "orderId"     : order_id,
            "paymentMode" : payment_mode,
            "cardInfo"    : card_info,
            "authMode"    : otp,
        }

        paytmParams["head"] = {
            "txnToken": txn_token
        }

        post_data = json.dumps(paytmParams)
        url = paytm_stage_url + "processTransaction?mid={}&orderId={}".format(MERCHANT_ID, order_id)
        response = requests.post(url, data=post_data, headers={"Content-type": "application/json"}).json()

        return Response(response, status=status.HTTP_200_OK)


class OauthToken(viewsets.ViewSet):

    def list(self, request):
        get_data = {"Note": "This API will take post method only",
                    "Params": "order_id, cust_id and value as parameters",
                    "Example": {"order_id" : "ORDERID_98765", "otp": "77777", "paymentMode": "CREDIT CARD",
                                 "txn_token" : "2f61025f332b444197d8b9d1e509c07e1589794795189", "card_info": 411111111111},
                    "Response": Example['OauthToken']
                    }
        return Response(get_data, status=status.HTTP_200_OK)

    def create(self, request):
        CLIENT_ID = 'bWVyY2hlBTSXllbkdGWU9Bdm9BYw=='
        CLIENT_SECRET = '999e3877-97c1-XXXX-b19d-6c8787983300'
        post_data = "grant_type=authorization_code&scope=paytm&code=999e3877-97c1-XXXX-b19d-6c8787983300"

        auth = "Basic " + base64.b64encode(CLIENT_ID + ":" + CLIENT_SECRET)
        url = "https://accounts-uat.paytm.com/oauth2/v2/token"
        response = requests.post(url, data = post_data, headers = {"content-type": "application/x-www-form-urlencoded", "Authorization": auth}).json()

        return Response(response, status=status.HTTP_200_OK)


class Refund(viewsets.ViewSet):

    def list(self, request):
        get_data = {"Note": "This API will take post method only",
                    "Params": "order_id, cust_id and value as parameters",
                    "Example": {"order_id" : "ORDERID_98765", "otp": "77777", "paymentMode": "CREDIT CARD",
                                 "txn_token" : "2f61025f332b444197d8b9d1e509c07e1589794795189", "card_info": 411111111111},
                    "Response": Example['Refund']
                    }
        return Response(get_data, status=status.HTTP_200_OK)

    def create(self, request):
        order_id = str(self.request.GET.get('order_id'))
        txn_id = str(self.request.GET.get('txn_id'))
        ref_id = str(self.request.GET.get('ref_id'))
        refund_amount = str(self.request.GET.get('refund_amount'))

        paytmParams = dict()

        paytmParams["body"] = {
            "mid"         : MERCHANT_ID,
            "orderId"     : order_id,
            "refId"       : ref_id
        }
        checksum = PaytmChecksum.generateSignature(json.dumps(paytmParams["body"]), MERCHANT_KEY)

        paytmParams["head"] = {
            "signature": checksum
        }

        post_data = json.dumps(paytmParams)
        url = "https://securegw-stage.paytm.in/v2/refund/status"
        response = requests.post(url, data = post_data, headers = {"Content-type": "application/json"}).json()

        return Response(response, status=status.HTTP_200_OK)


class RefundStatus(viewsets.ViewSet):

    def list(self, request):
        get_data = {"Note": "This API will take post method only",
                    "Params": "order_id, cust_id and value as parameters",
                    "Example": {"order_id" : "ORDERID_98765", "otp": "77777", "paymentMode": "CREDIT CARD",
                                 "txn_token" : "2f61025f332b444197d8b9d1e509c07e1589794795189", "card_info": 411111111111},
                    "Response": Example['RefundStatus']
                    }
        return Response(get_data, status=status.HTTP_200_OK)

    def create(self, request):
        order_id = str(self.request.GET.get('order_id'))
        txn_id = str(self.request.GET.get('txn_id'))
        ref_id = str(self.request.GET.get('ref_id'))
        refund_amount = str(self.request.GET.get('refund_amount'))

        paytmParams = dict()

        paytmParams["body"] = {
            "mid"         : MERCHANT_ID,
            "txnType"     : "REFUND",
            "orderId"     : order_id,
            "txnId"       : txn_id,
            "refId"       : ref_id,
            "refundAmount" : refund_amount
        }
        checksum = PaytmChecksum.generateSignature(json.dumps(paytmParams["body"]), MERCHANT_KEY)

        paytmParams["head"] = {
            "signature": checksum
        }

        post_data = json.dumps(paytmParams)
        url = "https://securegw-stage.paytm.in/refund/apply"
        response = requests.post(url, data = post_data, headers = {"Content-type": "application/json"}).json()

        return Response(response, status=status.HTTP_200_OK)