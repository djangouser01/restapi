from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from recursos.models import Recurso
from .serializers import RecursoSerializer


class RecursoViewSet(ModelViewSet):
    queryset = Recurso.objects.all()
    serializer_class = RecursoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome']

