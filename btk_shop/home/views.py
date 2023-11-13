from django.http import HttpResponse
from django.shortcuts import render

from home.models import Setting

# Create your views here.
def index(request):
    setting = Setting.objects.get(pk=1)
    title = "Volkan"
    context = {'setting': setting}
    return render(request, 'index.html', context)
    # return HttpResponse("Merhaba")

def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'hakkimizda.html', context)

def iletishim(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'iletisim.html', context)