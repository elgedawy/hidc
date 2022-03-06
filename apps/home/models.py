
from cgitb import reset
from pydoc import plain
from statistics import mode
from tkinter import Place
from unicodedata import name
from wsgiref.handlers import format_date_time
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey


class Governorate(models.Model):
     code = models.IntegerField(verbose_name='كود المحافظة')
     name = models.CharField(max_length=15,verbose_name='المحافظة')
     def __str__(self):
        return self.name
     class Meta:
      verbose_name_plural = "المحافظة"
  




class Edara(models.Model):
     govern = models.ForeignKey(Governorate,on_delete=CASCADE, verbose_name='محافظة')
     code = models.IntegerField(verbose_name='كود الادارة')
     name = models.CharField(max_length=15, verbose_name='الادارة')
     def __str__(self):
        return self.name
     class Meta:
       verbose_name_plural = "الادارة"
  

class Unit(models.Model):
     governorate = models.ForeignKey(Governorate, on_delete=CASCADE,verbose_name="المحافظة")
     edara = models.ForeignKey(Edara, on_delete=CASCADE, verbose_name="الادارة")
     code = models.IntegerField(verbose_name=" كود الوحدة ")
     name = models.CharField(max_length=15, verbose_name="الوحدة")
     def __str__(self):
        return self.name
     class Meta:
       verbose_name_plural = "الوحدة"
  

class Device(models.Model):
    name = models.CharField(max_length=15, verbose_name="الجهاز")
    def __str__(self):
        return self.name
    class Meta:
      verbose_name_plural = "نوع الجهاز"
  

    


class Mark(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    name = models.CharField(max_length=15, verbose_name="الماركة")
    def __str__(self):
        return self.name
    class Meta:
      verbose_name_plural = "الماركة"
  


class Model(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE)
    name = models.CharField(max_length=10, verbose_name="الموديل")
    def __str__(self):
        return self.name
    class Meta:
       verbose_name_plural = "الموديل"
  



class PersonalData(models.Model):
    name = models.CharField(max_length=200, verbose_name='الاسم')
    national_id = models.IntegerField(max_length=14)
    phone = models.IntegerField(max_length=14)
    def __str__(self):
        return self.name
    class Meta:
       verbose_name_plural = "البيانات الشخصية "


class Place(models.Model):
    name = models.CharField(max_length=50)
    govern = models.ForeignKey(Governorate, on_delete=models.CASCADE)
    edara = models.ForeignKey(Edara, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    serial = models.IntegerField()
    national_id = models.IntegerField(max_length=14)
    def __str__(self):
        return self.name



class Request(models.Model):
    govern = models.ForeignKey(Governorate, on_delete=models.CASCADE,  verbose_name='')
    edara = models.ForeignKey(Edara, on_delete=models.CASCADE,  verbose_name='')
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE,  verbose_name='')
    place = models.ForeignKey(Place, on_delete=models.CASCADE,  verbose_name=' ')
    device = models.ForeignKey(Device, on_delete=models.CASCADE, verbose_name='')
    model = models.ForeignKey(Model, on_delete=models.CASCADE,  verbose_name='')
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE,  verbose_name='')
    serial = models.IntegerField(verbose_name='')
    national_id = models.IntegerField(max_length=14,  verbose_name='')
    name = models.CharField(max_length=50,  verbose_name='')
    phone = models.IntegerField( verbose_name=''
    
    )
    datatime = models.DateTimeField(auto_now=True)
 





    















