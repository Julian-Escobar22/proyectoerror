from api_final.models import contenido
from rest_framework import serializers

class contenido_serializer(serializers.ModelSerializer):
    class Meta:
        model=contenido
        fields=('id','nombre','genero','duracion','descripcion','actores','directores')