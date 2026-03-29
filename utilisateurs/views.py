from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from emprunts.forms import *
from django.db.models import Q

def success_view(request):

    return render(request,"utilisateurs/success.html")
def create_utilisateur(request):
    form = UtilisateurForm()
    
    if request.method == "POST":
        form = UtilisateurForm(request.POST)
        if form.is_valid():
            utilisateur = form.save(commit=False)
            utilisateur.save()
            return redirect("liste-utilisateurs")
        
    context = {
        "form": form
    }

    return render(request,"utilisateurs/utilisateur-add.html",context)

def details_utilisateur(request, id):
    
    utilisateur = get_object_or_404(Utilisateur,pk=id)
    context = {
        "utilisateur":utilisateur
    }
    return render(request,"utilisateurs/utilisateur-details.html",context)

def read_utilisateurs(request):
    if request.method == "POST":
        mots = request.POST.get("recherche", "").split()
        champs = ["matricule", "prenom", "nom", "statut"]

        filtre = Q()

        for mot in mots:
            for champ in champs:
                filtre |= Q(**{f"{champ}__icontains": mot})

        utilisateurs = Utilisateur.objects.filter(filtre)
    else :
        utilisateurs = Utilisateur.objects.all()
    context = {
        "utilisateurs":utilisateurs
    }
    return render(request,"utilisateurs/utilisateurs-liste.html",context)


def update_utilisateur(request,id):
    utilisateur = get_object_or_404(Utilisateur, pk=id)
    form = UtilisateurForm(instance=utilisateur)
    if request.method == "POST":
        form = UtilisateurForm(request.POST,instance=utilisateur)
        if form.is_valid():
            form.save()
            return redirect("liste-utilisateurs")
    context = {
        "form": form
    }

    return render(request,"utilisateurs/utilisateur-update.html",context)

def supprimer_utilisateur(request, id):
    utilisateur = get_object_or_404(Utilisateur, pk=id)

    if request.method == "POST":
        utilisateur.delete()
        return redirect("liste-utilisateurs")

    return redirect("liste-utilisateurs")


