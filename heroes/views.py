from django.shortcuts import render
from django.http import HttpResponse
from .models import Hero
from django.views.generic import ListView, TemplateView

def hello_heroes(request):
    return HttpResponse("Bem-vindo ao módulo Heroes!")

def lista_herois(request):
    herois = Hero.objects.all()  
    return render(request, "heroes/lista_herois.html", {"herois": herois})

class Home(TemplateView):
    template_name = 'base.html'

class HeroListView(ListView):
    model = Hero
    template_name = "heroes/base.html"
    context_object_name = "herois"