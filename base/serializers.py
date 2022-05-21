from rest_framework import serializers
from .models import *

    
class OrderSerializerForTable(serializers.ModelSerializer):
    id= serializers.IntegerField(required=False)
    
    class Meta:
        model = Order
        fields=[
            "id",          
            "mrr_date",
            "mrr_no",

        ]
     

class KitSerializerForTable(serializers.ModelSerializer):

    Order=OrderSerializerForTable(many=False)
   
    id= serializers.IntegerField(required=False)
    
    class Meta:
        model = Kit
        fields=[
            "id",
            "Model",
            "Body",
            "Lot_No",
            "Variant",
            "Order"
            
        ]



class KitSerializerForUpdate(serializers.ModelSerializer):
    Order=OrderSerializerForTable(many=False)

    id= serializers.IntegerField(required=False)
    
    class Meta:
        model = Kit
        fields=[
            "id",
            "Model",
            "Body",
            "Lot_No",
            "Variant",
            "Order"

        ]
      
    # def update(self, instance, data):
    #     instance.Status=data.get('Status', instance.Status)
    #     instance.Model=data.get('Model', instance.Model)
    #     instance.Body=data.get('Body', instance.Body)
    #     instance.Lot_No=data.get('Lot_No', instance.Lot_No)
    #     instance.Variant=data.get('Variant', instance.Variant)
    #     instance.Fuel=data.get('Fuel', instance.Fuel)
     
    #     Order_data = data.pop('Order')
    #     if Order_data != None:
    #         order=Order.objects.create(**Order_data)
    #         instance.Order=order 
    #         order.save()

    #     instance.save()
    #     return instance
          


class KitSerializer(serializers.ModelSerializer):
    id= serializers.IntegerField(required=False)
    class Meta:
        model = Kit
        fields=[
            "id",
            "Model",
            "Body",
            "Lot_No",
            "Variant"
        ]
            
 #rdvttbfvu   
class OrderSerializer(serializers.ModelSerializer):
    id= serializers.IntegerField(required=False)
   
    kits=KitSerializer(many=True)

    class Meta:
        model = Order
        fields=[
            "id",
            "mrr_date",
            "mrr_no",
            "kits",
        ]

    def create(self, validated_data):

        Kits=validated_data.pop('kits')
        order=Order.objects.create(**validated_data)
        for kit in Kits:
            Kit.objects.create(**kit,Order=order)
        return order








        