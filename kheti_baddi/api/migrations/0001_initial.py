# Generated by Django 2.1.5 on 2020-07-18 11:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_1', models.CharField(blank=True, max_length=250, null=True)),
                ('address_2', models.CharField(blank=True, max_length=250, null=True)),
                ('pin_code', models.CharField(blank=True, max_length=250, null=True)),
                ('state', models.CharField(blank=True, choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh ', 'Arunachal Pradesh '), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir ', 'Jammu and Kashmir '), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal'), ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'), ('Chandigarh', 'Chandigarh'), ('Dadra and Nagar Haveli', 'Dadra and Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Lakshadweep', 'Lakshadweep'), ('National Capital Territory of Delhi', 'National Capital Territory of Delhi'), ('Puducherry', 'Puducherry')], max_length=250, null=True)),
                ('district', models.CharField(blank=True, max_length=250, null=True)),
                ('tehsil', models.CharField(blank=True, max_length=250, null=True)),
                ('active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AgriEquipmentAgency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorized_person_name', models.CharField(blank=True, max_length=120, null=True)),
                ('designation', models.CharField(blank=True, max_length=120, null=True)),
                ('phone_number', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('state', models.CharField(blank=True, choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh ', 'Arunachal Pradesh '), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir ', 'Jammu and Kashmir '), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal'), ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'), ('Chandigarh', 'Chandigarh'), ('Dadra and Nagar Haveli', 'Dadra and Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Lakshadweep', 'Lakshadweep'), ('National Capital Territory of Delhi', 'National Capital Territory of Delhi'), ('Puducherry', 'Puducherry')], max_length=120, null=True)),
                ('district', models.CharField(blank=True, max_length=120, null=True)),
                ('city', models.CharField(blank=True, max_length=120, null=True)),
                ('town', models.CharField(blank=True, max_length=120, null=True)),
                ('Address', models.CharField(blank=True, max_length=120, null=True)),
                ('pin_code', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('company_name', models.CharField(blank=True, max_length=120, null=True)),
                ('license_or_company_registration', models.CharField(blank=True, max_length=120, null=True)),
                ('gst_or_pan', models.DateField(blank=True, max_length=120, null=True)),
                ('upload_agency_picture', models.FileField(blank=True, help_text='Max size 2MB, and only pdf are allowed', upload_to='upload_picture/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'gif'])])),
                ('active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AgriEquipmentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_name', models.CharField(blank=True, max_length=120, null=True)),
                ('equipment_type', models.CharField(blank=True, max_length=120, null=True)),
                ('quantity', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('state', models.CharField(blank=True, choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh ', 'Arunachal Pradesh '), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir ', 'Jammu and Kashmir '), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal'), ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'), ('Chandigarh', 'Chandigarh'), ('Dadra and Nagar Haveli', 'Dadra and Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Lakshadweep', 'Lakshadweep'), ('National Capital Territory of Delhi', 'National Capital Territory of Delhi'), ('Puducherry', 'Puducherry')], max_length=120, null=True)),
                ('district', models.CharField(blank=True, max_length=120, null=True)),
                ('city', models.CharField(blank=True, max_length=120, null=True)),
                ('town', models.CharField(blank=True, max_length=120, null=True)),
                ('Address', models.CharField(blank=True, max_length=120, null=True)),
                ('pin_code', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('company_name', models.CharField(blank=True, max_length=120, null=True)),
                ('license_or_company_registration', models.CharField(blank=True, max_length=120, null=True)),
                ('gst_or_pan', models.DateField(blank=True, max_length=120, null=True)),
                ('upload_agency_picture', models.FileField(blank=True, help_text='Max size 2MB, and only pdf are allowed', upload_to='upload_picture/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'gif'])])),
                ('active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agri_equipment_agency', to='api.AgriEquipmentAgency')),
            ],
        ),
        migrations.CreateModel(
            name='BankDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_holder_name', models.CharField(blank=True, max_length=120, null=True)),
                ('bank_account_number', models.CharField(blank=True, max_length=120, null=True)),
                ('ifsc_code', models.CharField(blank=True, max_length=120, null=True)),
                ('upload_passbook', models.FileField(blank=True, help_text='Max size 2MB, and only pdf are allowed', null=True, upload_to='passbook/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'png', 'jpg', 'jpeg'])])),
                ('active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BidDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commodity_name', models.CharField(blank=True, max_length=120, null=True)),
                ('buyer_name', models.CharField(blank=True, max_length=255, null=True)),
                ('quantity', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('bid_price', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('total_amount', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('expected_pickup_date', models.DateField(blank=True, max_length=120, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('accept_bid', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BidStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('best_bid_matched_price', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('Initiated', 'Initiated'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('Partially Completed', 'Partially Completed'), ('Other', 'Other')], default='Completed', max_length=50, null=True)),
                ('active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommodityBuyerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('mobile_no', models.CharField(blank=True, max_length=250, null=True)),
                ('alternate_mobile_no', models.CharField(blank=True, max_length=250, null=True)),
                ('license_no', models.CharField(blank=True, max_length=250, null=True)),
                ('company_name', models.CharField(blank=True, max_length=250, null=True)),
                ('company_reg', models.CharField(blank=True, max_length=250, null=True)),
                ('active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommodityDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('quantity', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('auction', models.DateTimeField(blank=True, null=True)),
                ('base_price', models.FloatField(blank=True, default=0, null=True)),
                ('average_bid_price', models.FloatField(blank=True, default=0, null=True)),
                ('bid_count', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('status', models.CharField(blank=True, choices=[('Open', 'Open'), ('Closed', 'Closed')], default='Open', max_length=50, null=True)),
                ('active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommodityInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grain_name', models.CharField(blank=True, max_length=120, null=True)),
                ('category', models.CharField(blank=True, choices=[('FOOD GRAINS/ CEREALS', 'FOOD GRAINS/ CEREALS'), ('OILSEEDS', 'OILSEEDS'), ('FRUITS', 'FRUITS'), ('VEGETABLES', 'VEGETABLES'), ('SPICES', 'SPICES'), ('MISC', 'MISC')], max_length=120, null=True)),
                ('upload_picture', models.FileField(blank=True, help_text='Max size 2MB, and only pdf are allowed', upload_to='commodity_picture/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'gif'])])),
                ('active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommoditySellerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('alternate_mobile_no_1', models.CharField(blank=True, max_length=250, null=True)),
                ('alternate_mobile_no_2', models.CharField(blank=True, max_length=250, null=True)),
                ('license_no', models.CharField(blank=True, max_length=250, null=True)),
                ('company_name', models.CharField(blank=True, max_length=250, null=True)),
                ('company_reg', models.CharField(blank=True, max_length=250, null=True)),
                ('active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommodityTransportProviderProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('alternate_mobile_no_1', models.CharField(blank=True, max_length=250, null=True)),
                ('alternate_mobile_no_2', models.CharField(blank=True, max_length=250, null=True)),
                ('license_no', models.CharField(blank=True, max_length=250, null=True)),
                ('company_name', models.CharField(blank=True, max_length=250, null=True)),
                ('company_reg', models.CharField(blank=True, max_length=250, null=True)),
                ('landline_no', models.CharField(blank=True, max_length=250, null=True)),
                ('year_of_establishment', models.CharField(blank=True, max_length=250, null=True)),
                ('gst', models.CharField(blank=True, max_length=250, null=True)),
                ('vehicle_image', models.FileField(blank=True, help_text='Max size 2MB, and only pdf are allowed', upload_to='ctpp/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'gif'])])),
                ('active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmailActivation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('key', models.CharField(blank=True, max_length=120, null=True)),
                ('activated', models.BooleanField(default=False)),
                ('forced_expired', models.BooleanField(default=False)),
                ('expires', models.IntegerField(default=7)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='KYCDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_id_type', models.CharField(blank=True, choices=[('ADHAR CARD', 'ADHAR CARD'), ('PAN CARD', 'PAN CARD'), ('VOTER CARD', 'VOTER CARD'), ('OTHERS', 'OTHERS')], max_length=250, null=True)),
                ('id_number', models.CharField(blank=True, max_length=250, null=True)),
                ('upload_id', models.FileField(blank=True, help_text='Max size 2MB, and only pdf are allowed', null=True, upload_to='kyc/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'gif'])])),
                ('active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Logistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(blank=True, max_length=120, null=True)),
                ('destination', models.CharField(blank=True, max_length=120, null=True)),
                ('distance', models.CharField(blank=True, max_length=120, null=True)),
                ('estimate_charges', models.FloatField(blank=True, null=True)),
                ('total_charges', models.FloatField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('PENDING', 'PENDING'), ('INITIATED', 'INITIATED'), ('COMPLETED', 'COMPLETED'), ('OTHERS', 'OTHERS')], default='PENDING', max_length=120, null=True)),
                ('active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MandiAdministrator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=120, null=True)),
                ('designation', models.CharField(blank=True, max_length=120, null=True)),
                ('state', models.CharField(blank=True, max_length=120, null=True)),
                ('district', models.CharField(blank=True, max_length=120, null=True)),
                ('city', models.CharField(blank=True, max_length=120, null=True)),
                ('town', models.CharField(blank=True, max_length=120, null=True)),
                ('Address', models.CharField(blank=True, max_length=120, null=True)),
                ('pin_code', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('mandi_name', models.CharField(blank=True, max_length=120, null=True)),
                ('upload_mandi_picture', models.FileField(blank=True, help_text='Max size 2MB, and only pdf are allowed', upload_to='mandi_picture/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'gif'])])),
                ('active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MandiAgent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=120, null=True)),
                ('designation', models.CharField(blank=True, max_length=120, null=True)),
                ('state', models.CharField(blank=True, choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh ', 'Arunachal Pradesh '), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir ', 'Jammu and Kashmir '), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal'), ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'), ('Chandigarh', 'Chandigarh'), ('Dadra and Nagar Haveli', 'Dadra and Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Lakshadweep', 'Lakshadweep'), ('National Capital Territory of Delhi', 'National Capital Territory of Delhi'), ('Puducherry', 'Puducherry')], max_length=120, null=True)),
                ('district', models.CharField(blank=True, max_length=120, null=True)),
                ('city', models.CharField(blank=True, max_length=120, null=True)),
                ('town', models.CharField(blank=True, max_length=120, null=True)),
                ('Address', models.CharField(blank=True, max_length=120, null=True)),
                ('pin_code', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('company_name', models.CharField(blank=True, max_length=120, null=True)),
                ('license_or_company_registration', models.CharField(blank=True, max_length=120, null=True)),
                ('gst_or_pan', models.DateField(blank=True, max_length=120, null=True)),
                ('upload_picture', models.FileField(blank=True, help_text='Max size 2MB, and only pdf are allowed', upload_to='upload_picture/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'gif'])])),
                ('active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MandiTrader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=120, null=True)),
                ('designation', models.CharField(blank=True, max_length=120, null=True)),
                ('state', models.CharField(blank=True, choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh ', 'Arunachal Pradesh '), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir ', 'Jammu and Kashmir '), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal'), ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'), ('Chandigarh', 'Chandigarh'), ('Dadra and Nagar Haveli', 'Dadra and Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Lakshadweep', 'Lakshadweep'), ('National Capital Territory of Delhi', 'National Capital Territory of Delhi'), ('Puducherry', 'Puducherry')], max_length=120, null=True)),
                ('district', models.CharField(blank=True, max_length=120, null=True)),
                ('city', models.CharField(blank=True, max_length=120, null=True)),
                ('town', models.CharField(blank=True, max_length=120, null=True)),
                ('Address', models.CharField(blank=True, max_length=120, null=True)),
                ('pin_code', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('company_name', models.CharField(blank=True, max_length=120, null=True)),
                ('license_or_company_registration', models.CharField(blank=True, max_length=120, null=True)),
                ('gst_or_pan', models.CharField(blank=True, max_length=120, null=True)),
                ('registration_level', models.CharField(blank=True, max_length=120, null=True)),
                ('registered_with_mandi', models.CharField(blank=True, max_length=120, null=True)),
                ('upload_picture', models.FileField(blank=True, help_text='Max size 2MB, and only pdf are allowed', upload_to='upload_picture/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'gif'])])),
                ('active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(blank=True, max_length=1, null=True)),
                ('body', models.CharField(blank=True, max_length=256, null=True)),
                ('active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='StateWiseDistrict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('district', models.CharField(blank=True, max_length=256, null=True)),
                ('active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True, validators=[django.core.validators.EmailValidator])),
                ('mobile', models.CharField(db_index=True, max_length=10, unique=True, validators=[django.core.validators.RegexValidator(message='Enter a valid phone number', regex='^\\+?1?\\d{9,15}$')])),
                ('full_name', models.CharField(blank=True, max_length=250, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Unknown', 'Unknown'), ('Other', 'Other')], max_length=120, null=True)),
                ('commodity_seller', models.BooleanField(default=False)),
                ('commodity_buyer', models.BooleanField(default=False)),
                ('commodity_transport_provider', models.BooleanField(default=False)),
                ('mandi_administrator', models.BooleanField(default=False)),
                ('manager', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WarehouseDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warehouse_name', models.CharField(blank=True, max_length=120, null=True)),
                ('authorized_person_name', models.CharField(blank=True, max_length=120, null=True)),
                ('designation', models.CharField(blank=True, max_length=120, null=True)),
                ('phone_number', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('state', models.CharField(blank=True, choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh ', 'Arunachal Pradesh '), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir ', 'Jammu and Kashmir '), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal'), ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'), ('Chandigarh', 'Chandigarh'), ('Dadra and Nagar Haveli', 'Dadra and Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Lakshadweep', 'Lakshadweep'), ('National Capital Territory of Delhi', 'National Capital Territory of Delhi'), ('Puducherry', 'Puducherry')], max_length=120, null=True)),
                ('district', models.CharField(blank=True, max_length=120, null=True)),
                ('city', models.CharField(blank=True, max_length=120, null=True)),
                ('town', models.CharField(blank=True, max_length=120, null=True)),
                ('Address', models.CharField(blank=True, max_length=120, null=True)),
                ('pin_code', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('company_name', models.CharField(blank=True, max_length=120, null=True)),
                ('license_or_company_registration', models.CharField(blank=True, max_length=120, null=True)),
                ('gst_or_pan', models.DateField(blank=True, max_length=120, null=True)),
                ('upload_warehouse_picture', models.FileField(blank=True, help_text='Max size 2MB, and only pdf are allowed', upload_to='upload_picture/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'gif'])])),
                ('active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='warehouse_user', to='api.User')),
            ],
        ),
        migrations.AddField(
            model_name='rating',
            name='rating_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating_by', to='api.User'),
        ),
        migrations.AddField(
            model_name='rating',
            name='rating_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating_to', to='api.User'),
        ),
        migrations.AddField(
            model_name='manditrader',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mandi_traders_user', to='api.User'),
        ),
        migrations.AddField(
            model_name='mandiagent',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mandi_agent_user', to='api.User'),
        ),
        migrations.AddField(
            model_name='mandiadministrator',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mandi_administrator_user', to='api.User'),
        ),
        migrations.AddField(
            model_name='logistic',
            name='commodity_buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='c_buyer', to='api.User'),
        ),
        migrations.AddField(
            model_name='logistic',
            name='commodity_seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='c_seller', to='api.User'),
        ),
        migrations.AddField(
            model_name='logistic',
            name='commodity_transport_provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commodity_tp', to='api.User'),
        ),
        migrations.AddField(
            model_name='kycdetail',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='kyc_detail', to='api.User'),
        ),
        migrations.AddField(
            model_name='emailactivation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User'),
        ),
        migrations.AddField(
            model_name='commoditytransportproviderprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='commodity_transport_provider_profile', to='api.User'),
        ),
        migrations.AddField(
            model_name='commoditysellerprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='commodity_seller_profile', to='api.User'),
        ),
        migrations.AddField(
            model_name='commoditydetail',
            name='grain_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.CommodityInfo'),
        ),
        migrations.AddField(
            model_name='commoditydetail',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commodity_detail_user', to='api.User'),
        ),
        migrations.AddField(
            model_name='commoditybuyerprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='commodity_buyer_profile', to='api.User'),
        ),
        migrations.AddField(
            model_name='bidstatus',
            name='bid_detail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bid_status', to='api.User'),
        ),
        migrations.AddField(
            model_name='bidstatus',
            name='commodity_detail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bid_on', to='api.CommodityDetail'),
        ),
        migrations.AddField(
            model_name='biddetail',
            name='commodity_detail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commodity_detail', to='api.CommodityDetail'),
        ),
        migrations.AddField(
            model_name='biddetail',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bid_agent_user', to='api.User'),
        ),
        migrations.AddField(
            model_name='bankdetail',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank_detail_user', to='api.User'),
        ),
        migrations.AddField(
            model_name='agriequipmentagency',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agri_equipment_agency_user', to='api.User'),
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_address', to='api.User'),
        ),
    ]