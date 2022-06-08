from django.urls import path
from . import views

app_name = 'chess'

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('levels/', views.levels, name='levels'),
    path('gamepage/', views.gamepage, name='gamepage'),
    path('about/', views.about, name='about'),
    path('tutorial/', views.tutorial, name='tutorial'),
    path('victory/', views.victory, name='victory'),
    path('defeat/', views.defeat, name='defeat'),

]