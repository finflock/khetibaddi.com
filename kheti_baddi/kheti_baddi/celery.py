import os, datetime
import pytz
from celery import Celery
from django.db.models import Max, Avg

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kheti_baddi.settings')

app = Celery('kheti_baddi', broker='redis://localhost')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
utc=pytz.UTC
asian_timezone = pytz.timezone('Asia/Kolkata')

@app.task(bind=True)
def auction_task(self):
    from api.models import BidStatus, BidDetail, CommodityDetail, Logistic, Address
    from api.utils import gmaps
    # manage commodity for auction
    qs = CommodityDetail.objects.exclude(active=False)
    for i in qs:
        if asian_timezone.localize(datetime.datetime.now()) >= i.auction:
            bid_d = BidDetail.objects.filter(active=True, commodity_detail=i.id)
            if bid_d.exists():
                max_bid_price = BidDetail.objects.filter(active=True, commodity_detail=i.id).aggregate(Max('bid_price'))['bid_price__max']
                avr_bid_price = BidDetail.objects.filter(active=True, commodity_detail=i.id).aggregate(Avg('bid_price'))['bid_price__avg']
                get_bid = BidDetail.objects.filter(bid_price=max_bid_price, commodity_detail=i.id)
                BidDetail.objects.filter(bid_price=max_bid_price, commodity_detail=i.id).update(accept_bid=True)
                source = Address.objects.filter(user=i.user)
                source_address = source.values('address_1')[0]['address_1'] + ' ' + source.values('address_2')[0][
                    'address_2'] + ' ' +  source.values('district')[0]['district'] + ' ' +  source.values('state')[0]['state']

                for m in get_bid:
                    destination = Address.objects.filter(user=m.user)
                    destination_address = destination.values('address_1')[0]['address_1'] + ' ' +  \
                                      destination.values('address_2')[0]['address_2'] + ' ' +  \
                                      destination.values('district')[0]['district'] + ' ' +  destination.values('state')[0][
                                          'state']
                    gdm = gmaps.distance_matrix(source_address, destination_address)
                    Logistic.objects.create(commodity_transport_provider=i.user,
                                            commodity_seller=i.user,
                                            commodity_buyer=m.user,
                                            source=source_address,
                                            destination=destination_address,
                                            distance=gdm['rows'][0]['elements'][0]['distance']['text'],
                                            estimate_charges=gdm['rows'][0]['elements'][0]['distance']['value']*0.01)
                    get_bid.update(accept_bid=True)

                CommodityDetail.objects.filter(auction=i.auction).update(active=False, bid_count=BidDetail.objects.filter(commodity_detail=i).count(),
                                                                         average_bid_price=avr_bid_price)



