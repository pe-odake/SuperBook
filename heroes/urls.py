from django.urls import path
from . import views
from .views import Home


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('hello/', views.hello_heroes, name='hello_heroes'),
    path('lista/', views.lista_herois, name='lista_heroes'),
    path('cbv-lista/', views.HeroListView.as_view(), name='cbv_lista_herois'),
    path('contato/', views.contato_view, name='contato'),
    path('novo/', views.criar_heroi, name='criar_heroi'),
]

