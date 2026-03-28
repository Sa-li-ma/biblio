from django import forms

from .models import *

class UtilisateurForm(forms.ModelForm):
    STATUT_CHOICES = [
        ("etudiant", "Etudiant"),
        ("enseignant", "Enseignant"),
        ("personnel", "Personnel administratif"),
    ]

    prenom = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder":'Prenom'}),
        required=True
    )
    nom = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder":'Nom'}),
        required=True
    )

    statut = forms.CharField(
        widget=forms.Select(attrs={"class": "form-control"}, choices=STATUT_CHOICES),
        required=True
    )

    class Meta:
        model = Utilisateur
        fields = [
            "prenom",
            "nom",
            "statut"
        ]