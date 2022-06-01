from django.urls import path
from . import views

app_name = 'chess'

urlpatterns = [
    path('', views.index, name='index'),
    path('levels/', views.levels, name='levels'),
    path('gamepage/', views.gamepage, name='gamepage'),
    path('about/', views.about, name='about'),
    path('tutorial/', views.tutorial, name='tutorial'),
]