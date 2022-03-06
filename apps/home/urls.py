# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views, api

urlpatterns = [

    # The home page
    path('', views.index, name='index'),
    path('request', views.request, name='request'),
    path('addrequest', views.addrequest, name='addrequest'),
    path('request/delete/<int:pk>/', views.product_delete, name='request_delete'),
    path('place', views.place, name='place'),
    path('addplace', views.addplace, name='addplace'),
    path('governate', views.governate, name='governate'),
    path('addgovernate', views.addgovernate, name='addgovernate'),
    path('edara', views.edara, name='edara'),
    path('addedara', views.addedara, name='addedara'),
    path('unit', views.unit, name='unit'),
    path('addunit', views.addunit, name='addunit'),
    path('device', views.device, name='device'),
    path('add_device', views.add_device, name='add_device'),
    path('model', views.model, name='model'),
    path('addmodel', views.addmodel, name='addmodel'),
    path('mark', views.mark, name='mark'),
    path('addmark', views.addmark, name='addmark'),
    path('personaldata', views.personaldata, name='personaldata'),
    path('ajax/load-edara/', views.load_dists, name='ajax_load_dists'),
    path('ajax/load-unit/', views.load_units, name='ajax_load_unit'),
    path('ajax/display_name/', views.display_name, name='display_name'),
    path('ajax/load_mark/', views.load_marks, name='ajax_load_marks'),
    path('ajax/load_model/', views.load_models, name='ajax_load_models'),
    path('ajax/load_place/', views.load_place, name='ajax_load_place'),
    path('ajax/load_model_request/', views.load_model_request, name='ajax_model_request'),
    path('api/request', api.request_list_api, name='reqlistapi'),
    path('api/request/<int:id>', api.request_detail_api, name='request_detail_api'),
    path('api/v2/request/<int:id>', api.RequestDetail.as_view(), name='RequestDetail'),
    path('pdf',views.getpdf),


]
 