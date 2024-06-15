from django.urls import path
from . import views

app_name = 'quoteapp '

urlpatterns = [
    path("", views.main, name='maine'),
    path("<int:page>", views.main, name='root_paginate'),
]