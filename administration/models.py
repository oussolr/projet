from django.db import models

class Adresse(models.Model):
    ville = models.CharField(max_length=30)
    Rue = models.CharField(max_length=30)
    N_lot = models.IntegerField()
    Code_Postal = models.IntegerField()
    Longitude = models.FloatField()
    Latitude = models.FloatField()


    def __str__(self):
        return self.Rue + ' - ' + self.ville

class Etudiant(models.Model):
    Nom = models.CharField(max_length=30)
    Prenom = models.CharField(max_length=30)
    Date_De_Naissance = models.DateField()
    Email = models.EmailField()
    Adresse = models.ForeignKey(Adresse, on_delete=models.CASCADE)
    Année_Scolaire = models.ForeignKey(Année_Scolaire, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nom + ' - ' + self.Prenom


class Entreprise(models.Model):
    Nom = models.CharField(max_length=30)
    Ntel = models.IntegerField()
    Email = models.EmailField()
    Description = models.CharField(max_length=300)
    Logo = models.ImageField(default='default.png', blank=True)
    P_Couverture = models.ImageField(default='default.png', blank=True)
    Adresse = models.ForeignKey(Adresse, on_delete=models.CASCADE)

class Année_Scolaire(models.Model):
    Année = models.DateField()
    Specialite = models.CharField(max_length=30)
    Moy_G = models.IntegerField()
    Moy_S1 = models.IntegerField()
    Moy_S1 = models.IntegerField()

class Encadreur(models.Model):
    Nom = models.CharField(max_length=30)
    Prenom = models.CharField(max_length=30)
    Date_De_Naissance = models.DateField()
    Email = models.EmailField()

class Stage_Propose(models.Model):
    Durée = models.IntegerField()
    theme = models.CharField(max_length=30)
    Date_limite = models.DateField()
    Adresse = models.ForeignKey(Adresse, on_delete=models.CASCADE)
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
    Etat = models.CharField()
    Date_debut = models.DateField()
    Date_fin = models.DateField()
    Type_De_Stage = models.CharField(max_length=30)
    Stage_Propose = models.ForeignKey(Stage_Propose, on_delete=models.CASCADE)
    Raport = models.ForeignKey(Raport, on_delete=models.CASCADE)
    Suivi_Stage = models.ForeignKey(Suivi_Stage, on_delete=models.CASCADE)
    Payement = models.ForeignKey(Payement, on_delete=models.CASCADE)
    Encadreur = models.ForeignKey(Encadreur, on_delete=models.CASCADE)
    Etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)

