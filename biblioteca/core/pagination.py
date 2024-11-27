from rest_framework.pagination import LimitOffsetPagination


class LimitOffsetPagination(LimitOffsetPagination):
    max_limit = 5
