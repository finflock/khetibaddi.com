from rest_framework import serializers
from rest_framework import exceptions
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from django.db.models import Q

from api.models import (User, CommoditySellerProfile, CommodityBuyerProfile, CommodityTransportProviderProfile,
                        BankDetail, CommodityInfo, Address, KYCDetail, Rating, StateWiseDistrict,
                        CommodityDetail, BidDetail, BidStatus, MandiAdministrator, MandiAgent, MandiTrader,
                        Logistic, WarehouseDetails, AgriEquipmentAgency, AgriEquipmentDetail)


class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    email = serializers.EmailField(required=True, label='Email')
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ['email', 'password', 'token']
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        user_obj = None
        email = data.get("email", None)
        password = data.get("password", None)

        if not email and not password:
            raise ValidationError("Must provide email and password both.")

        user = User.objects.filter(
            Q(email=email)
        ).distinct()
        if user.exists() and user.count() == 1:
            user.first()
        else:
            raise ValidationError('This Email is not valid')
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError('Incorrect credentials please try again.')
        data['token'] = 'some random token'

        return data


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get("email", "")
        password = data.get("password", "")

        if email and password:
            user = authenticate(username=email, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    raise exceptions.ValidationError("User is deactivated.")
            else:
                raise exceptions.ValidationError("Unable to login with given credentials.")
        else:
            raise exceptions.ValidationError("Must provide username and password both.")
        return data


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'mobile', 'password', 'password2', 'commodity_seller', 'commodity_buyer',
                  'commodity_transport_provider', 'mandi_administrator', 'manager',
                  'is_active', 'is_staff', 'created']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        account = User(
            email=self.validated_data['email'],
            mobile=self.validated_data['mobile']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Password must match'})
        account.set_password(password)
        account.save()
        return account


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'mobile', 'password', 'gender', 'commodity_seller', 'commodity_buyer',
                  'commodity_transport_provider', 'mandi_administrator', 'manager',
                  'is_active', 'is_staff', 'created']

    validate_password = make_password


class CommoditySellerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommoditySellerProfile
        fields = '__all__'


class CommodityBuyerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommodityBuyerProfile
        fields = '__all__'


class CommodityTransportProviderProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommodityTransportProviderProfile
        fields = '__all__'


class BankDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankDetail
        fields = '__all__'


class CommodityInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommodityInfo
        fields = '__all__'


class CommodityDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommodityDetail
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class KYCDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = KYCDetail
        fields = '__all__'


class BidDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BidDetail
        fields = '__all__'


class BidStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = BidStatus
        fields = '__all__'


class MandiAdministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MandiAdministrator
        fields = '__all__'


class MandiAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MandiAgent
        fields = '__all__'


class MandiTraderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MandiTrader
        fields = '__all__'


class LogisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logistic
        fields = '__all__'


class WarehouseDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseDetails
        fields = '__all__'


class AgriEquipmentAgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = AgriEquipmentAgency
        fields = '__all__'


class AgriEquipmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgriEquipmentDetail
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class StateWiseDistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateWiseDistrict
        fields = '__all__'

