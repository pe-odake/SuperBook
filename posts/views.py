from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import ListView
from .forms import PostForm

def lista_posts(request):
    posts = Post.objects.all() 
    return render(request, "posts/lista_posts.html", {"posts": posts})

class PostsListView(ListView):
    model = Post
    template_name = "posts/lista_posts.html"
    context_object_name = "posts"
    
def criar_posts(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_heroes')
    else:
        form = PostForm()

    return render(request, "posts/form_posts.html", {"form": form})