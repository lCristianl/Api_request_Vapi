from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario
from .serializers import UsuarioSerializer
import json

# Create your views here.

class UsuarioAPIView(APIView):
    """
    API View para buscar usuarios por cédula
    """
    
    def post(self, request):
        try:
            # Obtener la cédula del body de la request
            cedula = request.data.get('cedula')
            
            if not cedula:
                return Response({
                    "data": "",
                    "estatus": "error",
                    "mensaje": "La cédula es requerida"
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # Buscar el usuario por cédula
            try:
                usuario = Usuario.objects.get(cedula=cedula)
                serializer = UsuarioSerializer(usuario)
                
                return Response({
                    "data": serializer.data,
                    "estatus": "exitoso"
                }, status=status.HTTP_200_OK)
                
            except Usuario.DoesNotExist:
                # Si no existe el usuario, retornar data vacía
                return Response({
                    "data": "",
                    "estatus": "exitoso"
                }, status=status.HTTP_200_OK)
                
        except Exception as e:
            return Response({
                "data": "",
                "estatus": "error",
                "mensaje": f"Error interno del servidor: {str(e)}"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
