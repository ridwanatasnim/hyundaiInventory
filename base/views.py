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
import math

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
 
@api_view(['GET'])
def kit_list(request):
    kits=Kit.objects.all()
   
    
    p=Paginator(kits,10)
    page_num=request.GET.get('page')
    try:
        page=p.page(page_num)
    except EmptyPage:
        page=p.page(math.ceil(p.count/10))

    if request.method=='GET':
        
        page_count=math.ceil(p.count/10)  
        serializer=KitSerializer(page, many=True)
        return Response({"data": serializer.data, "count": page_count})

@api_view(['GET'])
def kit_list_for_table(request):
    kits = Kit.objects.all()
    p=Paginator(kits,10)
    page_num=request.GET.get('page')
    try:
        page=p.page(page_num)
    except EmptyPage:
        page=p.page(1)
   
    if request.method=='GET':
        page_count=math.ceil(p.count/10)        
        serializer=KitSerializerForTable(page, many=True)
  
        return Response({"data": serializer.data,"count": page_count})




@api_view(['GET'])
def order_list(request):
    orders=Order.objects.all()
    p=Paginator(orders,10)
    page_num=request.GET.get('page')
    try:
        page=p.page(page_num)
    except EmptyPage:
        page=p.page(1)
    if request.method=='GET':
        page_count=math.ceil(p.count/10)
        serializer=OrderSerializer(page, many=True)
        return Response({"data": serializer.data,"count":page_count})




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




@api_view(['POST','GET'])
def kit_search(request):   

    orders=Order.objects.all()
    kits=Kit.objects.all()
    fromDate = request.data.get('fromDate')
    if fromDate==None:
        fromDate="0001-01-01"

    toDate = request.data.get('toDate')
    if toDate==None:
        toDate="9999-01-01"
    
    return Response({'fromDate':fromDate,'toDate':toDate})
    

@api_view(['GET'])
def kit_search_details(request,fromyear,frommonth,fromday,toyear,tomonth,today):
    fromDate=fromyear+"-"+frommonth+"-"+fromday
    toDate=toyear+"-"+tomonth+"-"+today
    orders = Order.objects.distinct().filter(mrr_date__gte=fromDate,mrr_date__lte=toDate)

  
        #kits = Kit.objects.distinct().filter(Order__mrr_date__gte=fromDate,Order__mrr_date__lte=toDate,)

        #if model input is also required->
        #model_input = request.data.get('Model')
        #if model_input==None:
        #    kits = Kit.objects.distinct().filter(Order__mrr_date__gte=fromDate,Order__mrr_date__lte=toDate,)
        #else:
        #    kits = Kit.objects.distinct().filter(Order__mrr_date__gte=fromDate,Order__mrr_date__lte=toDate,)\
        #    .filter(Model=model_input)
    p=Paginator(orders,10)
        #orders_length=len(orders)
        #page_num=math.ceil(orders_length/10)

    page_num=request.GET.get('page')
    try:
        page=p.page(page_num)
    except EmptyPage:
        page=p.page(1)
    serializer=OrderSerializer(page, many=True) 
    return Response({'data':serializer.data, 'count':p.count})


      




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


            mrr_date = request.data.get('mrr_date')
            if mrr_date ==None:
                mrr_date=kit_instance.Order.mrr_date


            kit_instance.Order.mrr_date=mrr_date
            kit_instance.Order.save()
            order=kit_instance.Order
            
            kit_instance.save()
              
            
            mrr_no = request.data.get('mrr_no')
            if mrr_no==None:
                 mrr_no=kit_instance.Order.mrr_no



            try:
                order = Order.objects.get(mrr_no=mrr_no)

            except Order.DoesNotExist:
                order = None

            if order==None:
               kit_instance.Order.mrr_no=mrr_no
               kit_instance.Order.save()
               order=kit_instance.Order



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



@api_view(['GET','PUT'])
def kit_update_by_order(request,pk):

    order_instance=Order.objects.get(id=pk)
    kit_list=Kit.objects.filter(Order=order_instance)
    kits = request.data.get('kits')
    mrr_no = request.data.get('mrr_no')
    mrr_date = request.data.get('mrr_date')



    if request.method=='GET':
        serializer=OrderSerializer(order_instance, many=False)
        return Response(serializer.data)
    

    if request.method=='PUT':
        
        if mrr_date ==None:
            mrr_date=order_instance.mrr_date
        order_instance.mrr_date=mrr_date
            
                
            
        if mrr_no==None:
            mrr_no=order_instance.mrr_no
        order_instance.mrr_no=mrr_no

        order_instance.save()
            
        
        for kit in kits:
            kit_instance=Kit.objects.get(id=kit["id"])
            serializer=KitSerializer(kit_instance, data=kit)
            kit_instance.save()
            if serializer.is_valid():
                serializer.save()
            else:
                return Response ("invalid data format")    

        serializer=OrderSerializer(order_instance, many=False)
    return Response( serializer.data)
   




@api_view(['POST'])
def order_add(request):
    if request.method=='POST':
        serializer=OrderSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
        
