from django.contrib import admin

# Register your models here.
from .models import Adresse, Etudiant, Entreprise, Encadreur

admin.site.register(Adresse)
admin.site.register(Etudiant)
admin.site.register(Entreprise)
admin.site.register(Encadreur)