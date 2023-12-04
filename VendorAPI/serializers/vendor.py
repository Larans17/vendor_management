from VendorAPI.models import *
from rest_framework import serializers
from VendorAPI.utils import *



class PostVendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['vendorid','name','vendor_code','contact_details','address','on_time_delivery_rate',
                  'quality_rating_avg','average_response_time','fulfillment_rate']
        

    def validate_name(self, value):
        if getAllObjectWithFilter(Vendor,{'name':value}).exists():
            raise serializers.ValidationError("Vendor name already exists")
        return value
    

class UpdateVendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['vendorid','name','vendor_code','contact_details','address','on_time_delivery_rate',
                  'quality_rating_avg','average_response_time','fulfillment_rate']
        

    def validate_name(self, value):
        vendorid = self.context.get('vendorid')
        existing_vendor_with_same_name = Vendor.objects.exclude(vendorid=vendorid).filter(name=value).exists()
        if existing_vendor_with_same_name:
            raise serializers.ValidationError("Vendor name already exists")
        return value
    
class GetAllVendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'


class PostPurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ['poid','po_number','vendor','order_date','delivery_date','items','quantity',
                  'status','quality_rating','issue_date','acknowledgment_date']
        
class GetPurchaseOrderSerializer(serializers.ModelSerializer):
    vendor = serializers.StringRelatedField(source="vendor.name")
    status = serializers.StringRelatedField(source="status.status_name")
    class Meta:
        model = PurchaseOrder
        fields = ['poid','po_number','vendor','order_date','delivery_date','items','quantity',
                  'status','quality_rating','issue_date','acknowledgment_date']
       