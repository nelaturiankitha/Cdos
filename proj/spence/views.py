from django.http import Http404
from django.shortcuts import render
from .models import Spence

def index(request):
    newest_pantry = Spence.objects.order_by('-release_date')[:15]
    context = {'newest_pantry': newest_pantry}
    return render(request, 'spence/index.html', context)

def show(request, movie_id):
    try:
        spence = Spence.objects.get(pk=movie_id)
    except Spence.DoesNotExist:
        raise Http404("Pantry does not exist")
    return render(request, 'spence/show.html', {'spence': spence})

# from django.shortcuts import render
# from .models import Spence

# def index(request):
#     newest_pantry = Spence.objects.order_by('-release_date')[:15]
#     # spence.objects.order_by('-release_date')[:15]
#     context = {'newest_pantry': newest_pantry}
#     return render(request, 'spence/index.html', context)
