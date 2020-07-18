from datetime import timedelta
from django.conf import settings
from django.urls import reverse, reverse_lazy
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
from django.core.mail import send_mail
from django.template.loader import get_template
from django.utils import timezone
from django.core.validators import (EmailValidator, RegexValidator, FileExtensionValidator)


from kheti_baddi.utils import unique_key_generator
from .utils import STATE_CHOICES, COMMODITY_CATEGORIES, BID_STATUS, GENDER_CHOICES, KYC_ID_CHOICES, STATUS_CHOICES
# send_mail(subject, message, from_email, recipient_list, html_message)

DEFAULT_ACTIVATION_DAYS = getattr(settings, 'DEFAULT_ACTIVATION_DAYS', 7)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=False, is_staff=False, is_admin=False,
                    is_commodity_seller=True, is_commodity_buyer=False, is_commodity_transport_provider=False,
                    is_mandi_administrator=False, is_manager=False):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        user = self.model(
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.is_active = is_active
        user.staff = is_staff
        user.admin = is_admin
        user.commodity_seller = is_commodity_seller
        user.commodity_buyer = is_commodity_buyer
        user.commodity_transport_provider = is_commodity_transport_provider
        user.mandi_administrator = is_mandi_administrator
        user.manager = is_manager
        user.save(using=self._db)
        return user

    def create_commodity_seller(self, email, password=None):
        user = self.create_user(
                email,
                password=password,
                is_commodity_seller=True
        )
        return user

    def create_commodity_buyer(self, email, password=None):
        user = self.create_user(
                email,
                password=password,
                is_commodity_buyer=True
        )
        return user

    def create_commodity_transport_provider(self, email, password=None):
        user = self.create_user(
                email,
                password=password,
                is_commodity_transport_provider=True
        )
        return user

    def create_mandi_administrator(self, email, password=None):
        user = self.create_user(
                email,
                password=password,
                is_mandi_administrator=True
        )
        return user

    def create_manager(self, email, password=None):
        user = self.create_user(
                email,
                password=password,
                is_manager=True
        )
        return user

    def create_staffuser(self, email, password=None):
        user = self.create_user(
                email,
                password=password,
                is_staff=True,
                is_active=True,
                is_commodity_seller=True,
                is_commodity_buyer=True,
                is_commodity_transport_provider=True,
                is_mandi_administrator=True,
                is_manager=True
        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
                email,
                password=password,
                is_staff=True,
                is_admin=True,
                is_active=True,
                is_commodity_seller=True,
                is_commodity_buyer=True,
                is_commodity_transport_provider=True,
                is_mandi_administrator=True,
                is_manager=True
        )
        return user


class User(AbstractBaseUser):
    # username = models.CharField(max_length=250, unique=True)
    email = models.EmailField(db_index=True, validators=[EmailValidator], unique=True)
    mobile = models.CharField(max_length=10, db_index=True,
                              validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message='Enter a valid phone number')],
                              unique=True)
    # first_name = models.CharField(max_length=250)
    full_name = models.CharField(max_length=250, blank=True, null=True)
    gender = models.CharField(max_length=120, blank=True, null=True, choices=GENDER_CHOICES)
    # country = models.CharField(max_length=250)

    commodity_seller = models.BooleanField(default=False)
    commodity_buyer = models.BooleanField(default=False)
    commodity_transport_provider = models.BooleanField(default=False)
    mandi_administrator = models.BooleanField(default=False)
    manager = models.BooleanField(default=False)

    is_active = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile',]

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        if self.is_admin:
            return True
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_commodity_seller(self):
        return self.commodity_seller

    @property
    def is_commodity_buyer(self):
        return self.commodity_buyer

    @property
    def is_commodity_transport_provider(self):
        return self.commodity_transport_provider

    @property
    def is_mandi_administrator(self):
        return self.mandi_administrator


class EmailActivationQuerySet(models.query.QuerySet):

    def to_be_confirm(self):
        now = timezone.now()
        start_range = now - timedelta(days=DEFAULT_ACTIVATION_DAYS)
        end_range = now
        return self.filter(
                activated= False,
                forced_expired= False
              ).filter(
                created__gt=start_range,
                created__lte=end_range
              )


class EmailActivationManager(models.Manager):
    def get_queryset(self):
        return EmailActivationQuerySet(self.model, using=self._db)

    def to_be_confirm(self):
        return self.get_queryset().to_be_confirm()

    def email_exists(self, email):
        return self.get_queryset().filter(
                    Q(email=email) |
                    Q(user__email=email)
                ).filter(
                    activated=False
                )


class EmailActivation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    key = models.CharField(max_length=120, blank=True, null=True)
    activated = models.BooleanField(default=False)
    forced_expired = models.BooleanField(default=False)
    expires = models.IntegerField(default=7)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    objects = EmailActivationManager()

    def __str__(self):
        return self.email

    def can_activate(self):
        qs = EmailActivation.objects.filter(pk=self.pk).to_be_confirm()
        if qs.exists():
            return True
        return False

    def activate(self):
        if self.can_activate():
            # pre activation user signal
            user = self.user
            user.is_active = True
            user.save()
            # post activation signal for user
            self.activated = True
            self.save()
            return True
        return False

    def regenerate(self):
        self.key = None
        self.save()
        if self.key is not None:
            return True
        return False

    def send_activation(self):
        if not self.activated and not self.forced_expired:
            if self.key:
                print('email send')
                base_url = getattr(settings, 'BASE_URL', 'http://www.finflock.com')
                key_path = reverse("email-activation", kwargs={'key': self.key})
                path = "{base}{path}".format(base=base_url, path=key_path)
                context = {
                    'path': path,
                    'email': self.email
                }
                txt_ = get_template("registration/emails/verify.txt").render(context)
                html_ = get_template("registration/emails/verify.html").render(context)
                subject = '1-Click Email Verification'
                from_email = settings.DEFAULT_FROM_EMAIL
                recipient_list = [self.email]
                sent_mail = send_mail(
                            subject,
                            txt_,
                            from_email,
                            recipient_list,
                            html_message=html_,
                            fail_silently=False,
                    )
                return sent_mail
                return True
        return False


def pre_save_email_activation(sender, instance, *args, **kwargs):
    if not instance.activated and not instance.forced_expired:
        if not instance.key:
            instance.key = unique_key_generator(instance)


pre_save.connect(pre_save_email_activation, sender=EmailActivation)


def post_save_user_create_receiver(sender, instance, created, *args, **kwargs):
    if created:
        obj = EmailActivation.objects.create(user=instance, email=instance.email)
        obj.send_activation()
        CommoditySellerProfile.objects.create(user=instance)
        Address.objects.create(user=instance)
        BankDetail.objects.create(user=instance)
        KYCDetail.objects.create(user=instance)


post_save.connect(post_save_user_create_receiver, sender=User)


class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_address')
    address_1 = models.CharField(max_length=250, blank=True, null=True)
    address_2 = models.CharField(max_length=250, blank=True, null=True)
    pin_code = models.CharField(max_length=250, blank=True, null=True)
    state = models.CharField(choices=STATE_CHOICES, max_length=250, blank=True, null=True)
    district = models.CharField(max_length=250, blank=True, null=True)
    tehsil = models.CharField(max_length=250, blank=True, null=True)

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class KYCDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='kyc_detail')
    photo_id_type = models.CharField(max_length=250, blank=True, null=True, choices=KYC_ID_CHOICES)
    id_number = models.CharField(max_length=250, blank=True, null=True)
    upload_id = models.FileField(upload_to='kyc/%Y/%m/%d/', blank=True, null=True,
                                     validators=[
                                         FileExtensionValidator(allowed_extensions=['png', 'jpg', 'gif'])],
                                     help_text='Max size 2MB, and only pdf are allowed')

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class CommoditySellerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='commodity_seller_profile')
    date_of_birth = models.DateField(auto_now_add=False, blank=True, null=True)
    alternate_mobile_no_1 = models.CharField(max_length=250, blank=True, null=True)
    alternate_mobile_no_2 = models.CharField(max_length=250, blank=True, null=True)
    license_no = models.CharField(max_length=250, blank=True, null=True)
    company_name = models.CharField(max_length=250, blank=True, null=True)
    company_reg = models.CharField(max_length=250, blank=True, null=True)

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class CommodityBuyerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='commodity_buyer_profile')
    date_of_birth = models.DateField(auto_now_add=False, blank=True, null=True)
    mobile_no = models.CharField(max_length=250, blank=True, null=True)
    alternate_mobile_no = models.CharField(max_length=250, blank=True, null=True)
    license_no = models.CharField(max_length=250, blank=True, null=True)
    company_name = models.CharField(max_length=250, blank=True, null=True)
    company_reg = models.CharField(max_length=250, blank=True, null=True)

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class CommodityTransportProviderProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='commodity_transport_provider_profile')
    date_of_birth = models.DateField(auto_now_add=False, blank=True, null=True)
    alternate_mobile_no_1 = models.CharField(max_length=250, blank=True, null=True)
    alternate_mobile_no_2 = models.CharField(max_length=250, blank=True, null=True)
    license_no = models.CharField(max_length=250, blank=True, null=True)
    company_name = models.CharField(max_length=250, blank=True, null=True)
    company_reg = models.CharField(max_length=250, blank=True, null=True)
    landline_no = models.CharField(max_length=250, blank=True, null=True)
    year_of_establishment = models.CharField(max_length=250, blank=True, null=True)
    gst = models.CharField(max_length=250, blank=True, null=True)
    vehicle_image = models.FileField(upload_to='ctpp/%Y/%m/%d/', blank=True,
                                            validators=[
                                                FileExtensionValidator(allowed_extensions=['png', 'jpg', 'gif'])],
                                            help_text='Max size 2MB, and only pdf are allowed')

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class BankDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bank_detail_user')
    account_holder_name = models.CharField(max_length=120, blank=True, null=True)
    bank_account_number = models.CharField(max_length=120, blank=True, null=True)
    ifsc_code = models.CharField(max_length=120, blank=True, null=True)
    upload_passbook = models.FileField(upload_to='passbook/%Y/%m/%d/', blank=True, null=True,
                                       validators=[FileExtensionValidator(allowed_extensions=['pdf','png','jpg','jpeg'])],
                                       help_text='Max size 2MB, and only pdf are allowed')

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class CommodityInfo(models.Model):
    grain_name = models.CharField(max_length=120, blank=True, null=True)
    category = models.CharField(max_length=120, blank=True, null=True, choices=COMMODITY_CATEGORIES)
    upload_picture = models.FileField(upload_to='commodity_picture/', blank=True,
                                       validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'gif'])],
                                       help_text='Max size 2MB, and only pdf are allowed')

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.grain_name


class CommodityDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commodity_detail_user')
    grain_name = models.ForeignKey(CommodityInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, blank=True, null=True)
    quantity = models.PositiveSmallIntegerField(blank=True, null=True)
    auction = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    base_price = models.FloatField(blank=True, null=True, default=0)
    average_bid_price = models.FloatField(blank=True, null=True, default=0)
    bid_count = models.PositiveIntegerField(blank=True, null=True, default=0)
    status = models.CharField(max_length=50,blank=True, null=True, choices=(("Open", "Open"), ("Closed", "Closed")), default='Open')

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.grain_name)


class BidDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bid_agent_user')
    commodity_detail = models.ForeignKey(CommodityDetail, on_delete=models.CASCADE, related_name='commodity_detail')
    commodity_name = models.CharField(max_length=120, blank=True, null=True)
    buyer_name = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.PositiveSmallIntegerField(blank=True, null=True)
    bid_price = models.PositiveSmallIntegerField(blank=True, null=True)
    total_amount = models.PositiveSmallIntegerField(blank=True, null=True)
    expected_pickup_date = models.DateField(max_length=120, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    accept_bid = models.BooleanField(default=False)

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class BidStatus(models.Model):
    bid_detail = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bid_status')
    commodity_detail = models.ForeignKey(CommodityDetail, on_delete=models.CASCADE, related_name='bid_on')
    best_bid_matched_price = models.PositiveSmallIntegerField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=BID_STATUS, blank=True, null=True, default='Completed')

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class MandiAdministrator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mandi_administrator_user')
    full_name = models.CharField(max_length=120, blank=True, null=True)
    designation = models.CharField(max_length=120, blank=True, null=True)
    state = models.CharField(max_length=120, blank=True, null=True)
    district = models.CharField(max_length=120, blank=True, null=True)
    city = models.CharField(max_length=120, blank=True, null=True)
    town = models.CharField(max_length=120, blank=True, null=True)
    Address = models.CharField(max_length=120, blank=True, null=True)
    pin_code = models.PositiveSmallIntegerField(blank=True, null=True)
    mandi_name = models.CharField(max_length=120, blank=True, null=True)

    upload_mandi_picture = models.FileField(upload_to='mandi_picture/%Y/%m/%d/', blank=True,
                                       validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'gif'])],
                                       help_text='Max size 2MB, and only pdf are allowed')

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class MandiAgent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mandi_agent_user')
    full_name = models.CharField(max_length=120, blank=True, null=True)
    designation = models.CharField(max_length=120, blank=True, null=True)
    state = models.CharField(choices=STATE_CHOICES, max_length=120, blank=True, null=True)
    district = models.CharField(max_length=120, blank=True, null=True)
    city = models.CharField(max_length=120, blank=True, null=True)
    town = models.CharField(max_length=120, blank=True, null=True)
    Address = models.CharField(max_length=120, blank=True, null=True)
    pin_code = models.PositiveSmallIntegerField(blank=True, null=True)
    company_name = models.CharField(max_length=120, blank=True, null=True)
    license_or_company_registration = models.CharField(max_length=120, blank=True, null=True)
    gst_or_pan = models.DateField(max_length=120, blank=True, null=True)
    upload_picture = models.FileField(upload_to='upload_picture/%Y/%m/%d/', blank=True,
                                       validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'gif'])],
                                       help_text='Max size 2MB, and only pdf are allowed')

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class MandiTrader(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mandi_traders_user')
    full_name = models.CharField(max_length=120, blank=True, null=True)
    designation = models.CharField(max_length=120, blank=True, null=True)
    state = models.CharField(choices=STATE_CHOICES, max_length=120, blank=True, null=True)
    district = models.CharField(max_length=120, blank=True, null=True)
    city = models.CharField(max_length=120, blank=True, null=True)
    town = models.CharField(max_length=120, blank=True, null=True)
    Address = models.CharField(max_length=120, blank=True, null=True)
    pin_code = models.PositiveSmallIntegerField(blank=True, null=True)
    company_name = models.CharField(max_length=120, blank=True, null=True)
    license_or_company_registration = models.CharField(max_length=120, blank=True, null=True)
    gst_or_pan = models.CharField(max_length=120, blank=True, null=True)
    registration_level = models.CharField(max_length=120, blank=True, null=True)
    registered_with_mandi = models.CharField(max_length=120, blank=True, null=True)
    upload_picture = models.FileField(upload_to='upload_picture/%Y/%m/%d/', blank=True,
                                       validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'gif'])],
                                       help_text='Max size 2MB, and only pdf are allowed')

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Logistic(models.Model):
    commodity_transport_provider = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commodity_tp')
    commodity_seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='c_seller')
    commodity_buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='c_buyer')
    source = models.CharField(max_length=120, blank=True, null=True)
    destination = models.CharField(max_length=120, blank=True, null=True)
    distance = models.CharField(max_length=120, blank=True, null=True)
    estimate_charges = models.FloatField(blank=True, null=True)
    total_charges = models.FloatField(blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES ,max_length=120, blank=True, null=True, default='PENDING')

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class WarehouseDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='warehouse_user')
    warehouse_name = models.CharField(max_length=120, blank=True, null=True)
    authorized_person_name = models.CharField(max_length=120, blank=True, null=True)
    designation = models.CharField(max_length=120, blank=True, null=True)
    phone_number = models.PositiveSmallIntegerField(blank=True, null=True)
    state = models.CharField(choices=STATE_CHOICES, max_length=120, blank=True, null=True)
    district = models.CharField(max_length=120, blank=True, null=True)
    city = models.CharField(max_length=120, blank=True, null=True)
    town = models.CharField(max_length=120, blank=True, null=True)
    Address = models.CharField(max_length=120, blank=True, null=True)
    pin_code = models.PositiveSmallIntegerField(blank=True, null=True)
    company_name = models.CharField(max_length=120, blank=True, null=True)
    license_or_company_registration = models.CharField(max_length=120, blank=True, null=True)
    gst_or_pan = models.DateField(max_length=120, blank=True, null=True)
    upload_warehouse_picture = models.FileField(upload_to='upload_picture/%Y/%m/%d/', blank=True,
                                       validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'gif'])],
                                       help_text='Max size 2MB, and only pdf are allowed')

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class AgriEquipmentAgency(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='agri_equipment_agency_user')
    authorized_person_name = models.CharField(max_length=120, blank=True, null=True)
    designation = models.CharField(max_length=120, blank=True, null=True)
    phone_number = models.PositiveSmallIntegerField(blank=True, null=True)
    state = models.CharField(choices=STATE_CHOICES, max_length=120, blank=True, null=True)
    district = models.CharField(max_length=120, blank=True, null=True)
    city = models.CharField(max_length=120, blank=True, null=True)
    town = models.CharField(max_length=120, blank=True, null=True)
    Address = models.CharField(max_length=120, blank=True, null=True)
    pin_code = models.PositiveSmallIntegerField(blank=True, null=True)
    company_name = models.CharField(max_length=120, blank=True, null=True)
    license_or_company_registration = models.CharField(max_length=120, blank=True, null=True)
    gst_or_pan = models.DateField(max_length=120, blank=True, null=True)
    upload_agency_picture = models.FileField(upload_to='upload_picture/%Y/%m/%d/', blank=True,
                                       validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'gif'])],
                                       help_text='Max size 2MB, and only pdf are allowed')

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class AgriEquipmentDetail(models.Model):
    agency = models.ForeignKey(AgriEquipmentAgency, on_delete=models.CASCADE, related_name='agri_equipment_agency')
    equipment_name = models.CharField(max_length=120, blank=True, null=True)
    equipment_type = models.CharField(max_length=120, blank=True, null=True)
    quantity = models.PositiveSmallIntegerField(blank=True, null=True)
    state = models.CharField(choices=STATE_CHOICES, max_length=120, blank=True, null=True)
    district = models.CharField(max_length=120, blank=True, null=True)
    city = models.CharField(max_length=120, blank=True, null=True)
    town = models.CharField(max_length=120, blank=True, null=True)
    Address = models.CharField(max_length=120, blank=True, null=True)
    pin_code = models.PositiveSmallIntegerField(blank=True, null=True)
    company_name = models.CharField(max_length=120, blank=True, null=True)
    license_or_company_registration = models.CharField(max_length=120, blank=True, null=True)
    gst_or_pan = models.DateField(max_length=120, blank=True, null=True)
    upload_agency_picture = models.FileField(upload_to='upload_picture/%Y/%m/%d/', blank=True,
                                       validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'gif'])],
                                       help_text='Max size 2MB, and only pdf are allowed')

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Rating(models.Model):
    rating_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rating_by')
    rating_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rating_to')
    rating = models.CharField(max_length=1, blank=True, null=True)
    body = models.CharField(max_length=256, blank=True, null=True)

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class StateWiseDistrict(models.Model):
    state = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=256, blank=True, null=True)

    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.state, self.district)