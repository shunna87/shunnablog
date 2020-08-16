from django.shortcuts import render
from .models import Imprint

# Create your views here.


def index(request):
    return render(request, 'web/index.html')


def imprint(request):
    impr = Imprint.objects.get(pk=1)
    data = {'impr': impr}
    return render(request, 'web/imprint.html', data)
