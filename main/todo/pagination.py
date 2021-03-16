from rest_framework.pagination import LimitOffsetPagination

class ProjectPagination(LimitOffsetPagination):
    default_limit = 10