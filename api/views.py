from rest_framework import viewsets, permissions
from api.models import Administrativo,Materia,Curso,Alumno,gestion,Profesor,dato,tipo_dato
from api.serializers import AdministrativoSerializer,AdministrativoSignupSerializer,ProfesorSerializer,AlumnoSerializer,MateriaSerializer,CursoSerializer,AlumnoSignupSerializer,GestiopnSerializer,ProfesorSignupSerializer,DatoSerializer,Tipo_DatoSerializer ,UserSerializer
from rest_framework import status,views, response
from rest_framework import authentication,generics
from rest_framework.response import Response
from django.contrib.auth import logout ,authenticate, login 
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from api.permissions import is_Alumno,is_Profesor,is_AdminOrReadOnly

class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer
    permission_classes = [permissions.IsAuthenticated&permissions.IsAdminUser]
    authentication_classes = [authentication.TokenAuthentication,]

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    permission_classes = [permissions.IsAuthenticated&permissions.IsAdminUser]
    authentication_classes = [authentication.TokenAuthentication,]

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    permission_classes = [permissions.IsAuthenticated&permissions.IsAdminUser]
    authentication_classes = [authentication.TokenAuthentication,]


class AdministrativoViewSet(viewsets.ModelViewSet):
    queryset = Administrativo.objects.all()
    serializer_class = AdministrativoSerializer 
    permission_classes = [permissions.IsAuthenticated&permissions.IsAdminUser]
    authentication_classes = [authentication.TokenAuthentication,]
   
    
class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = ProfesorSerializer
    permission_classes = [permissions.IsAuthenticated&permissions.IsAdminUser]
    authentication_classes = [authentication.TokenAuthentication,]


class AlumnoSignupView(generics.GenericAPIView):
        serializer_class = AlumnoSignupSerializer
        permission_classes = [permissions.IsAuthenticated&permissions.IsAdminUser]
        authentication_classes = [authentication.TokenAuthentication,]

        def post (self, request, *args, **kwargs):
            serializer=self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user=serializer.save()
            return response.Response({
                "user":UserSerializer(user, context=self.get_serializer_context).data,
                "token":Token.objects.get(user=user).key,
                "message":"cuenta creada satisfactoriamente"
            },status=status.HTTP_200_OK)

class ProfesorSignupView(generics.GenericAPIView):
    serializer_class = ProfesorSignupSerializer
    permission_classes = [permissions.IsAuthenticated&permissions.IsAdminUser]
    authentication_classes = [authentication.TokenAuthentication,]

    def post (self, request, *args, **kwargs):
            serializer=self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user=serializer.save()
            return response.Response({
                "user":UserSerializer(user, context=self.get_serializer_context).data,
                "token":Token.objects.get(user=user).key,
                "message":"cuenta creada satisfactoriamente"
            },status=status.HTTP_200_OK)

class AdministrativoSignupView(generics.GenericAPIView):
    serializer_class = AdministrativoSignupSerializer
    permission_classes = [permissions.IsAuthenticated&permissions.IsAdminUser]
    authentication_classes = [authentication.TokenAuthentication,]

    def post (self, request, *args, **kwargs):
            serializer=self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user=serializer.save()
            return response.Response({
                "user":UserSerializer(user, context=self.get_serializer_context).data,
                "token":Token.objects.get(user=user).key,
                "message":"cuenta creada satisfactoriamente"
            },status=status.HTTP_200_OK)

class GestionViewSet(viewsets.ModelViewSet):
  queryset = gestion.objects.all()
  permission_classes = [permissions.IsAuthenticated&permissions.IsAdminUser]
  authentication_classes = [authentication.TokenAuthentication,]

  serializer_class = GestiopnSerializer

class DatoViewSet(viewsets.ModelViewSet):
  queryset = dato.objects.all()
  permission_classes = [permissions.IsAuthenticated&is_AdminOrReadOnly|permissions.IsAuthenticated&is_Profesor]
  authentication_classes = [authentication.TokenAuthentication,]

  serializer_class = DatoSerializer

class Tipo_DatoViewSet(viewsets.ModelViewSet):
  queryset = tipo_dato.objects.all()
  permission_classes = [permissions.IsAuthenticated&permissions.IsAdminUser]
  authentication_classes = [authentication.TokenAuthentication,]

  serializer_class = Tipo_DatoSerializer
  


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer=self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        token, created=Token.objects.get_or_create(user=user)
        return response.Response({
            'token':token.key,
            'user_id':user.pk,
            'is_Alumno':user.is_Alumno,

        })

class AdministrativoOnlyView(generics.RetrieveAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser&permissions.IsAuthenticated]
    serializer_class=UserSerializer

    def get_object(self):
        return self.request.user

class AlumnosOnlyView(generics.RetrieveAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes=[is_Alumno&permissions.IsAuthenticated]
    serializer_class=UserSerializer

    def get_object(self):
        return self.request.user

class ProfesorOnlyView(generics.RetrieveAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes=[is_Profesor&permissions.IsAuthenticated]
    serializer_class=UserSerializer

    def get_object(self):
        return self.request.user

class LogoutView(views.APIView):
    authentication_classes = [authentication.TokenAuthentication]
    def post(self, request):        
        request.user.auth_token.delete()
        # Borramos de la request la información de sesión
        logout(request)
        # Devolvemos la respuesta al cliente
        return response.Response({'message':'Sessión Cerrada y Token Eliminado !!!!'},status=status.HTTP_200_OK)