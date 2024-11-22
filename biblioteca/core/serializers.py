from rest_framework import serializers
from .models import Categoria, Autor, Livro, Colecao
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Categoria, Autor, Livro, Colecao


class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ["__all__"]


class AutorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Autor
        fields = ["__all__"]


class LivroSerializer(serializers.HyperlinkedModelSerializer):
    autor = serializers.SlugRelatedField(
        queryset=Autor.objects.all(), slug_field="nome"
    )
    categoria = serializers.SlugRelatedField(
        queryset=Categoria.objects.all(), slug_field="nome"
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
        fields = ["__all__"]


class ColecaoSerializer(serializers.ModelSerializer):
    livros = LivroSerializer(many=True)
    colecionador = UserSerializer()
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Colecao
        fields = ["__all__", "owner", "livros", "colecionador"]
