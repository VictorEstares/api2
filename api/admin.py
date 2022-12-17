from django.contrib import admin
from .models import Alumno,Profesor,gestion,Curso,Materia,dato,tipo_dato,User,Administrativo

admin.site.register(User)
admin.site.register(Alumno)
admin.site.register(Administrativo)
admin.site.register(Profesor)
admin.site.register(gestion)
admin.site.register(Curso)
admin.site.register(Materia)
admin.site.register(dato)
admin.site.register(tipo_dato)
# Register your models here.
