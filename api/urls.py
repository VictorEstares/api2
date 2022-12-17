from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from api.views import AdministrativoViewSet,AdministrativoOnlyView,AdministrativoSignupView,ProfesorViewSet,AlumnoViewSet,ProfesorOnlyView,AlumnosOnlyView,MateriaViewSet,CursoViewSet,AlumnoSignupView,GestionViewSet,ProfesorSignupView,DatoViewSet,Tipo_DatoViewSet, CustomAuthToken,LogoutView
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
router  = routers.DefaultRouter()
router.register('Curso', CursoViewSet)
router.register('Materia', MateriaViewSet)
router.register('Gestion',GestionViewSet)
router.register('Dato',DatoViewSet)
router.register('Tipo_Dato',Tipo_DatoViewSet),
router.register('Alumnos',AlumnoViewSet),
router.register('Profesores',ProfesorViewSet),
router.register('Administrativos',AdministrativoViewSet),


urlpatterns = [
    path('login/', CustomAuthToken.as_view(), name='auth-token'),
    path('logout/', LogoutView.as_view()),
    path('signup/Alumno/', AlumnoSignupView.as_view()),
    path('signup/Profesor/', ProfesorSignupView.as_view()),
    path('signup/Administrativo/', AdministrativoSignupView.as_view()),
    path('perfil/Alumno/', AlumnosOnlyView.as_view(), name="alumno-dashboard"),
    path('perfil/Profesor/', ProfesorOnlyView.as_view(), name="profesor-dashboard"),
    path('perfil/Administrativo/', AdministrativoOnlyView.as_view(), name="administrativo-dashboard")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + router.urls 