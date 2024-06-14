from django.urls import path
from . import views

app_name = 'authorapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('author/', views.author, name='author'),
    path('quotes/', views.quotes, name='quotes'),
    path('detail/<int:quotes_id>', views.detail, name='detail'),
]
