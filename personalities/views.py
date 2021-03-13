from django.http import HttpResponse
from django.shortcuts import render
from .models import Personality

# Create your views here.


def index(request):
    # select * from personalities_personality
    personalities = Personality.objects.all()
    # output = ', '.join([p.name for p in personalities])
    # WHERE
    # .objects.filter(personality=)
    # .objects.get(id=1)
    return render(request, 'personalities/index.html', {'personalities': personalities})
