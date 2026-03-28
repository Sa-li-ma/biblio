from django.db import models
class Auteur(models.Model):
    nom = models.CharField(max_length=150)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.nom
    

class Genre(models.Model):
    nom = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    def __str__(self):
        return self.nom

class Livre(models.Model):

    statuts = {
        "disponible": "Disponible",
        "emprunte": "Emprunté",
        "reserve": "Réservé",
        "perdu": "Perdu",
        "endommage": "Endommagé"
    }

    isbn = models.CharField(max_length=20)
    titre = models.CharField(max_length=200)
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE, related_name="livres")
    annee_publication = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="livres")
    nbr_exemplaires = models.IntegerField()
    statut = models.CharField(choices=statuts)
    description = models.CharField(max_length=600, default="...")
    def __str__(self):
        return self.titre
