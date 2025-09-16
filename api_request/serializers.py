from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    fechaNacimiento = serializers.CharField(source='fecha_nacimiento')
    ultimosDigitosTarjeta = serializers.CharField(source='ultimos_digitos_tarjeta')
    
    class Meta:
        model = Usuario
        fields = ['nombre', 'cedula', 'fechaNacimiento', 'ultimosDigitosTarjeta', 'saldo']