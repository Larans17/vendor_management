from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from VendorAPI.models import PurchaseOrder, Vendor
from VendorAPI.utils import *

@receiver(post_save, sender=PurchaseOrder)
@receiver(post_delete, sender=PurchaseOrder)
def update_vendor_metrics_on_po_change(sender, instance, **kwargs):
    update_vendor_performance_metrics(instance.vendor)