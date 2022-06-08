from django.shortcuts import render

# Pages

def index(request): 
    return render(request, 'chess/menu.html', {})
    
def menu(request): 
    return render(request, 'chess/menu.html', {})
    
def gamepage(request):
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
