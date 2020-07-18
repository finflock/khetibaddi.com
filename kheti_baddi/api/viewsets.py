from rest_framework import viewsets, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
import pandas as pd


from .serializers import *
url='https://enam.gov.in/web/commodity/commodity-list'
from .utils import gmaps


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['email','commodity_seller', 'commodity_buyer', 'commodity_transport_provider']

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = self.request.data
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommoditySellerProfileViewSet(viewsets.ModelViewSet):
    queryset = CommoditySellerProfile.objects.all()
    serializer_class = CommoditySellerProfileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user',]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = self.request.data
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommodityBuyerProfileViewSet(viewsets.ModelViewSet):
    queryset = CommodityBuyerProfile.objects.all()
    serializer_class = CommodityBuyerProfileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = self.request.data
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommodityTransportProviderProfileViewSet(viewsets.ModelViewSet):
    queryset = CommodityTransportProviderProfile.objects.all()
    serializer_class = CommodityTransportProviderProfileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = self.request.data
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BankDetailViewSet(viewsets.ModelViewSet):
    queryset = BankDetail.objects.all()
    serializer_class = BankDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'account_holder_name']

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = self.request.data
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommodityDetailViewSet(viewsets.ModelViewSet):
    queryset = CommodityDetail.objects.all()
    serializer_class = CommodityDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'grain_name','name','quantity','status','active']

    def create(self, request, *args, **kwargs):
        data = self.request.data
        get_name = CommodityInfo.objects.filter(id=data['grain_name'])
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(name=get_name[0])
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = self.request.data
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommodityInfoViewSet(viewsets.ModelViewSet):
    queryset = CommodityInfo.objects.all()
    serializer_class = CommodityInfoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['grain_name', 'category']

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = self.request.data
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'address_1', 'address_2', 'state', 'district','tehsil']

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = self.request.data
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class KYCDetailViewSet(viewsets.ModelViewSet):
    queryset = KYCDetail.objects.all()
    serializer_class = KYCDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user',]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = self.request.data
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BidDetailViewSet(viewsets.ModelViewSet):
    queryset = BidDetail.objects.all()
    serializer_class = BidDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'commodity_detail', 'quantity', 'bid_price', 'commodity_name']

    def create(self, request, *args, **kwargs):
        data = self.request.data
        get_name = CommodityDetail.objects.filter(id=data['name'])
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(name=get_name[0])
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = self.request.data
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BidStatusViewSet(viewsets.ModelViewSet):
    queryset = BidStatus.objects.all()
    serializer_class = BidStatusSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['bid_detail', 'commodity_detail', 'status']

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = self.request.data
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MandiAdministratorViewSet(viewsets.ModelViewSet):
    queryset = MandiAdministrator.objects.all()
    serializer_class = MandiAdministratorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user',]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = self.request.data
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MandiAgentViewSet(viewsets.ModelViewSet):
    queryset = MandiAgent.objects.all()
    serializer_class = MandiAgentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user',]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = self.request.data
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MandiTraderViewSet(viewsets.ModelViewSet):
    queryset = MandiTrader.objects.all()
    serializer_class = MandiTraderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user',]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = self.request.data
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LogisticViewSet(viewsets.ModelViewSet):
    queryset = Logistic.objects.all()
    serializer_class = LogisticSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['commodity_transport_provider','commodity_seller', 'commodity_buyer','source','destination',
                        'distance','estimate_charges','total_charges','status']

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = self.request.data
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class WarehouseDetailsViewSet(viewsets.ModelViewSet):
    queryset = WarehouseDetails.objects.all()
    serializer_class = WarehouseDetailsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user',]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = self.request.data
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AgriEquipmentAgencyViewSet(viewsets.ModelViewSet):
    queryset = AgriEquipmentAgency.objects.all()
    serializer_class = AgriEquipmentAgencySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user',]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = self.request.data
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AgriEquipmentDetailViewSet(viewsets.ModelViewSet):
    queryset = AgriEquipmentDetail.objects.all()
    serializer_class = AgriEquipmentDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['equipment_name',]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = self.request.data
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['rating_by','rating_to','rating']

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = self.request.data
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class StateWiseDistrictViewSet(viewsets.ModelViewSet):
    queryset = StateWiseDistrict.objects.all()
    serializer_class = StateWiseDistrictSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['state','district']

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = self.request.data
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetCommodityList(viewsets.ViewSet):
    def list(self, request):
        data = pd.read_html(url)
        l = {"FOOD_GRAINS_CEREALS": [], "OILSEEDS": [], "FRUITS": [], "VEGETABLES": [], "SPICES": [], "MISC": [], }
        for i in data:
            d = i.values
            if i.columns[0] == 'FOOD GRAINS/ CEREALS':
                for m in d:
                    l['FOOD_GRAINS_CEREALS'].append(m[0])

            if i.columns[0] == 'OILSEEDS':
                for m in d:
                    l['OILSEEDS'].append(m[0])

            if i.columns[0] == 'FRUITS':
                for m in d:
                    l['FRUITS'].append(m[0])

            if i.columns[0] == 'VEGETABLES':
                for m in d:
                    l['VEGETABLES'].append(m[0])

            if i.columns[0] == 'SPICES':
                for m in d:
                    l['SPICES'].append(m[0])

            if i.columns[0] == 'MISC':
                for m in d:
                    l['MISC'].append(m[0])

        return Response(l)


class GoogleDistanceMatrix(viewsets.ViewSet):
    def list(self, request):
        source = self.request.GET.get('source')
        destination = self.request.GET.get('destination')
        if (source and destination) is not None:

            gdm = gmaps.distance_matrix(source, destination)

            return Response(gdm)

        return Response({"Note: ": "Please input the source and destination"})