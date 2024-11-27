from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("livros/", views.LivroList.as_view(), name=views.LivroList.name),
    path("livros/<int:pk>/", views.LivroDetail.as_view(), name=views.LivroDetail.name),
    path("categorias/", views.CategoriaList.as_view(), name=views.CategoriaList.name),
    path("categorias/<int:pk>/", views.CategoriaDetail.as_view(), name=views.CategoriaDetail.name),
    path("autores/", views.AutorList.as_view(), name=views.AutorList.name),
    path("autores/<int:pk>/", views.AutorDetail.as_view(), name=views.AutorDetail.name),
    path("colecoes/", views.ColecaoListCreate.as_view(), name=views.ColecaoListCreate.name),
    path("colecoes/<int:pk>/", views.ColecaoDetail.as_view(), name=views.ColecaoDetail.name),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
    path("", views.ApiRoot.as_view(), name=views.ApiRoot.name),
]
