from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from .models import *
import qrcode
import qrcode.image.svg
from io import BytesIO
# Create your views here.
def index(request):
    if 'po' in request.GET:
        po=request.GET['po']
        latest=Stockproduct.objects.filter(NameProduct__icontains=po)
        if po =="":
            messages.success(request,"โปรดป้อนข้อมูลสินค้า หรือรหัสสินค้า")
            return redirect("index")
            
    else:
        latest = Stockproduct.objects.all()
    return render(request,"frontend/index.html",{'latest':latest})

def createproducts(request):
    return render(request,"frontend/createproduct.html")

def createproductsx(request):
    
    if request.method == "POST":
            #รับค่าฟอร์
        NameProduct = request.POST['NameProduct']
        productID = request.POST['productID']

        if NameProduct == "" or productID =="":
            messages.info(request,"กรุณาป้อนข้อมูล")
            return redirect("createproducts")
        else:
            messages.info(request,"บันทึกข้อมูลเรียบร้อย")
            admission = Stockproduct(NameProduct=NameProduct,productID=productID)
            admission.save()
            return redirect("createproducts")

def createpox(request,id):
    sblog = Stockproduct.objects.get(id=id)
    sblog.save()
    return render(request,"frontend/createpo.html",{"blog":sblog})

def createpoc(request):
    if request.method == "POST":
        NameProduct = request.POST["NameProduct"]
        productID = request.POST["productID"]
        createPo = request.POST['createPo']

        if createPo  == "" :
            messages.success(request,"กรุณากรอกหมายเลข PO")
            return redirect("index")
        else:
            messages.success(request,"บันทึกข้อมูลเรียบร้อย")
            admission = CreatePo(createPo=createPo,productID=productID,NameProduct=NameProduct)
            admission.save()
            return redirect("poqrs")

def poqrs(request):
    sblog=CreatePo.objects.all().order_by('-pk')[:1]
    if request.method=="POST":
      qr_text=request.POST['qr_text']
      QrCode.objects.create(qr_text=qr_text)

    qr_code=QrCode.objects.all()
    return render(request,"frontend/poqr.html",{"blogs":sblog,'qr_code':qr_code})


