from django.urls import path
from .import views


urlpatterns = [
    path('', views.kit_list, name='kit_list'),
    path('table/', views.kit_list_for_table, name='kit_list_for_table'),
    #path('create/', views.kit_create, name='kit_create'),
    path('search/', views.kit_search, name='kit_search'),
    path('update/<str:pk>', views.kit_update, name='kit_update'), 
    path('orders/', views.order_list, name='order_list'),
    path('order_update/<str:pk>', views.order_update, name='order_update'),
    path('order_add/', views.order_add, name='order_add'), 
     path('kit_update_by_order/<str:pk>', views.kit_update_by_order, name='order_edit')
    
]