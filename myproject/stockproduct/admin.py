from django.contrib import admin
from .models import *
# Register your models here.
class StockproductAdmin(admin.ModelAdmin):
    list_display = ('NameProduct','productID','addtime')
admin.site.register(Stockproduct,StockproductAdmin)