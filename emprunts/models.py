from django.db import models

from livres.models import *
from utilisateurs.models import *

class Emprunt(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE, related_name="emprunts")

    date_emprunt = models.DateField(auto_now_add=True)
    date_retour_prevue = models.DateField()
    date_retour = models.DateField(null=True, blank=True)

    statut = models.CharField(
        max_length=20,
        choices=[
            ("en_cours", "En cours"),
            ("retourne", "Retourné"),
            ("retard", "En retard")
        ],
        default="en_cours"
    )

    def __str__(self):
        return f"{self.utilisateur.matricule} : {self.livre.titre}"