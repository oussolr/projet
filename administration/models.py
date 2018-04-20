from django.db import models



class Annee_Scolaire(models.Model):
    Annee = models.DateField()
    Specialite = models.CharField(max_length=30)
    Moy_G = models.FloatField()
    Moy_S1 = models.FloatField()
    Moy_S1 = models.FloatField()

class Etudiant(models.Model):
    Nom = models.CharField(max_length=30)
    Prenom = models.CharField(max_length=30)
    Date_De_Naissance = models.DateField()
    Email = models.EmailField()
    Annee_Scolaire = models.ForeignKey(Annee_Scolaire, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nom + ' - ' + self.Prenom


class Entreprise(models.Model):
    Nom = models.CharField(max_length=30)
    Ntel = models.IntegerField()
    Email = models.EmailField()
    Description = models.CharField(max_length=300)
    Logo = models.ImageField(default='default.png', blank=True)
    P_Couverture = models.ImageField(default='default.png', blank=True)


class Encadreur(models.Model):
    Nom = models.CharField(max_length=30)
    Prenom = models.CharField(max_length=30)
    Date_De_Naissance = models.DateField()
    Email = models.EmailField()

class Stage_Propose(models.Model):
    Durée = models.DurationField()
    theme = models.CharField(max_length=30)
    Date_limite = models.DateField()

    Entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)

class Raport(models.Model):
    Description = models.CharField(max_length=30)

class Suivi_Stage(models.Model):
    Assiduité = models.IntegerField()
    Remarque = models.CharField(max_length=30)

class Payement(models.Model):
    Frais_De_Dejeuner = models.FloatField()
    Frais_De_Diner = models.FloatField()
    Frais_Dhebergement = models.FloatField()

class Stage (models.Model):
    Etat = models.CharField(max_length=30,default='en cour')
    Date_debut = models.DateField()
    Date_fin = models.DateField()
    Type_De_Stage = models.CharField(max_length=30)
    Stage_Propose = models.ForeignKey(Stage_Propose, on_delete=models.CASCADE)
    Raport = models.ForeignKey(Raport, on_delete=models.CASCADE)
    Suivi_Stage = models.ForeignKey(Suivi_Stage, on_delete=models.CASCADE)
    Payement = models.ForeignKey(Payement, on_delete=models.CASCADE)
    Encadreur = models.ForeignKey(Encadreur, on_delete=models.CASCADE)
    Etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)

