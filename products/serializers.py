from rest_framework import serializers
from .models import Product#   Al haber muchos 'models' de apps, se coloca el '.' para una busqueda en la carpeta

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product #   Decirle al traductor en que modelo debe basarse
        fields = '__all__'  #   Decirle que por ahora, queremos que traduzca todo los campos del modelo
