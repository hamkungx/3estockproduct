from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from .models import *
# Create your views here.
def index(request):
    if 'po' in request.GET:
        po=request.GET['po']
        latest=Stockproduct.objects.filter(NameProduct__icontains=po)
    else:
        latest = Stockproduct.objects.all()
    return render(request,"frontend/index.html",{'latest':latest})

def createproducts(request):
    return render(request,"frontend/createproduct.html")

def createproductsx(request):
    try:
            request.method == "POST"
            #รับค่าฟอร์
            NameProduct = request.POST['NameProduct']
            productID = request.POST['productID']

            #บันทึกข่าวสาร
            admission = Stockproduct(NameProduct=NameProduct,productID=productID)
            admission.save()

            messages.info(request,"บันทึกข้อมูลเรียบร้อย")
            return redirect("createproducts")
    except:
            return redirect("createproducts")


