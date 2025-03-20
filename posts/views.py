from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from django.urls import reverse_lazy


# Vista para listar posts
class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post


# Vista para ver el detalle de un post
class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post


# Vista para crear un nuevo post
class PostCreateView(CreateView):
    template_name = "posts/create.html"
    model = Post
    fields = ["title", "subtitle", "body", "status"]


# Vista para actualizar un post
class PostUpdateView(UpdateView):
    template_name = "posts/edit.html"
    model = Post
    fields = ["title", "subtitle", "body", "status"]


# Vista para eliminar un post
class PostDeleteView(DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("list")
