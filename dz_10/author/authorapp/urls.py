from django.urls import path
from . import views

app_name = 'authorapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('author/', views.author, name='author'),
    path('quotes/', views.quotes, name='quotes'),
    path('detail/<int:quote_id>', views.detail, name='detail'),
    path('done/<int:quote_id>', views.set_done, name='set_done'),
    path('delete/<int:quote_id>', views.delete_quote, name='delete'),
]
