from django.urls import path
from .views import *

urlpatterns=[
    path('',index,name='index'),  
    path('createproduct',createproducts,name='createproducts'),  
    path('createproductsx',createproductsx,name='createproductsx'),  
    
]