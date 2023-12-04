from VendorAPI.common.bulk_creation import *
from VendorAPI.models import *

def callbulkCreation():
    if Status.objects.all().exists() == False:
        StatusCreation(),

