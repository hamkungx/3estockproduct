from django.urls import path
from .views import *

urlpatterns=[
    path('',index,name='index'),  
    path('createproduct',createproducts,name='createproducts'),  
    path('createproductsx',createproductsx,name='createproductsx'),  
    path('createpo/<int:id>',createpox,name='createpox'),   
    path('createpoc',createpoc,name='createpoc'),  
    path('po/<int:id>',poqrs,name='poqrs'), 
    
]