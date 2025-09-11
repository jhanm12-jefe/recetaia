from django.shortcuts import render
from administracion.models import Rol, User , Suscripcion
from administracion.serializers import RolSerializer,UserSerializer, SuscripcionSerializer
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
    
@api_view(['GET','PUT','DELETE'])    
def crudRol_detail(request,id):
    try:
        rol = Rol.objects.get(pk = id)
    except Rol.DoesNotExist:
        return Response("rol no encontrado", status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = RolSerializer(rol)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = RolSerializer(rol, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    if request.method == 'DELETE':
        rol.delete()
        return Response("eliminar con exito")
    
    
      
@api_view(['GET','POST'])
def crudUser(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error)
    
@api_view(['GET','PUT','DELETE'])    
def crudUser_detail(request,id):
    try:
        user = User.objects.get(pk = id)
    except User.DoesNotExist:
        return Response("user no encontrado", status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = UserSerializer(user, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    if request.method == 'DELETE':
        user.delete()
        return Response("eliminar con exito")
    
@api_view(['GET','POST'])
def crudSuscripcion(request):
    if request.method == 'GET':
        suscripciones = Suscripcion.objects.all()
        serializer = SuscripcionSerializer(suscripciones, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SuscripcionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def crudSuscripcion_detail(request, id):
    try:
        suscripcion = Suscripcion.objects.get(pk=id)
    except Suscripcion.DoesNotExist:
        return Response("suscripción no encontrada", status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SuscripcionSerializer(suscripcion)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = SuscripcionSerializer(suscripcion, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        suscripcion.delete()
        return Response("eliminada con éxito")