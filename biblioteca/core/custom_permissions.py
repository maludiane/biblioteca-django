from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permissão customizada que permite apenas ao colecionador modificar a coleção.
    Outros usuários podem apenas visualizar.
    """

    def has_object_permission(self, request, view, obj):
        # Permissões de leitura são permitidas para qualquer requisição
        if request.method in permissions.SAFE_METHODS:
            return True

        # Permissão de escrita apenas para o colecionador
        return obj.colecionador == request.user
