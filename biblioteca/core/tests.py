from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Colecao  

class ColecaoTests(APITestCase):

    def setUp(self):
        # Configuração inicial: criar um usuário e gerar um token
        self.user = User.objects.create_user(username="superuser", password="superuser")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

    def test_criar_colecao_autenticado(self):
        # Enviar requisição para criar coleção
        data = {"nome": "Minha Coleção",
        "id": self.user.id, }
        response = self.client.post("/api/colecoes/", data)

        # Verificar a resposta e a associação da coleção ao usuário
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Colecao.objects.count(), 1)
        self.assertEqual(Colecao.objects.first().owner, self.user)

    def test_editar_deletar_apenas_proprietario(self):
        # Criar coleção associada ao usuário
        colecao = Colecao.objects.create(nome="Coleção Pessoal", owner=self.user)

        # Criar um segundo usuário
        other_user = User.objects.create_user(username="other_user", password="password456")
        other_token = Token.objects.create(user=other_user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {other_token.key}")

        # Tentar editar a coleção
        response_edit = self.client.put(f"/api/colecoes/{colecao.id}/", {"nome": "Novo Nome"})
        self.assertEqual(response_edit.status_code, 403)

        # Tentar deletar a coleção
        response_delete = self.client.delete(f"/api/colecoes/{colecao.id}/")
        self.assertEqual(response_delete.status_code, 403)

    def test_acoes_usuario_nao_autenticado(self):
        # Remover credenciais
        self.client.credentials()

        # Tentar criar uma coleção
        response_create = self.client.post("/api/colecoes/", {"nome": "Coleção Pública"})
        self.assertEqual(response_create.status_code, 401)

        # Criar uma coleção associada ao usuário autenticado
        colecao = Colecao.objects.create(nome="Coleção Privada", owner=self.user)

        # Tentar editar e deletar sem autenticação
        response_edit = self.client.put(f"/api/colecoes/{colecao.id}/", {"nome": "Novo Nome"})
        response_delete = self.client.delete(f"/api/colecoes/{colecao.id}/")

        self.assertEqual(response_edit.status_code, 401)
        self.assertEqual(response_delete.status_code, 401)

    def test_listar_colecoes_autenticado(self):
        # Criar coleções associadas ao usuário
        Colecao.objects.create(nome="Coleção 1", owner=self.user)
        Colecao.objects.create(nome="Coleção 2", owner=self.user)

        # Enviar requisição de listagem
        response = self.client.get("/api/colecoes/")

        # Verificar a resposta
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["nome"], "Coleção 1")
        self.assertEqual(response.data[1]["nome"], "Coleção 2")


