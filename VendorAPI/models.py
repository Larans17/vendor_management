from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from VendorAPI.common.api_response_message import *

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, user_name, password=None, **kwargs):
        user = self.model(user_name=user_name, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, user_name, password=None, **kwargs):
        user = self.create_user(
            user_name=user_name,
            password=password,
            is_super_admin=True,
            is_active=True,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    user_name = models.CharField(
        max_length=100,
        unique=True,
        null=True,
        blank=True,
        error_messages={"unique": USER_ALREADY_EXISTS},
    )
    display_name = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_super_admin = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        "User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="usercreate_userid",
    )
    created_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        "User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="userupdate_userid",
    )
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_by = models.ForeignKey(
        "User",
        on_delete=models.SET_NULL,
        related_name="userdelete_userid",
        null=True,
        blank=True,
    )
    deleted_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "user_name"
    REQUIRED_FIELDS = ["email"]

    def has_perm(self, perm, obj=None):
        return self.is_super_admin

    def has_module_perms(self, app_label):
        return self.is_super_admin

    def __str__(self):
        return self.user_name


class Logs(models.Model):
    logid = models.BigAutoField(primary_key=True, editable=False)
    transaction_name = models.CharField(max_length=500)
    mode = models.CharField(max_length=100)
    log_message = models.TextField()
    userid = models.ForeignKey(
        "User",
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        related_name="log_user_id",
    )
    ip_address = models.CharField(max_length=100, null=True, blank=True)
    system_name = models.CharField(max_length=100, null=True, blank=True)
    log_date = models.DateTimeField(auto_now=True)



class Status(models.Model):
    statusid = models.BigAutoField(primary_key=True,editable=False)
    status_name = models.CharField(max_length=100)
    status_color = models.CharField(max_length=100)


class Vendor(models.Model):
    vendorid = models.BigAutoField(primary_key=True,editable=False)
    name = models.CharField(max_length=500)
    vendor_code = models.CharField(unique=True,max_length=10)
    contact_details = models.TextField()
    address = models.TextField()
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

class PurchaseOrder(models.Model):
    poid = models.BigAutoField(primary_key=True,editable=False)
    po_number = models.CharField(max_length=10,unique=True)
    vendor = models.ForeignKey("Vendor",
        on_delete=models.RESTRICT,
        related_name="po_vendorid")
    order_date = models.DateTimeField(auto_now=True)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField(default=0)
    status = models.ForeignKey("Status",
        on_delete=models.RESTRICT,
        related_name="po_statusid")
    quality_rating = models.FloatField(null=True,blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True,blank=True)
    


# class HistoricalPerformance(models.Model):
#     performanceid = models.BigAutoField(primary_key=True,editable=True)
#     vendor = models.ForeignKey("Vendor",
#         on_delete=models.RESTRICT,
#         related_name="performance_vendorid")
#     date = models.DateTimeField(auto_now=True)
#     on_time_delivery_rate = models.FloatField(default=0)
#     quality_rating_avg = models.FloatField(default=0)
#     average_response_time = models.FloatField(default=0)
#     fulfillment_rate = models.FloatField(default=0)

