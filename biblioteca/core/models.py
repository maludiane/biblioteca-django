from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome


class Autor(models.Model):
    nome = models.CharField(max_length=100, unique=False)

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="livros")
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name="livros"
    )
    publicado_em = models.DateField()

    def __str__(self):
        return self.titulo


class Colecao(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)
    livros = models.ManyToManyField(Livro, related_name="colecoes")
    colecionador = models.ForeignKey(
        User, related_name="colecoes", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.nome} - {self.colecionador.username}"
