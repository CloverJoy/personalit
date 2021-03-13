from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
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


def detail(request, personality_mbtitype):
    personality = get_object_or_404(Personality, mbtitype=personality_mbtitype)
    return render(request, 'personalities/detail.html', {'personality': personality})

    # try:
    #     personality = Personality.objects.get(mbtitype=personality_mbtitype)
    #     return render(request, 'personalities/detail.html', {'personality': personality})
    # except Personality.DoesNotExist:
    #     raise Http404()
