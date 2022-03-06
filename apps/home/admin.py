# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from dataclasses import fields
from django.contrib import admin
from .models import Device, Mark, Model, Governorate, Edara, Place, Request, Unit, PersonalData
from import_export.admin import ImportExportModelAdmin



@admin.register(Device)
class DeviceAdmin(ImportExportModelAdmin):
    pass

@admin.register(Mark)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('device', 'name')


@admin.register(Model)
class ModelAdmin(ImportExportModelAdmin):
    list_display = ('device', 'mark', 'name')

@admin.register(Governorate)
class GovernorateAdmin(ImportExportModelAdmin):
    list_display = ['name' ,'code' ]
    search_fileds = ['name']

@admin.register(Edara)
class EdaraAdmin(ImportExportModelAdmin):
     list_display = ('govern', 'code', 'name')

@admin.register(Unit)
class UnitAdmin(ImportExportModelAdmin):
    list_display = ('governorate', 'edara', 'code', 'name')



@admin.register(PersonalData)
class PersonalDataAdmin(ImportExportModelAdmin):
    list_display = ('name', 'national_id', 'phone')

@admin.register(Place)
class PlaceAdmin(ImportExportModelAdmin):
    list_display = ('govern', 'edara', 'unit', 'name','device', 'mark', 'model','serial', 'national_id')
@admin.register(Request)
class RequestAdmin(ImportExportModelAdmin):
    list_display = ('govern', 'edara', 'unit', 'place','device', 'model','serial')

# Register your models here.








