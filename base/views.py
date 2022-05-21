from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter

from django.http import HttpResponse
from .models import *
from .forms import *
from .serializers import *
from .filters import KitFilter

from datetime import date

# Create your views here.
 
@api_view(['GET'])
def kit_list(request):
    kits=Kit.objects.all()
    if request.method=='GET':
        
        serializer=KitSerializer(kits, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def kit_list_for_table(request):
    kits = Kit.objects.all()
   
    if request.method=='GET':
        
        serializer=KitSerializerForTable(kits, many=True)
        
        #paginator = Paginator(data,5)
        #page_number = request.GET.get('page')
        #page_obj = paginator.get_page(page_number)

        return Response(serializer.data)




@api_view(['GET'])
def order_list(request):
    orders=Order.objects.all()
    if request.method=='GET':
        
        serializer=OrderSerializer(orders, many=True)
        return Response(serializer.data)




@api_view(['POST'])
def kit_create(request):
    if request.method=='POST':
        serializer=KitSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
        


# @api_view(['POST'])
# def kit_search_old(request):
#     kits=Kit.objects.all()
#     if request.method=='POST':
#         myFilter= KitFilter(request.data, queryset=kits)
       
#         kits=myFilter.qs 
        
#         serializer=KitSerializerForTable(kits, many=True)      
         
#         return Response(serializer.data)




@api_view(['POST'])
def kit_search(request):   

    orders=Order.objects.all()
    kits=Kit.objects.all()
    
    
    fromDate = request.data.get('fromDate')
    if fromDate==None:
        fromDate="0001-01-01"

    toDate = request.data.get('toDate')
    if toDate==None:
        toDate="9999-01-01"

    model_input = request.data.get('Model')
    if model_input==None:
        kits = Kit.objects.distinct().filter(Order__mrr_date__gte=fromDate,Order__mrr_date__lte=toDate,)
      
    else:
        kits = Kit.objects.distinct().filter(Order__mrr_date__gte=fromDate,Order__mrr_date__lte=toDate,)\
        .filter(Model=model_input)

    
    serializer=KitSerializerForTable(kits, many=True) 
   
    return Response(serializer.data)

 

# @api_view(['GET','PUT','DELETE'])
# def kit_update_old(request,pk):
#     kit_instance=Kit.objects.get(id=pk)
  
#     if request.method=='GET':
        
#         serializer=KitSerializerForUpdate(kit_instance, many=False)
#         return Response(serializer.data)
    
#     if request.method=='PUT':
            
#             serializer=KitSerializerForUpdate(kit_instance, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             else:
#                 return Response(serializer.errors)

                    
            
#     if request.method=='DELETE':
        
#         kit_instance.delete()
#         return Response('mmr_detail deleted')
       


@api_view(['GET','PUT','DELETE'])
def kit_update(request,pk):
    kit_instance=Kit.objects.get(id=pk)
  
    if request.method=='GET':
        
        serializer=KitSerializerForUpdate(kit_instance, many=False)
        return Response(serializer.data)
    
    if request.method=='PUT':
            
            kit_model = request.data.get('Model')
            if kit_model==None:
                kit__model=kit_instance.Model
            else:
                kit_instance.Model=kit_model



            kit_body = request.data.get('Body')
            if kit_body==None:
                kit__body=kit_instance.Body
            else:
                kit_instance.Body=kit_body  


            kit_Lot_No = request.data.get('Lot_No')
            if kit_Lot_No==None:
                kit__Lot_No=kit_instance.Lot_No
            else:
                kit_instance.Lot_No=kit_Lot_No



            kit_Variant = request.data.get('Variant')
            if kit_Variant==None:
                kit__Variant=kit_instance.Variant
            else:
                kit_instance.Variant=kit_Variant     



            kit_Order = request.data.get('Order')
            if kit_Order==None:
                kit__Order=kit_instance.Order
            else:
                kit_instance.Order=kit_Order   


            mrr_date = request.data.get('mrr_date')
            mrr_no = request.data.get('mrr_no')
            
    
            order = Order.objects.get(mrr_no=mrr_no)

            if order==None: 
                order=Order.objects.create(mrr_date=mrr_date, mrr_no=mrr_no)

            kit_instance.Order=order 
            order.save()
            kit_instance.save()
            serializer=KitSerializerForUpdate(kit_instance, many=False)
            return Response(serializer.data)    

    if request.method=='DELETE':
        
        kit_instance.delete()
        return Response('mmr_detail deleted')




@api_view(['GET','PUT','DELETE'])
def order_update(request,pk):
    order_instance=Order.objects.get(id=pk)
  
    if request.method=='GET':
        
        serializer=OrderSerializer(order_instance, many=False)
        return Response(serializer.data)
    
    if request.method=='PUT':
            
            serializer=OrderSerializerForTable(order_instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)

                    
            
    if request.method=='DELETE':
        
        order_instance.delete()
        return redirect('/orders')



@api_view(['POST'])
def order_add(request):
    if request.method=='POST':
        serializer=OrderSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
        
