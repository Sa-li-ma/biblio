from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.db.models import Q

def success_view(request):

    return render(request,"livres/success.html")

def accueil(request):
    
    return render(request, "home.html")


def create_livre(request):
    form = LivreForm()
    
    if request.method == "POST":
        form = LivreForm(request.POST)
        if form.is_valid():
            livre = form.save(commit=False)
            livre.save()
            return redirect("liste-livres")
        
    context = {
        "form": form
    }

    return render(request,"livres/livre-add.html",context)

def details_livre(request, id):

    livre = get_object_or_404(Livre,pk=id)
    context = {
        "livre":livre
    }
    return render(request,"livres/details.html",context)



def read_livres(request):
    if request.method == "POST":
        mots = request.POST.get("recherche", "").split()
        champs = ["isbn", "titre", "auteur__nom", "genre__nom"]

        filtre = Q()

        for mot in mots:
            for champ in champs:
                filtre |= Q(**{f"{champ}__icontains": mot})

        livres = Livre.objects.filter(filtre)

    else:
        livres = Livre.objects.all()

    context = {
        "livres": livres
    }

    return render(request, "livres/livres-liste.html", context)
def update_livre(request,id):
    livre = get_object_or_404(Livre, pk=id)
    form = LivreForm(instance=livre)
    if request.method == "POST":
        form = LivreForm(request.POST,instance=livre)
        if form.is_valid():
            form.save()
            return redirect("liste-livres")
    context = {
        "form": form
    }

    return render(request,"livres/livre-update.html",context)

def supprimer_livre(request, id):
    livre = get_object_or_404(Livre, pk=id)

    if request.method == "POST":
        livre.delete()
        return redirect("liste-livres")

    return redirect("liste-livres")


def menu(request):
    return render(request,"livres/menu.html")
