from rest_framework import serializers
from core.models import Cliente
from core.models import Juego

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__' #traer todos las columnas de la BD

class ClientePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'ciudad', 'edad', 'fono']

class JuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juego
        fields = '__all__' #traer todos las columnas de la BD

class JuegoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juego
        fields = ['Id_categoria', 'descripcion_juego']