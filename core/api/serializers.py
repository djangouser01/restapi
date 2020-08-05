from rest_framework import serializers
from core.models import PontoTuristico
from recursos.api.serializers import RecursoSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from enderecos.api.serializers import EnderecoSerializer
from rest_framework.fields import SerializerMethodField


class PontoTuristicoSerializer(serializers.ModelSerializer):
    atracoes = RecursoSerializer(many=True)
    avaliacoes = AvaliacaoSerializer(many=True)
    comentarios = ComentarioSerializer(many=True)
    endereco = EnderecoSerializer()
    descricao_completa = SerializerMethodField()


    class Meta:
        model = PontoTuristico
        fields = '__all__'
        extra_fields = ['descricao_completa',]

    def get_descricao_completa(self, obj):
        return '%s -> %s' % (obj.nome, obj.descricao)
