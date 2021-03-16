from django_filters.rest_framework import FilterSet,CharFilter
from .models import Project

class ProjectFilter(FilterSet):
    name=CharFilter(lookup_expr='contains')
    class Meta:
        model=Project
        fields=['name']