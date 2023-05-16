from django.shortcuts import render
from . import models

def index(request):
    all_games = models.Games.objects.all()
    context = {'all_games': all_games}

    return render(request, 'index.html', context)

def game_page(request, pk):
    category = models.Category.objects.get(id = pk)
    game_from_category = models.Games.objects.filter(game_category=category)
    tournirs_stark = models.StarkTournirs.objects.filter(tournirs_category = category)
    tournirs_cyberium = models.CyberiumTournirs.objects.filter(tournirs_category = category)
    tournirs_cyberarena = models.CyberArenaTournirs.objects.filter(tournirs_category = category)
    context = {'games': game_from_category, 'StarkTournirs': tournirs_stark, 'CyberiumTournirs': tournirs_cyberium, 'CyberArenaTournirs': tournirs_cyberarena}

    return render(request, 'about.html', context)

def login(request):
    return render(request, 'login.html')