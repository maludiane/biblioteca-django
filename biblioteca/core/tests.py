from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.urls import reverse
from .models import Colecao, Livro, Autor, Categoria


class ColecaoTests(APITestCase):
    def setUp(self):
        # Configurar usuários e tokens
        self.user = User.objects.create_user(
            username="user01", email="user01@example.com", password="user01P4ssw0rD"
        )
        self.user_token = Token.objects.create(user=self.user)

        self.other_user = User.objects.create_user(
            username="user02", email="user02@example.com", password="user02P4ssw0rD"
        )
        self.other_user_token = Token.objects.create(user=self.other_user)

        # Configurar livros e coleções
        self.autor = Autor.objects.create(nome="Autor Exemplo")
        self.categoria = Categoria.objects.create(nome="Ficção")
        self.livro = Livro.objects.create(
            titulo="Livro Exemplo",
            autor=self.autor,
            categoria=self.categoria,
            publicado_em="2023-01-01",
        )
        self.colecao = Colecao.objects.create(
            nome="Coleção Exemplo", colecionador=self.user
        )
        self.colecao.livros.add(self.livro)

    def authenticate_user(self, token):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def test_create_colecao_authenticated(self):
        self.authenticate_user(self.user_token)
        url = reverse("colecao-list")
        data = {
            "nome": "Nova Coleção",
            "descricao": "Descrição da nova coleção",
            "livros": [self.livro.id],
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["nome"], "Nova Coleção")

    def test_create_colecao_unauthenticated(self):
        url = reverse("colecao-list")
        data = {
            "nome": "Nova Coleção Não Autenticada",
            "descricao": "Descrição sem autenticação",
            "livros": [self.livro.id],
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_colecao_by_owner(self):
        self.authenticate_user(self.user_token)
        url = reverse("colecao-detail", args=[self.colecao.id])
        data = {"nome": "Coleção Atualizada"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["nome"], "Coleção Atualizada")

    def test_update_colecao_by_non_owner(self):
        self.authenticate_user(self.other_user_token)
        url = reverse("colecao-detail", args=[self.colecao.id])
        data = {"nome": "Tentativa de Atualização"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_colecao_by_owner(self):
        self.authenticate_user(self.user_token)
        url = reverse("colecao-detail", args=[self.colecao.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_colecao_by_non_owner(self):
        self.authenticate_user(self.other_user_token)
        url = reverse("colecao-detail", args=[self.colecao.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_colecoes_authenticated(self):
        self.authenticate_user(self.user_token)
        url = reverse("colecao-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_list_colecoes_unauthenticated(self):
        url = reverse("colecao-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
