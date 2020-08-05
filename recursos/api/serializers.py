from rest_framework import serializers
from recursos.models import Recurso


class RecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recurso
        fields = ['id', 'nome', 'descricao', 'horario_func', 'idade_minima', 'foto']
