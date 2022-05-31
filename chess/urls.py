from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gamepage/', views.gamepage, name='gamepage'),
    path('levels/', views.levels, name='levels'),
]