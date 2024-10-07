from rest_framework.pagination import LimitOffsetPagination


class LimitOffsetPagination(LimitOffsetPagination):
    # Set the maximum limit value to 8
    max_limit = 5
