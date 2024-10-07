from django.urls import path
from . import views

urlpatterns = [
    path("livros/", views.LivroList.as_view(), name=views.LivroList.name),
    path("livros/<int:pk>/", views.LivroDetail.as_view(), name=views.LivroDetail.name),
    path("categorias/", views.CategoriaList.as_view(), name=views.CategoriaList.name),
    path("categorias/<int:pk>/", views.CategoriaDetail.as_view(), name=views.CategoriaDetail.name),
    path("autores/", views.AutorList.as_view(), name=views.AutorList.name),
    path("autores/<int:pk>/", views.AutorDetail.as_view(), name=views.AutorDetail.name),
    path("", views.ApiRoot.as_view(), name=views.ApiRoot.name),
]
