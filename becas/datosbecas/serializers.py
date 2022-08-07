from rest_framework import serializers

from datosbecas.models import Becario, Estudio, Beca

class BecarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Becario
        fields = '__all__'

class EstudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudio
        fields = '__all__' 

class BecaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beca
        fields = '__all__'

        def to_representation(self, instance):
            response = super().to_representation(instance)
            response['becario'] = BecarioSerializer(instance.becario).data
            return response


