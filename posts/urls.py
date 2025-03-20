from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),  # Lista de posts
    path("<int:pk>/", views.PostDetailView.as_view(), name="detail"),  # Detalle
    path("create/", views.PostCreateView.as_view(), name="create"),  # Crear post
    path("<int:pk>/edit/", views.PostUpdateView.as_view(), name="edit"),  # Editar
    path("<int:pk>/delete/", views.PostDeleteView.as_view(), name="delete"),  # Eliminar
]
