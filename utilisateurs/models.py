from django.db import models

import uuid

class Utilisateur(models.Model):

    STATUT_CHOICES = [
        ("etudiant", "Etudiant"),
        ("enseignant", "Enseignant"),
        ("personnel", "Personnel administratif"),
    ]

    matricule = models.CharField(max_length=20, unique=True, editable=False)
    prenom = models.CharField(max_length=20)
    nom = models.CharField(max_length=20)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES)

    def save(self, *args, **kwargs):
        if not self.matricule:
            self.matricule = f"MAT-{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.prenom} {self.nom}"
    
