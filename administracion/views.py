from django.shortcuts import render
from administracion.models import Rol
from administracion.serializers import RolSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET'])
def prueba(request):
    respuesta = "hola mundo"
    return Response(respuesta)

@api_view(['GET','POST'])
def crudRol(request):
    if request.method == 'GET':
        rols = Rol.objects.all()
        serializer = RolSerializer(rols, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RolSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error)