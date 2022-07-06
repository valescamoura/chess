from django.shortcuts import render
from django.http import JsonResponse
from chess.src.services import Services 
import time

# Constants

SERVICE = Services()
LEVEL = 'easy'

# Pages

def index(request): 
    return render(request, 'chess/menu.html', {})
    
def gamepage_easy(request):
    global SERVICE
    global LEVEL

    SERVICE = Services()
    board = SERVICE.start_game()
    print(board)
    LEVEL = 'easy'

    return render(request, 'chess/chess.html', {})

def gamepage_hard(request):
    global SERVICE
    global LEVEL

    SERVICE = Services()
    board = SERVICE.start_game()
    LEVEL = 'hard'

    print(board)

    return render(request, 'chess/chess.html', {})

def ia_fight(request):
    global SERVICE
    global LEVEL

    SERVICE = Services()
    board = SERVICE.start_game()

    return render(request, 'chess/ia_fight.html', {})

def levels(request):
    return render(request, 'chess/levels.html', {})

def about(request):
    return render(request, 'chess/about.html', {})

def tutorial(request):
    return render(request, 'chess/tutorial.html', {})

def victory(request):
    return render(request, 'chess/victory.html', {})

def defeat(request):
    return render(request, 'chess/defeat.html', {})

# Requests

def get_moviments(request):
    idBoardHouse = request.GET['id']
    legal_moves = SERVICE.get_legal_moves(idBoardHouse)
    print(legal_moves)
    response = {'legal_moves': legal_moves}
    return JsonResponse(response)

def move_piece(request):
    print(request.GET)
    old_piece = request.GET['old_piece']
    new_piece = request.GET['new_piece']
    type_of_piece = request.GET['type_of_piece']

    print(old_piece, new_piece, type_of_piece)

    new_board = SERVICE.execute_move(old_piece, new_piece, type_of_piece)

    response = {'new_board': new_board}
    time.sleep(0.5)
    return JsonResponse(response)

def get_ai_move(request):
    if LEVEL == 'easy':
        return get_ai_move_easy(request)
    else:
        return get_ai_move_hard(request)

def get_ai_move_easy(request):
    new_board = SERVICE.IAMove_facil()
    
    response = {'new_board': new_board}
    time.sleep(0.5)
    return JsonResponse(response) 

def get_ai_move_easy2(request):
    new_board = SERVICE.IAMove_facil('white')
    
    response = {'new_board': new_board}
    time.sleep(0.5)
    return JsonResponse(response)

def get_ai_move_hard(request):
    new_board = SERVICE.IAMove_medio()
    
    response = {'new_board': new_board}

    time.sleep(0.5)
    return JsonResponse(response)

def get_is_game_over(request):
    is_game_over = False
    winner = ''

    if SERVICE.didPlayerWin():
        winner = 'player'
        is_game_over = True
    elif SERVICE.drawn():
        winner = 'drawn'
        is_game_over = True
    elif SERVICE.didIAWin():
        winner = 'ia'
        is_game_over = True

    response = {'is_game_over': is_game_over, 'winner': winner}
    print(response)
    return JsonResponse(response)
