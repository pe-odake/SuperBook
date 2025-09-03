from django.urls import path
from . import views

urlpatterns = [
    path('lista_posts/', views.lista_posts, name='lista_posts'),
    path('cbv-lista/', views.PostsListView.as_view(), name='cbv_lista_posts'),
    path('novo/', views.criar_posts, name='criar_posts'),
]

