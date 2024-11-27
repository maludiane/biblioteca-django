from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Livro, Autor, Categoria, Colecao
from .serializers import (
    LivroSerializer,
    AutorSerializer,
    CategoriaSerializer,
    ColecaoSerializer,
)
from .custom_permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.reverse import reverse


class ApiRoot(generics.GenericAPIView):
    name = "api-root"

    def get(self, request, *args, **kwargs):
        return Response(
            {
                "livros": reverse(LivroList.name, request=request),
                "categorias": reverse(CategoriaList.name, request=request),
                "autores": reverse(AutorList.name, request=request),
                "colecoes": reverse(ColecaoListCreate.name, request=request),
            }
        )


class LivroList(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = "livro-list"


class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = "livro-detail"


class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = "categoria-list"
    search_fields = ("^nome",)
    ordering_fields = ("nome",)


class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = "categoria-detail"


class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = "autor-list"
    search_fields = ("^nome",)
    ordering_fields = ("nome",)


class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = "autor-detail"


class ColecaoListCreate(generics.ListCreateAPIView):   
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    name = "colecao-list"
    permission_classes = [
        IsAuthenticated
    ]  
    def perform_create(self, serializer):

        serializer.save(colecionador=self.request.user,)


class ColecaoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    name = "colecao-detail"
    permission_classes = [IsOwnerOrReadOnly]  
