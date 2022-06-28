from django.urls import path,re_path
from .import views


urlpatterns = [
    path('', views.kit_list, name='kit_list'),
    path('table/', views.kit_list_for_table, name='kit_list_for_table'),
    #path('create/', views.kit_create, name='kit_create'),
    path('search/', views.kit_search, name='kit_search'),
    re_path(r'^search/(?P<fromyear>[0-9]{4})/(?P<frommonth>[0-9]{2})/(?P<fromday>[0-9]{2})/(?P<toyear>[0-9]{4})/(?P<tomonth>[0-9]{2})/(?P<today>[0-9]{2})/$', views.kit_search_details, name='kit_search_details'),
    path('update/<str:pk>', views.kit_update, name='kit_update'), 
    path('orders/', views.order_list, name='order_list'),
    path('order_update/<str:pk>', views.order_update, name='order_update'),
    path('order_add/', views.order_add, name='order_add'), 
    path('kit_update_by_order/<str:pk>', views.kit_update_by_order, name='order_edit')
    
]