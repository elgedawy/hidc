# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("authentication/", include("apps.authentication.urls")), # Auth routes - login / register
    path("", include("apps.home.urls")),
    path("maintainance/", include("apps.maintainance.urls")),

    # UI Kits Html files
]

