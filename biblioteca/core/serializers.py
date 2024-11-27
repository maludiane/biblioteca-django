from rest_framework import serializers
from .models import Categoria, Autor, Livro, Colecao
from django.contrib.auth.models import User


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"  


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"


class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"


class ColecaoSerializer(serializers.ModelSerializer):
    livros = LivroSerializer(
        many=True, read_only=True
    )  
    colecionador = serializers.StringRelatedField() 

    class Meta:
        model = Colecao
        fields = "__all__"


# Opcional: Serializer para o User (caso necessário)
class UserSerializer(serializers.ModelSerializer):
    colecoes = ColecaoSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "colecoes"]
