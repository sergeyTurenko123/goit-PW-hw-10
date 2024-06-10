from django.urls import path
from . import views

app_name = 'authorapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('author/', views.author, name='author'),
    path('quote/', views.quote, name='quote'),
    path('detail/<int:author_id>', views.detail, name='author'),
    # path('done/<int:author_id>', views.set_done, name='set_done'),
    # path('delete/<int:author_id>', views.delete_note, name='delete')
]
