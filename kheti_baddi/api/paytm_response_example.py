Example = {
    "InitiateTransaction":
        {
            "head": {
                "responseTimestamp": "1526969112101",
                "version": "v1",
                "clientId": "C11",
                "signature": "TXBw50YPUKIgJd8gR8RpZuOMZ+csvCT7i0/YXmG//J8+BpFdY5goPBiLAkCzKlCkOvAQip/Op5aD6Vs+cNUTjFmC55JBxvp7WunZ45Ke2q0="
            },
            "body": {
                "resultInfo": {
                    "resultStatus": "S",
                    "resultCode": "0000",
                    "resultMsg": "Success"
                },
                "txnToken": "fe795335ed3049c78a57271075f2199e1526969112097",
                "isPromoCodeValid": 'false',
                "authenticated": 'false'
            }
        },
    "UpdateTransaction":
        {
            "head": {
                "responseTimestamp": "xxxxxxxxxxxxx",
                "version": "v1",
                "clientId": "C11",
                "signature": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
            },
            "body": {
                "resultInfo": {
                    "resultStatus": "S",
                    "resultCode": "0000",
                    "resultMsg": "Success"
                }
            }
        },
    "FetchPaymentOptions":
        {
            "head": {
                "requestId": 'null',
                "responseTimestamp": "1573044458274",
                "version": "v1"
            },
            "body": {
                "resultInfo": {
                    "resultStatus": "S",
                    "resultCode": "0000",
                    "resultMsg": "Success"
                },
                "walletOnly": 'false',
                "zeroCostEmi": 'false',
                "pcfEnabled": 'false',
                "nativeJsonRequestSupported": 'false',
                "activeMerchant": 'true',
                "oneClickMaxAmount": "2000",
                "onTheFlyKYCRequired": 'false',
                "paymentFlow": "NONE",
                "merchantPayOption": {
                    "paymentModes": [{
                        "displayName": "Paytm Balance",
                        "isDisabled": {
                            "status": "false",
                            "msg": 'null',
                            "userAccountExist": "true",
                            "merchantAccept": "true"
                        },
                        "payChannelOptions": [{
                            "isDisabled": {
                                "status": "false",
                                "msg": 'null',
                                "userAccountExist": "true",
                                "merchantAccept": "true"
                            },
                            "hasLowSuccess": {
                                "status": "false",
                                "msg": ""
                            },
                            "iconUrl": 'null',
                            "balanceInfo": {
                                "subWalletDetails": 'null',
                                "payerAccountExists": 'true',
                                "accountBalance": {
                                    "currency": "INR",
                                    "value": "1089.00"
                                }
                            },
                            "isHybridDisabled": 'false'
                        }],
                        "feeAmount": 'null',
                        "taxAmount": 'null',
                        "totalTransactionAmount": 'null',
                        "priority": 'null',
                        "onboarding": 'false',
                        "paymentMode": "BALANCE",
                        "isHybridDisabled": 'false'
                    }, {
                        "displayName": "Debit Card",
                        "isDisabled": {
                            "status": "false",
                            "msg": ""
                        },
                        "payChannelOptions": [],
                        "feeAmount": 'null',
                        "taxAmount": 'null',
                        "totalTransactionAmount": 'null',
                        "priority": 'null',
                        "onboarding": 'false',
                        "paymentMode": "DEBIT_CARD",
                        "isHybridDisabled": 'false'
                    }, {
                        "displayName": "Credit Card",
                        "isDisabled": {
                            "status": "false",
                            "msg": ""
                        },
                        "payChannelOptions": [],
                        "feeAmount": 'null',
                        "taxAmount": 'null',
                        "totalTransactionAmount": 'null',
                        "priority": 'null',
                        "onboarding": 'false',
                        "paymentMode": "CREDIT_CARD",
                        "isHybridDisabled": 'false'
                    }, {
                        "displayName": "BANK_MANDATE",
                        "isDisabled": {
                            "status": "false",
                            "msg": ""
                        },
                        "payChannelOptions": [{
                            "isDisabled": {
                                "status": "false",
                                "msg": ""
                            },
                            "hasLowSuccess": {
                                "status": "false",
                                "msg": ""
                            },
                            "iconUrl": 'null',
                            "mandateMode": "E_MANDATE",
                            "mandateAuthMode": ["NET_BANKING"],
                            "mandateBankCode": 'null',
                            "isHybridDisabled": 'false',
                            "channelCode": "AXIS",
                            "channelName": "AXIS"
                        }, {
                            "isDisabled": {
                                "status": "false",
                                "msg": ""
                            },
                            "hasLowSuccess": {
                                "status": "false",
                                "msg": ""
                            },
                            "iconUrl": 'null',
                            "mandateMode": "E_MANDATE",
                            "mandateAuthMode": ["DEBIT_CARD", "NET_BANKING"],
                            "mandateBankCode": 'null',
                            "isHybridDisabled": 'false',
                            "channelCode": "HDFC",
                            "channelName": "HDFC"
                        }, {
                            "isDisabled": {
                                "status": "false",
                                "msg": ""
                            },
                            "hasLowSuccess": {
                                "status": "false",
                                "msg": ""
                            },
                            "iconUrl": 'null',
                            "mandateMode": "PAPER_MANDATE",
                            "mandateAuthMode": 'null',
                            "mandateBankCode": 'null',
                            "isHybridDisabled": 'false',
                            "channelCode": "ALH",
                            "channelName": "ALH"
                        }, {
                            "isDisabled": {
                                "status": "false",
                                "msg": ""
                            },
                            "hasLowSuccess": {
                                "status": "false",
                                "msg": ""
                            },
                            "iconUrl": 'null',
                            "mandateMode": "PAPER_MANDATE",
                            "mandateAuthMode": 'null',
                            "mandateBankCode": 'null',
                            "isHybridDisabled": 'false',
                            "channelCode": "BBK",
                            "channelName": "BBK"
                        }],
                        "feeAmount": 'null',
                        "taxAmount": 'null',
                        "totalTransactionAmount": 'null',
                        "priority": 'null',
                        "onboarding": 'false',
                        "paymentMode": "BANK_MANDATE",
                        "isHybridDisabled": 'false'
                    }],
                    "savedInstruments": [{
                        "isDisabled": {
                            "status": "false",
                            "msg": 'null'
                        },
                        "hasLowSuccess": {
                            "status": "false",
                            "msg": ""
                        },
                        "iconUrl": "https://staticgw-stage1.paytm.in/25.1.0/images/web/merchant4/visa.png",
                        "oneClickSupported": 'false',
                        "cardDetails": {
                            "cardId": "1159311733",
                            "cardType": "DEBIT_CARD",
                            "expiryDate": 'null',
                            "firstSixDigit": "411111",
                            "lastFourDigit": "1111",
                            "status": "1",
                            "cvvLength": "3",
                            "cvvRequired": 'true'
                        },
                        "issuingBank": "BBK",
                        "isEmiAvailable": 'false',
                        "authModes": ["otp"],
                        "displayName": "BBK - Debit Card",
                        "priority": 'null',
                        "paymentOfferDetails": 'null',
                        "isHybridDisabled": 'false',
                        "channelCode": "VISA",
                        "channelName": "Visa Inc.",
                        "isEmiHybridDisabled": 'false'
                    }],
                    "userProfileSarvatra": 'null',
                    "activeSubscriptions": 'null'
                },
                "addMoneyPayOption": {
                    "paymentModes": 'null',
                    "savedInstruments": [],
                    "userProfileSarvatra": 'null',
                    "activeSubscriptions": 'null'
                },
                "merchantLimitInfo": {
                    "merchantRemainingLimits": [],
                    "excludedPaymodes": 'null',
                    "message": "limit is breached for this pay-mode"
                }
            }
        },
    "FetchPCFDetails":
        {
            "head": {
                "responseTimestamp": "1587112457638",
                "version": "v1",
                "requestId": 'null'
            },
            "body": {
                "extraParamsMap": 'null',
                "resultInfo": {
                    "resultMsg": "Success",
                    "resultStatus": "S",
                    "resultCode": "0000"
                },
                "consultDetails": {
                    "CREDIT_CARD": {
                        "displayText": "Credit Card",
                        "totalConvenienceCharges": {
                            "currency": "INR",
                            "value": "1.19"
                        },
                        "totalTransactionAmount": {
                            "currency": "INR",
                            "value": "2.19"
                        },
                        "text": "Rs. 1.01 + GST as applicable.",
                        "taxAmount": {
                            "currency": "INR",
                            "value": "0.18"
                        },
                        "payMethod": "CREDIT_CARD",
                        "feeAmount": {
                            "currency": "INR",
                            "value": "1.01"
                        },
                        "baseTransactionAmount": {
                            "currency": "INR",
                            "value": "1.00"
                        }
                    }
                }
            }
        },
    "FetchBinDetails":
        {
            'head': {
                'requestId': 'null',
                'responseTimestamp': "1590989895825",
                'version': "v1"
            },
            'body': {
                'resultInfo': {
                    'resultStatus': "S",
                    'resultCode': "0000",
                    'resultMsg': "Success"
                },
                'isEmiAvailable': 'false',
                'binDetail': {
                    'bin': "411111",
                    'issuingBank': "JPMorgan Chase Bank",
                    'issuingBankCode': "JPMC",
                    'paymentMode': "CREDIT_CARD",
                    'channelName': "VISA",
                    'channelCode': "VISA",
                    'cnMin': "13",
                    'cnMax': "19",
                    'cvvR': "true",
                    'cvvL': "3",
                    'expR': "true",
                    'isActive': "true",
                    'isIndian': "true"
                },
                'authModes': [
                    "otp"
                ],
                'hasLowSuccessRate': {
                    'status': "false",
                    'msg': ""
                },
                'iconUrl': "https://staticgw-stage1.paytm.in/25.1.0/",
                'errorMessage': "EMI not available",
                'isHybridDisabled': 'false',
                'oneClickSupported': 'false',
                'oneClickMaxAmount': "2000"
            }
        },
    "SendOTP":
        {
            "head": {
                "requestId": 'null',
                "responseTimestamp": "1566977760870",
                "version": "v1"
            },
            "body": {
                "resultInfo": {
                    "resultStatus": "SUCCESS",
                    "resultCode": "01",
                    "resultMsg": "Otp sent to phone"
                },
                "extraParamsMap": 'null'
            }
        },
    "ValidateOTP":
        {
            "head": {
                "requestId": 'null',
                "responseTimestamp": "1566978340322",
                "version": "v1"
            },
            "body": {
                "resultInfo": {
                    "resultStatus": "SUCCESS",
                    "resultCode": "01"
                },
                "authenticated": 'true',
                "extraParamsMap": 'null'
            }
        },
    "FetchBalanceInfo":
        {
            "head": {
                "requestId": 'null',
                "responseTimestamp": "1567062349611",
                "version": "v1"
            },
            "body": {
                "resultInfo": {
                    "resultStatus": "S",
                    "resultCode": "0000",
                    "resultMsg": "Success"
                },
                "extraParamsMap": 'null',
                "balanceInfo": {
                    "currency": "INR",
                    "value": "18705.19"
                }
            }
        },
    "FetchNBPaymentChannel":
        {
            "head": {
                "requestId": 'null',
                "responseTimestamp": "1567084657276",
                "version": "v1"
            },
            "body": {
                "resultInfo": {
                    "resultStatus": "S",
                    "resultCode": "0000",
                    "resultMsg": "Success"
                },
                "extraParamsMap": 'null',
                "nbPayOption": {
                    "displayName": "Net Banking",
                    "isDisabled": {
                        "status": "false",
                        "msg": ""
                    },
                    "payChannelOptions": [{
                        "isDisabled": {
                            "status": "false",
                            "msg": 'null'
                        },
                        "hasLowSuccess": {
                            "status": "false",
                            "msg": ""
                        },
                        "iconUrl": "https://staticgw-stage1.paytm.in/native/bank/ANDB.png",
                        "isHybridDisabled": 'false',
                        "channelCode": "ANDB",
                        "channelName": "Andhra Bank"
                    }, {
                        "isDisabled": {
                            "status": "false",
                            "msg": 'null'
                        },
                        "hasLowSuccess": {
                            "status": "false",
                            "msg": ""
                        },
                        "iconUrl": "https://staticgw-stage1.paytm.in/native/bank/AXIS.png",
                        "isHybridDisabled": 'false',
                        "channelCode": "AXIS",
                        "channelName": "Axis Bank"
                    }, {
                        "isDisabled": {
                            "status": "false",
                            "msg": 'null'
                        },
                        "hasLowSuccess": {
                            "status": "false",
                            "msg": ""
                        },
                        "iconUrl": "https://staticgw-stage1.paytm.in/native/bank/CANARA.png",
                        "isHybridDisabled": 'false',
                        "channelCode": "CANARA",
                        "channelName": "Canara Bank"
                    }, {
                        "isDisabled": {
                            "status": "false",
                            "msg": 'null'
                        },
                        "hasLowSuccess": {
                            "status": "false",
                            "msg": ""
                        },
                        "iconUrl": "https://staticgw-stage1.paytm.in/native/bank/ICICI.png",
                        "isHybridDisabled": 'false',
                        "channelCode": "ICICI",
                        "channelName": "ICICI Bank"
                    }, {
                        "isDisabled": {
                            "status": "false",
                            "msg": 'null'
                        },
                        "hasLowSuccess": {
                            "status": "false",
                            "msg": ""
                        },
                        "iconUrl": "https://staticgw-stage1.paytm.in/native/bank/IDBI.png",
                        "isHybridDisabled": 'false',
                        "channelCode": "IDBI",
                        "channelName": "IDBI Bank"
                    }, {
                        "isDisabled": {
                            "status": "false",
                            "msg": 'null'
                        },
                        "hasLowSuccess": {
                            "status": "false",
                            "msg": ""
                        },
                        "iconUrl": "https://staticgw-stage1.paytm.in/native/bank/VJYA.png",
                        "isHybridDisabled": 'false',
                        "channelCode": "VJYA",
                        "channelName": "Vijaya Bank"
                    }, {
                        "isDisabled": {
                            "status": "false",
                            "msg": 'null'
                        },
                        "hasLowSuccess": {
                            "status": "false",
                            "msg": ""
                        },
                        "iconUrl": "https://staticgw-stage1.paytm.in/native/bank/YES.png",
                        "isHybridDisabled": 'false',
                        "channelCode": "YES",
                        "channelName": "Yes Bank"
                    }],
                    "feeAmount": 'null',
                    "taxAmount": 'null',
                    "totalTransactionAmount": 'null',
                    "priority": 'null',
                    "onboarding": 'false',
                    "paymentMode": "NET_BANKING",
                    "isHybridDisabled": 'false'
                }
            }
        },
    "ValidateVPA":
        {
            "head": {
                "requestId": 'null',
                "responseTimestamp": "1584172395417",
                "version": "v1"
            },
            "body": {
                "extraParamsMap": 'null',
                "resultInfo": {
                "resultStatus": "S",
                "resultCode": "0000",
                "resultMsg": "Success"
                },
                "vpa": "7777777777@paytm",
                "valid": 'true'
            }
        },
    "ProcessTransaction":
        {
            "head": {
                "responseTimestamp": "1567163330727",
                "version": "v1"
            },
            "body": {
                "resultInfo": {
                    "resultStatus": "S",
                    "resultCode": "0000",
                    "resultMsg": "Success"
                },
                "bankForm": {
                    "pageType": "direct",
                    "isForceResendOtp": 'false',
                    "redirectForm": {
                        "actionUrl": "https://securegw-stage.paytm.in/instaproxy/directbank/HDFO/CC/payment",
                        "method": "POST",
                        "type": "redirect",
                        "headers": {
                            "Content-Type": "application/x-www-form-urlencoded"
                        },
                        "content": {
                            "mbid": "70020748",
                            "orderid": "YOUR_ORDER_ID",
                            "txnamount": "1.0",
                            "bankAbbr": "HDFC",
                            "channelid": "WAP",
                            "txnid": "90190830000084518755",
                            "isResend": "true"
                        }
                    },
                    "directForms": [{
                        "actionUrl": "https://securegw-stage.paytm.in/theia/api/v1/directBankRequest?mid=YOUR_MID_HERE&orderId=YOUR_ORDER_ID",
                        "method": "POST",
                        "type": "submit",
                        "headers": {
                            "Content-Type": "application/json;charset=UTF-8"
                        },
                        "content": {
                            "txnToken": "71c19331a8b84f3988eb2067cebd53d91567163324641",
                            "requestType": "submit",
                            "otp": ""
                        }
                    }, {
                        "actionUrl": "https://securegw-stage.paytm.in/theia/api/v1/directBankRequest?mid=YOUR_MID_HERE&orderId=YOUR_ORDER_ID",
                        "method": "POST",
                        "type": "cancel",
                        "headers": {
                            "Content-Type": "application/json;charset=UTF-8"
                        },
                        "content": {
                            "txnToken": "71c19331a8b84f3988eb2067cebd53d91567163324641",
                            "requestType": "cancel"
                        }
                    }, {
                        "actionUrl": "https://securegw-stage.paytm.in/theia/api/v1/directBankRequest?mid=YOUR_MID_HERE&orderId=YOUR_ORDER_ID",
                        "method": "POST",
                        "type": "resend",
                        "headers": {
                            "Content-Type": "application/json;charset=UTF-8"
                        },
                        "content": {
                            "txnToken": "71c19331a8b84f3988eb2067cebd53d91567163324641",
                            "requestType": "resend"
                        }
                    }, {
                        "actionUrl": "https://securegw-stage.paytm.in/instaproxy/bankresponse/BANKCODE/NB",
                        "method": "POST",
                        "type": "payonbank",
                        "headers": {
                            "Content-Type": "application/x-www-form-urlencoded"
                        },
                        "content": {
                            "bankCode": "HDFO",
                            "mbid": "70020748",
                            "orderid": "YOUR_ORDER_ID",
                            "txnamount": "1.0",
                            "paymentMode": "CC",
                            "response": "retry",
                            "bankAbbr": "HDFC",
                            "channelid": "WAP",
                            "txnid": "90190830000084518755"
                        }
                    }],
                    "displayField": {
                        "amount": "1.0",
                        "headerText": "Authenticate Payment of Rs. 1",
                        "bankName": "HDFC",
                        "bankLogo": "https://staticgw.paytm.in/native/bank/HDFC.png",
                        "descriptionText": "Enter One Time Password (OTP) sent by HDFC on your registered mobile number"
                    }
                }
            }
        },
    "OauthToken":
        {
            'scope': "paytm",
            'access_token': "ae74f8b5-be5f-4503-XXXX-a60c9dcd3300",
            'expires': 1594011297000
        },
    "Refund":
        {
            "head": {
                "responseTimestamp": "1567421120859",
                "signature": "WaFdplm36GmfBtZ6jPIFClLSEffhAk9fTpJ6i8WpgqiZvtUNl53mLL7mu4JWwxPpfSa5pdexyxK/68WtoTmd53TI+R9GffjGc3USoLgWcKI=",
                "version": "v1"
            },
            "body": {
                "txnTimestamp": "2019-09-02 12:31:49.0",
                "orderId": "YOUR_ORDER_ID",
                "mid": "YOUR_MID_HERE",
                "refId": "UNIQUE_REFUND_ID",
                "resultInfo": {
                    "resultStatus": "PENDING",
                    "resultCode": "601",
                    "resultMsg": "Refund request was raised for this transaction. But it is pending state"
                },
                "refundId": "PAYTM_REFUND_ID",
                "txnId": "PAYTM_TRANSACTION_ID",
                "refundAmount": "1.00"
            }
        },
    "RefundStatus":
        {
            "head": {
                "clientId": "C11",
                "responseTimestamp": "1556719120393",
                "signature": "Stx6P9HpnEG3GADkMuOcj50dm7ZHmvMPd29b8K5rxi4aVzRcJ5hklZo//RZdtTA+zcll8sdelyAYsxqPxFs66RVE0F2b9RElTMqYSfBj89I=",
                "version": "v1"
            },
            "body": {
                "orderId": "YOUR_ORDER_ID",
                "userCreditInitiateStatus": "SUCCESS",
                "mid": "YOUR_MID_HERE",
                "merchantRefundRequestTimestamp": "2019-05-01 19:27:25.0",
                "resultInfo": {
                    "resultStatus": "TXN_SUCCESS",
                    "resultCode": "10",
                    "resultMsg": "Refund Successfull"
                },
                "txnTimestamp": "2019-05-01 19:25:41.0",
                "acceptRefundTimestamp": "2019-05-01 19:27:25.0",
                "acceptRefundStatus": "SUCCESS",
                "refundDetailInfoList": [{
                    "refundType": "TO_SOURCE",
                    "payMethod": "BALANCE",
                    "userCreditExpectedDate": "2019-05-02",
                    "userMobileNo": "91-******7777",
                    "refundAmount": "1.00"
                }],
                "userCreditInitiateTimestamp": "2019-05-01 19:27:26.0",
                "totalRefundAmount": "1.00",
                "refId": "UNIQUE_REFUND_ID",
                "txnAmount": "10.00",
                "refundId": "PAYTM_REFUND_ID",
                "txnId": "PAYTM_TRANSACTION_ID",
                "refundAmount": "1.00"
            }
        }

        }