from rest_framework import serializers
from api.models import Alumno,Profesor,Materia,Curso,gestion,dato,tipo_dato,User,Administrativo
from rest_framework.authtoken.models import Token



        

class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = '__all__'
        read_only_fields = ('created_at',)

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'
        read_only_fields = ('created_at',)

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = '__all__'       

class AdministrativoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrativo
        fields = '__all__'      

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'username','email','is_Alumno','is_Profesor','is_staff']

class AdministrativoSignupSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":"password"}, write_only=True)
    class Meta:
        model = User
        fields = ['username','email','password','password2']
        extra_kwargs={
            'password' :{'write_only':True}
        }
    def save (self, **kwargs):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password=self.validated_data['password'] 
        password2=self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({"error":"contraseñas no coinciden"})
        user.set_password(password)
        user.is_staff=True
        user.save()
        Administrativo.objects.create(user=user)
        return user

class AlumnoSignupSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":"password"}, write_only=True)
    class Meta:
        model = User
        fields = ['username','email','password','password2']
        extra_kwargs={
            'password' :{'write_only':True}
        }
    def save (self, **kwargs):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password=self.validated_data['password'] 
        password2=self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({"error":"contraseñas no coinciden"})
        user.set_password(password)
        user.is_Alumno=True
        user.save()
        Alumno.objects.create(user=user)
        return user


class ProfesorSignupSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":"password"}, write_only=True)
    class Meta:
        model = User
        fields = ['username','email','password','password2']
        extra_kwargs={
            'password' :{'write_only':True}
        }
    def save (self, **kwargs):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({"error":"contraseñas no coinciden"})
        user.set_password(password)
        user.is_Profesor=True
        user.save()
        Profesor.objects.create(user=user)
        return user

class DatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = dato
        fields = '__all__'
        extra_kwargs = {
            'fecha': {'read_only': True, 'required': False},
            # 'fecha': {'read_only': True},
        }   

class Tipo_DatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipo_dato
        fields = '__all__'


class GestiopnSerializer(serializers.ModelSerializer):
    class Meta:
        model = gestion
        fields = '__all__'




        