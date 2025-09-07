from django.urls import path
from . import views

app_name = "quotes"

urlpatterns = [
    path('', views.main, name='all_quotes'),
    path('page/<int:page>/', views.main, name='all_quotes_paginate'),

]
