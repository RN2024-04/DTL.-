from django.shortcuts import render
from django.views.generic import TemplateView



# Create your views here.
def platform_templates(request):
    return render(request, 'fourth_task/platform.html')

def games_templates(request):
    game_dict = {'games': ["Atomic Heart", "Cyberpunk 2077", "PayDay 77"]}
    context = {
        'game_dict': game_dict,
    }
    return render(request, 'fourth_task/games.html', context)
def cart_templates(request):
    return render(request, "fourth_task/cart.html")