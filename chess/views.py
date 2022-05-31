from django.shortcuts import render

def index(request): 
    return render(request, 'chess/menu.html', {})
    
def gamepage(request):
    return render(request, 'chess/chess.html', {})

def levels(request):
    return render(request, 'chess/levels.html', {})
