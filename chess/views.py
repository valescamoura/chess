from django.shortcuts import render
from django.http import JsonResponse
from chess.src.services import Services 

# Pages

def index(request): 
    return render(request, 'chess/menu.html', {})
    
def gamepage(request):
    board = Services.start_game()
    print(board)
    return render(request, 'chess/chess.html', {})

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

# 

def get_moviments(request):
    idBoardHouse = request.GET['id']
    legal_moves = Services.get_legal_moves(idBoardHouse)

    response = {'legal_moves': legal_moves}
    return JsonResponse(response)

def move_piece(request):
    old_piece = request.GET['old_piece']
    new_piece = request.GET['new_piece']

    new_board = Services.execute_move(old_piece, new_piece)

    response = {'new_board': new_board}
    return JsonResponse(response)
