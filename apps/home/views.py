# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from ast import UnaryOp
from logging import PlaceHolder
from multiprocessing import context
from statistics import mode
from tkinter import E
from unicodedata import name
from django import template
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from .models import Device, Edara, Governorate, Model,Mark, Place,  Unit, PersonalData, Request
from .form import GovernateForm, EdaraForm, PlaceForm, UnitForm, DeviceForm, ModelForm, MarkForm, PersonalDataForm,RequestForm
from apps.home.models import Governorate
from django.contrib import messages 
from reportlab.pdfgen import canvas  
from django.http import HttpResponse 
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3
from reportlab.lib.pagesizes import portrait
from reportlab.platypus import Image


def index(request):
    printers = Place.objects.all().count()
    return render(request, 'home/index.html', {printers:printers})



@login_required(login_url="/login/")
def governate(request):
    govern = Governorate.objects.all()
    return render(request, 'home/governate.html', {'govern': govern})

def addgovernate(request):
    if request.method == 'POST':
     datagov = GovernateForm(request.POST)
     if datagov.is_valid:
         datagov.save()

    return render(request, 'home/addgovernate.html', {'governat': GovernateForm})


def edara(request):
    edara = Edara.objects.all()
    return render(request, 'home/edara.html', {'edara': edara})


def addedara(request):

    return render(request, 'home/addedara.html', {'dedara': EdaraForm})


def unit(request):

    unit= Unit.objects.all()

    return render(request,'home/unit.html', {'unit': unit})


def addunit(request):
    if request.method == 'POST':
     dataaddunit = UnitForm(request.POST)
     dataaddunit.save()

    return render(request,'home/addunit.html', {'addunit': UnitForm})



def load_dists(request):
    govern = request.GET.get('govern')
    edara = Edara.objects.filter(govern=govern)
    return render(request,'home/city_dropdown_list_options.html', {'edara': edara})

def load_units(request):
    edara = request.GET.get('edara')
    unit = Unit.objects.filter(edara=edara)
    return render(request,'home/unit_dropdown_list_options.html', {'unit': unit})

def load_place(request):
    place = request.GET.get('place')
    place = Place.objects.filter(unit=place)
    return render(request,'home/place_dropdown_list_options.html', {'place': place})


def load_model_request(request):
    device = request.GET.get('device')
    models = Place.objects.filter(pk=device)
    return render(request,'home/model_request.html', {'models': models})


def device(request):
    device = Device.objects.all()
    return render(request,'home/device.html', {'device' :device})
 
def add_device(request):
    if request.method == 'POST':
        datadevice = DeviceForm(request.POST)
        if datadevice.is_valid:
           datadevice.save()
           return redirect('device')
    return render(request,'home/add_device.html', {'device' :DeviceForm})

def model(request):
    model = Model.objects.all()
    return render(request,'home/device/model.html', {'model' :model})

def addmodel(request):
  if request.method == 'POST':
    datamodel = ModelForm(request.POST)
    if datamodel.is_valid:
       datamodel.save()
       return redirect('model')
  return render(request,'home/device/addmodel.html', {'dmodel' :ModelForm})


def load_marks(request):
    device = request.GET.get('device')
    marks = Mark.objects.filter(device=device)
    return render(request,'home/device/mark_dropdown_list_options.html', {'marks': marks})



def load_models(request):
    mark = request.GET.get('mark')
    models = Model.objects.filter(mark=mark)
    return render(request,'home/device/model_dropdown_list_options.html', {'models': models})



def mark(request):
    mark = Mark.objects.all()
    return render(request,'home/device/mark.html', {'mark' :mark})


def addmark(request):
    if request.method == 'POST':
     MarkFormdt = MarkForm(request.POST)
     if MarkFormdt.is_valid:
         MarkFormdt.save()
         return redirect('mark')
    return render(request,'home/device/addmark.html', {'dmark' :MarkForm})

    

def personaldata(request):
    
    if request.method == 'POST':
     Personaldata = PersonalDataForm(request.POST)
     if Personaldata.is_valid:
         Personaldata.save()


    return render(request,'home/personaldata.html', {'dpersonal' :PersonalDataForm})


def display_name(request):

    id = request.GET.get('id')
    employee = PersonalData.objects.get(national_id=id)
    name = employee.name
    phone = employee.phone
    data = {'name':name, 'phone':phone}
    return JsonResponse(data)

def place(request):
    place = Place.objects.all()
    context = {'place': place}
    return render(request, 'home/place.html', context)


def addplace(request):
    if request.method == 'POST':
     datagov = PlaceForm(request.POST)
     if datagov.is_valid:
         datagov.save()
         messages.success(request, 'تم حفظ الجهاز ')
         return redirect('place')
    context = {'placeform': PlaceForm}

    return render(request, 'home/addplace.html', context)


def request(request):
    datarequest = Request.objects.all()
    form = RequestForm(request.POST or None)
    context = {
        'request': datarequest,
        'form': form

        }
    
    if request.method == 'POST':
        datarequest = Request.objects.filter(name__icontains = form['name'].value())

        context = {
            
            'request': datarequest,
            'form': form
        }

    return render(request, 'home/request.html', context)


def addrequest(request):

    if request.method == 'POST':
     datarequest = RequestForm(request.POST)
     if datarequest.is_valid:
         datarequest.save()
         return redirect('request')
    return render(request, 'home/addrequest.html', {'requestform': RequestForm})


def product_delete(request, pk):
    item = Request.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        
        return redirect('request')

    return render(request, 'home/products_delete.html', {'item': item})














































	

# def display_name(request):
#     id = request.GET.get('id')
#     try:
#         employee = PersonalData.objects.get(national_id=id)
#     except PersonalData.DoesNotExist:
#         return JsonResponse({'error': 'Employee not found'}, status=404)

#     name = employee.name
#     return JsonResponse({'name': name})




# def index(request):
#     html_template = loader.get_template('home/index.html')
# @login_required(login_url="/login/")
# def pages(request):
#     context = {}
#     # All resource paths end in .html.
#     # Pick out the html file name from the url. And load that template.
#     try:

#         load_template = request.path.split('/')[-1]

#         if load_template == 'admin':
#             return HttpResponseRedirect(reverse('admin:index'))
#         context['segment'] = load_template

#         html_template = loader.get_template('home/' + load_template)
#         return HttpResponse(html_template.render(context, request))

#     except template.TemplateDoesNotExist:

#         html_template = loader.get_template('home/page-404.html')
#         return HttpResponse(html_template.render(context, request))

#     except:
#         html_template = loader.get_template('home/page-500.html')
#         return HttpResponse(html_template.render(context, request))

 
  
def getpdf(request):  
    response = HttpResponse(content_type='application/pdf')  
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'  
    p = canvas.Canvas(response)  
    p.setFont("Times-Roman", 20)  
    p.drawString(100,700, "Hello, MOHAMED OMAR.")  
    p.showPage()  
    p.save()  
    return response  