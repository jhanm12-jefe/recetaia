from administracion.models import Rol, User, Suscripcion
from rest_framework import serializers

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model= Rol
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    rol = RolSerializer(read_only=True)
    
    rol_id = serializers.PrimaryKeyRelatedField(
        queryset = Rol.objects.all(),
        source = 'rol',write_only=True
    )
    class Meta:
        model= User
        fields = '__all__'        
        
class SuscripcionSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(read_only=True)
    usuario_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='usuario',
        write_only=True
    )

    class Meta:
        model = Suscripcion
        fields = '__all__'