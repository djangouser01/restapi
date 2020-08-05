from django.utils.text import capfirst
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import PontoTuristicoSerializer
from ..models import PontoTuristico


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    filter_backends = [filters.SearchFilter]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    search_fields = ['nome', 'nome','endereco__linha1']

    def get_queryset(self):
        # id = self.request.query_params.get('id', None)
        # aprovado = self.request.query_params.get('aprovado', None)
        # nome = self.request.query_params.get('nome', None)
        # queryset = PontoTuristico.objects.all()
        #
        # if id:
        #     queryset = queryset.filter(pk=id)
        #
        # if nome:
        #     queryset = queryset.filter(nome__iexact=nome)
        #
        # return queryset

        return PontoTuristico.objects.filter()

    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, args, **kwargs)

    #
    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, args, **kwargs)

    # @action(methods=['get'], detail=True)
    # def denunciar(self, request, pk=None):
    #     pass
    #
    # @action(method=['get'], detail=False)
    # def teste(self, request):
    #     pass
