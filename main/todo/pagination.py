from rest_framework.pagination import LimitOffsetPagination

class ProjectPagination(LimitOffsetPagination):
    default_limit = 10

class ToDoPagination(LimitOffsetPagination):
    default_limit = 20