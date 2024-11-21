from rest_framework import serializers
from .models import Categoria, Autor, Livro, Colecao
from django.contrib.auth.models import User


from rest_framework import serializers
from .models import Categoria, Autor, Livro, Colecao


class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ["id", "nome"]


class AutorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Autor
        fields = ["id", "nome"]


class LivroSerializer(serializers.HyperlinkedModelSerializer):
    autor = serializers.SlugRelatedField(
        queryset=Autor.objects.all(), slug_field="name"
    )
    categoria = serializers.SlugRelatedField(
        queryset=Categoria.objects.all(), slug_field="name"
    )

    class Meta:
        model = Livro
        fields = [
            "id",
            "titulo",
            "autor",
            "categoria",
            "publicado_em",
        ]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
        ]


class ColecaoSerializer(serializers.ModelSerializer):
    livros = LivroSerializer(many=True)
    colecionador = UserSerializer()

    class Meta:
        model = Colecao
        fields = [
            "id",
            "nome",
            "descricao",
            "livros",
            "colecionador",
        ]
