from django.contrib import admin
from api.models import (User, CommoditySellerProfile, CommodityBuyerProfile, CommodityTransportProviderProfile,
                        BankDetail, CommodityInfo, Address, KYCDetail, Rating, StateWiseDistrict,
                        CommodityDetail, BidDetail, BidStatus, MandiAdministrator, MandiAgent, MandiTrader,
                        Logistic, WarehouseDetails, AgriEquipmentAgency, AgriEquipmentDetail)

admin.site.register(User)
admin.site.register(CommoditySellerProfile)
admin.site.register(CommodityBuyerProfile)
admin.site.register(CommodityTransportProviderProfile)
admin.site.register(BankDetail)
admin.site.register(CommodityInfo)
admin.site.register(Address)
admin.site.register(KYCDetail)
admin.site.register(CommodityDetail)
admin.site.register(BidDetail)
admin.site.register(BidStatus)
admin.site.register(MandiAdministrator)
admin.site.register(MandiAgent)
admin.site.register(MandiTrader)
admin.site.register(Logistic)
admin.site.register(WarehouseDetails)
admin.site.register(AgriEquipmentAgency)
admin.site.register(AgriEquipmentDetail)
admin.site.register(Rating)
admin.site.register(StateWiseDistrict)

