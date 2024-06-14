from django.urls import path
from . import views

app_name = 'authorapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('author/', views.author, name='author'),
    path('quotes/', views.quotes, name='quotes'),
    path('detail_quote/<int:quote_id>', views.detail_quote, name='detail_quote'),
    path('detail_author/<int:quote_id>', views.detail_author, name='detail_author'),
    path('done/<int:quote_id>', views.set_done, name='set_done'),
    path('delete_author/<int:author_id>', views.delete_author, name='delete_author'),
]
