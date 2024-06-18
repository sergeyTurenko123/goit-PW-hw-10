from django.urls import path
from . import views

app_name = 'quoteapp'

urlpatterns = [
    path('', views.main, name="main"),
    path('<int:page>', views.main, name="root_paginate"),
    path('tag/', views.tag, name="tag"),
    path('quote/', views.quote, name="quote"),
    path('author/', views.author, name="author"),
    path('detail_author/<int:quote_id>', views.detail_author, name="detail_author"),
    path('delete_quote/<int:quote_id>', views.delete_quote, name="delete_quote"),
    path('detail_tag/<int:quote_id>/', views.detail_tag, name='detail_tag'),
]