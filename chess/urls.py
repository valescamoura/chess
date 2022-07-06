from django.urls import path
from . import views

app_name = 'chess'

urlpatterns = [
    path('', views.index, name='index'),
    path('levels/', views.levels, name='levels'),
    path('gamepage/easy', views.gamepage_easy, name='gamepage_easy'),
    path('gamepage/hard', views.gamepage_hard, name='gamepage_hard'),
    path('about/', views.about, name='about'),
    path('tutorial/', views.tutorial, name='tutorial'),
    path('victory/', views.victory, name='victory'),
    path('defeat/', views.defeat, name='defeat'),
    path('get_moviments/', views.get_moviments, name='get_moviments'),
    path('move_piece/', views.move_piece, name='move_piece'),
    path('get_ai_move/', views.get_ai_move, name='get_ai_move'),
    path('ia_fight/', views.ia_fight, name='ia_fight'),
    path('get_ai_move_easy/', views.get_ai_move_easy2, name='get_ai_move_easy'),
    path('get_ai_move_hard/', views.get_ai_move_hard, name='get_ai_move_hard'),
    path('get_is_game_over/', views.get_is_game_over, name='get_is_game_over')
]