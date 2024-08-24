from django.urls import path
from . import views

urlpatterns = [
    path("livros/", views.livro_list_create, name="livros-list-create"),
    path("livros/<int:pk>/", views.livro_detail, name="livro-detail"),
]
