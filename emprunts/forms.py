from django import forms
from utilisateurs.models import *
from livres.models import *
from .models import *

class CreateEmpruntForm(forms.ModelForm):

    livre = forms.ModelChoiceField(
        queryset=Livre.objects.filter(statut="disponible"),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=True
    )

    date_retour_prevue = forms.DateField(
        widget=forms.DateInput(attrs={
            "class": "form-control",
            "type": "date"
        }),
        required=True
    )

    class Meta:
        model = Emprunt
        fields = [
            'livre',
            'date_retour_prevue'
        ]