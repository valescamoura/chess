from django.urls import path
from . import views

app_name = 'chess'

urlpatterns = [
    path('', views.index, name='index'),
    path('levels/', views.levels, name='levels'),
    path('gamepage/', views.gamepage, name='gamepage'),
    path('about/', views.about, name='about'),
    path('tutorial/', views.tutorial, name='tutorial'),
    path('victory/', views.victory, name='victory'),
    path('defeat/', views.defeat, name='defeat'),
    path('get_moviments/', views.get_moviments, name='get_moviments'),
    path('move_piece/', views.move_piece, name='move_piece'),
    path('get_ai_move/', views.get_ai_move, name='get_ai_move'),
]