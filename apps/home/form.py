from inspect import classify_class_attrs
from os import name
from tkinter import E
from django import forms
from django.db import models
from django.db.models import fields
from .models import Governorate, Edara, Place, Request, Unit, Device, Mark, Model ,PersonalData


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('govern', 'edara', 'unit', 'place','device','mark', 'model', 'serial','national_id','name', 'phone' )




class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = '__all__'
    
 
   

class GovernateForm(forms.ModelForm):
    class Meta:
        model = Governorate
        fields = '__all__'
   

class EdaraForm(forms.ModelForm):
    class Meta:
        model = Edara
        fields = '__all__'


    

class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = '__all__'
        

  


class DeviceForm(forms.ModelForm):

    class Meta:
        model = Device
        fields = '__all__'


class MarkForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = '__all__'


class ModelForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = '__all__'

class PersonalDataForm(forms.ModelForm):
    class Meta:
        model = PersonalData
        fields = '__all__'

        labels = {
            'name': (''),
            'national_id':(''),
            'phone':('')
        }
        help_texts = {
            'name': ('الاسم'),
            'national_id': ('الرقم القومى'),
            'phone': ('رقم الموبايل'),
        }
        


class GovernateForm(forms.ModelForm):
    class Meta:
        model = Governorate
        fields = '__all__'

