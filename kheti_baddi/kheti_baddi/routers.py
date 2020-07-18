from rest_framework import routers

from api.viewsets import *
from api.paytm import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'commodity-seller-profile', CommoditySellerProfileViewSet, basename='commodity-seller-profile')
router.register(r'commodity-buyer-profile', CommodityBuyerProfileViewSet, basename='commodity-buyer-profile')
router.register(r'commodity-transport-provider-profile', CommodityTransportProviderProfileViewSet, basename='commodity-transport-provider-profile')
router.register(r'bank-detail', BankDetailViewSet, basename='bank-detail')
router.register(r'commodity-detail', CommodityDetailViewSet, basename='commodity-detail')
router.register(r'commodity-info', CommodityInfoViewSet, basename='commodity-info')
router.register(r'address', AddressViewSet, basename='address')
router.register(r'kyc-detail', KYCDetailViewSet, basename='kyc-detail')
router.register(r'bid-detail', BidDetailViewSet, basename='bid-detail')
router.register(r'bid-status', BidStatusViewSet, basename='bid-status')
router.register(r'mandi-administrator', MandiAdministratorViewSet, basename='mandi-administrator')
router.register(r'logistic', LogisticViewSet, basename='logistic')
router.register(r'rating', RatingViewSet, basename='rating')
router.register(r'state-wise-district', StateWiseDistrictViewSet, basename='state-wise-district')
router.register(r'get-commodity-list', GetCommodityList, basename='get-commodity-list')
router.register(r'google-distance-matrix', GoogleDistanceMatrix, basename='google-distance-matrix')


router.register(r'initiate-transaction', InitiateTransaction, basename='InitiateTransaction')
router.register(r'update-transaction', UpdateTransaction, basename='UpdateTransaction')
router.register(r'fetch-payment-options', FetchPaymentOptions, basename='FetchPaymentOptions')
router.register(r'fetch-pcf-details', FetchPCFDetails, basename='FetchPCFDetails')
router.register(r'fetch-bin-details', FetchBinDetails, basename='FetchBinDetails')
router.register(r'send-otp', SendOTP, basename='SendOTP')
router.register(r'validate-otp', ValidateOTP, basename='ValidateOTP')
router.register(r'fetch-balance-info', FetchBalanceInfo, basename='FetchBalanceInfo')
router.register(r'fetch-nb-payment-channel', FetchNBPaymentChannel, basename='FetchNBPaymentChannel')
router.register(r'validate-vpa', ValidateVPA, basename='ValidateVPA')
router.register(r'process-transaction', ProcessTransaction, basename='ProcessTransaction')
router.register(r'OauthToken', OauthToken, basename='OauthToken')
router.register(r'refund', Refund, basename='Refund')
router.register(r'refund-status', RefundStatus, basename='RefundStatus')