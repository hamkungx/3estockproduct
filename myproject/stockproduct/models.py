from io import BytesIO
from django.db import models
from django.core.files import File
import qrcode
from PIL import Image,ImageDraw
import random

# Create your models here.
class Stockproduct(models.Model):
    productID = models.CharField(max_length=100)
    NameProduct = models.CharField(max_length=100)
    addtime = models.DateTimeField(auto_now_add=True)
    code = models.ImageField(blank=True,upload_to='code')

    def __str__(self) -> str:
        return self.productID

    def save(self,*args,**kwargs):
        qr_image = qrcode.make(self.productID)
        qr_offset = Image.new('RGB',(330,310),'white')
        qr_offset.paste(qr_image)
        files_name = f'{self.productID}-{self.id}qr.png'
        stream = BytesIO()
        qr_offset.save(stream,'PNG')
        self.code.save(files_name,File(stream),save=False)
        qr_offset.close()
        super().save(*args, **kwargs)

class CreatePo(models.Model):
    NameProduct = models.CharField(max_length=100)
    productID = models.CharField(max_length=100)
    createPo = models.CharField(max_length=100)
    addtime = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.createPo

class QrCode(models.Model):
   url=models.URLField()
   image=models.ImageField(upload_to='qrcode',blank=True)

   def save(self,*args,**kwargs):
      qrcode_img=qrcode.make(self.url)
      canvas=Image.new("RGB", (300,300),"white")
      draw=ImageDraw.Draw(canvas)
      canvas.paste(qrcode_img)
      buffer=BytesIO()
      canvas.save(buffer,"PNG")
      self.image.save(f'image{random.randint(0,9999)}',File(buffer),save=False)
      canvas.close()
      super().save(*args,**kwargs)