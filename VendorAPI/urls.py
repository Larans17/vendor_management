from django.urls import path,include
from VendorAPI.views.login import *
from VendorAPI.views.vendor import *



urlpatterns = [
    path('login/',LoginAPI.as_view(),name='login'),
    # VENDOR URLS
    path('post-vendor/',VendorPostAPI.as_view(),name='post-vendor'),
    path('get-all-vendorlist/',VendorPostAPI.as_view(),name='get-all-vendorlist'),
    path('vendor/<int:vendorid>/',VendorPutAPI.as_view(),name='vendor'),

    #PURCHASE ORDER URLS
    path('post-purchaseorder/',PuchaseOrderPostAPI.as_view(),name='post-purchaseorder'),
    path('get-all-purchaseorder-list/',PuchaseOrderPostAPI.as_view(),name='get-all-purchaseorder-list'),
    path('purchase-order/<int:poid>/',PurchaseOrderPutAPI.as_view(),name='purchase-order'),

]
