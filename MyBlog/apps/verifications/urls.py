#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path
from django.urls import re_path

from . import views

app_name = 'verifications'

urlpatterns = [
    path('image_codes/<uuid:image_code_id>', views.ImageCode.as_view(), name='image_code'),
    re_path('username/(?P<username>\w{5, 20})', views.CheckUsernameView.as_view(), name='check_username'),
]
