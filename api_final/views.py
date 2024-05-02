from django.shortcuts import render
import json
from rest_framework.response import Response
from rest_framework import status, permissions
from api_final.models import contenido
from api_final.seralizer import contenido_serializer
from rest_framework.views import APIView

# Create your views here.
class contenido_api_view(APIView):
    def post(self, request, *args, **kwargs):
        data={
            'nombre': request.data.get('nombre'),
            'genero': request.data.get('genero'),
            'duracion': request.data.get('duracion'),
            'descripcion': request.data.get('descripcion'),
            'actores':request.data.get('actores'),
            'directores':request.data.get('directores'),
        }
        serializador=contenido_serializer(data=data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data,status=status.HTTP_200_OK)
        return Response(serializador.data,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request,*args,**kwargs):
        lista_contedio=contenido.objects.all()
        serializer_contenido=contenido_serializer(lista_contedio,many=True)
        return Response(serializer_contenido.data,status=status.HTTP_200_OK)
    def put(self,request,pkid):
        contenido_consultado=contenido.objects.filter(id=pkid).update(
            nombre=request.data.get("nombre"),
            genero=request.data.get("genero"),
            duracion=request.data.get("duracion"),
            descripcion=request.data.get("descripcion"),
            actores=request.data.get("actores"),
            directores=request.data.get("directores"),
        )
        return Response(contenido_consultado,status=status.HTTP_200_OK)
    def delete(self,request,pkid):
        contenido_consultado=contenido.objects.filter(id=pkid).delete()
        return Response(contenido_consultado,status=status.HTTP_200_OK)

    