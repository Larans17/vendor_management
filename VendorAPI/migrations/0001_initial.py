# Generated by Django 4.2.7 on 2023-12-03 13:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('statusid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('status_name', models.CharField(max_length=100)),
                ('status_color', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('vendorid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('vendor_code', models.CharField(max_length=10, unique=True)),
                ('contact_details', models.TextField()),
                ('address', models.TextField()),
                ('on_time_delivery_rate', models.FloatField(default=0)),
                ('quality_rating_avg', models.FloatField(default=0)),
                ('average_response_time', models.FloatField(default=0)),
                ('fulfillment_rate', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_name', models.CharField(blank=True, error_messages={'unique': 'Username already exists'}, max_length=100, null=True, unique=True)),
                ('display_name', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_super_admin', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usercreate_userid', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='userdelete_userid', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='userupdate_userid', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('poid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('po_number', models.CharField(max_length=10, unique=True)),
                ('order_date', models.DateTimeField(auto_now=True)),
                ('delivery_date', models.DateTimeField()),
                ('items', models.JSONField()),
                ('quantity', models.IntegerField(default=0)),
                ('quality_rating', models.FloatField(blank=True, null=True)),
                ('issue_date', models.DateTimeField()),
                ('acknowledgment_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='po_statusid', to='VendorAPI.status')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='po_vendorid', to='VendorAPI.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('logid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('transaction_name', models.CharField(max_length=500)),
                ('mode', models.CharField(max_length=100)),
                ('log_message', models.TextField()),
                ('ip_address', models.CharField(blank=True, max_length=100, null=True)),
                ('system_name', models.CharField(blank=True, max_length=100, null=True)),
                ('log_date', models.DateTimeField(auto_now=True)),
                ('userid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='log_user_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalPerformance',
            fields=[
                ('performanceid', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('on_time_delivery_rate', models.FloatField(default=0)),
                ('quality_rating_avg', models.FloatField(default=0)),
                ('average_response_time', models.FloatField(default=0)),
                ('fulfillment_rate', models.FloatField(default=0)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='performance_vendorid', to='VendorAPI.vendor')),
            ],
        ),
    ]
