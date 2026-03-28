from django import forms
from .models import *
class LivreForm(forms.ModelForm):

    statuts = {
        "disponible": "Disponible",
        "emprunte": "Emprunté",
        "reserve": "Réservé",
        "perdu": "Perdu",
        "endommage": "Endommagé"
    }


    isbn = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder":'ISBN'}),
        required=True
    )
    titre = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder":'Titre'}),
        required=True
    )
    auteur = forms.ModelChoiceField(
        queryset= Auteur.objects.all(),
        widget=forms.Select(attrs={"class": "form-control", "placeholder":'Auteur'}),
        required=True
    )
    genre = forms.ModelChoiceField(
        queryset= Genre.objects.all(),
        widget=forms.Select(attrs={"class": "form-control", "placeholder":'Genre'}),
        required=True
    )
    
    
    nbr_exemplaires = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder":'Nombre d\'exemplaires'}),
        required=True
    )
    annee_publication = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder":'Année de publication'}),
        required=True
    )
    statut = forms.CharField(
        widget=forms.Select(attrs={"class": "form-control"}, choices=statuts),
        required=True
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "placeholder":'Description'}),
        required=False
    )
    class Meta:
        model = Livre
        fields = [
            "isbn",
            "titre",
            "auteur",
            "nbr_exemplaires",
            "genre",
            "annee_publication",
            "statut",
            'description'
        ]

         