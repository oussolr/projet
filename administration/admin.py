from django.contrib import admin

# Register your models here.
from .models import Etudiant, Entreprise, Encadreur, Stage_Propose

admin.site.register(Etudiant)
admin.site.register(Entreprise)
admin.site.register(Encadreur)
admin.site.register(Stage_Propose)