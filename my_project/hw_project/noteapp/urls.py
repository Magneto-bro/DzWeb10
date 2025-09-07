from django.urls import path
from . import views

app_name = 'noteapp'
urlpatterns = [
    path('add_quote/', views.add_quote, name='add_quote'),
]
