from django.urls import path
from . import views

app_name = 'quoteapp'

urlpatterns = [
    path('', views.main, name="main"),
    path('<int:page>', views.main, name="root_paginate"),
    path('tag/', views.tag, name="tag"),
    path('quote/', views.quote, name="quote"),
]