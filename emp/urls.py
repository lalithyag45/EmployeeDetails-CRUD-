from django.contrib import admin
from django.urls import path
from. import views
urlpatterns = [
    path('', views.index, name='index'),
    path('input/', views.input, name='input'),
    path('display/', views.display, name='display'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
]
