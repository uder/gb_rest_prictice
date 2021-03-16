from django_filters.rest_framework import FilterSet,CharFilter,DateTimeFilter
from .models import Project,ToDo

class ProjectFilter(FilterSet):
    name=CharFilter(lookup_expr='contains')
    class Meta:
        model=Project
        fields=['name']

class ToDoFilter(FilterSet):
    min_date=DateTimeFilter(field_name="created_at", lookup_expr="gte")
    max_date=DateTimeFilter(field_name="created_at", lookup_expr="lte")

    class Meta:
        model=ToDo
        fields = ['created_at']