from django.shortcuts import render

# Create your views here.

from .models import World

def home (request):
    worlds = World.objects
    return render(request, 'world/home.html', {"worlds": worlds})
