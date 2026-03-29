from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count
from .models import *
from utilisateurs.models import *
from livres.models import *
from .forms import *
from django.contrib import messages
from datetime import date
from django.db.models import Q, F
 
def emprunter_via_utilisateur(request, id):
    message = ""
    utilisateur = get_object_or_404(Utilisateur, pk=id)
    emprunts = Emprunt.objects.filter(utilisateur=utilisateur, date_retour__isnull=True)
    if request.method == 'POST':
        form = CreateEmpruntForm(request.POST)
        if form.is_valid():
            
            emprunt = form.save(commit=False)
            livre = emprunt.livre
            a_emprunte = Emprunt.objects.filter(utilisateur=utilisateur, date_retour__isnull=True, livre=livre)# pour voir si cet utilisateur n'a pas emprunter ce livre
           
            if est_dispo(livre.id):
                if not a_emprunte :
                    reponse = peut_emprunter(utilisateur.id)
                    if reponse["decision"] == True:
                        livre.nbr_exemplaires -= 1
                        if livre.nbr_exemplaires <=0 :
                            livre.statut = "emprunte"
                            livre.save()
                        emprunt.utilisateur = utilisateur
                        emprunt.save()
                        messages.success(request,"Emprunt ajouté avec succès !")
                        return redirect("emprunts-utilisateur", id=utilisateur.id)
                    else:
                        messages.error(request,f"Cet utilisateur a un statut {utilisateur.statut} il ne peut avoir plus de {reponse["nbr_emprunt"]} emprunts.\nQuota atteint. ")
                else:
                    messages.error(request,"Cet utilisateur a déjà emprunté ce livre")
            else:
                messages.error(request,"Ce livre n'est pas disponoble")
    else:
        form = CreateEmpruntForm()

    context = {
        'form': form,
        'utilisateur': utilisateur,
        'message' : message
    }

    return render(request, "emprunts/emprunt-add.html", context)


def emprunts_historiques(request,id):
    utilisateur = get_object_or_404(Utilisateur,pk=id)
    emprunts = Emprunt.objects.filter(utilisateur=utilisateur, date_retour__isnull=False)
    context = {
        "utilisateur": utilisateur,
        "emprunts":emprunts
    }
    return render(request,"emprunts/emprunts-historiques.html", context)

def emprunts_utilisateur(request,id):
    
    utilisateur = get_object_or_404(Utilisateur,pk=id)
    emprunts = Emprunt.objects.filter(utilisateur=utilisateur, date_retour__isnull=True)
    tday = date.today()
    retards = Emprunt.objects.filter(utilisateur=utilisateur, date_retour__isnull=True, date_retour_prevue__lt=tday).count()
   
    context = {
        "utilisateur": utilisateur,
        "emprunts":emprunts,
        "retards": retards,
        
    }
    return render(request,"emprunts/emprunts-utilisateur.html", context)

def emprunts_utilisateur_retard(request,id):
    utilisateur = get_object_or_404(Utilisateur,pk=id)
    tday = date.today()
    emprunts = Emprunt.objects.filter(utilisateur=utilisateur, date_retour__isnull=True, date_retour_prevue__lt=tday)
    
    context = {
        "utilisateur": utilisateur,
        "emprunts":emprunts
    }
    return render(request,"emprunts/emprunts-utilisateur-retards.html", context)


def retourner_via_utilisateur(request, id):
    message = ""
    emprunt = get_object_or_404(Emprunt,pk=id)
    utilisateur = emprunt.utilisateur
    livre = emprunt.livre
    if livre and utilisateur:

        livre.nbr_exemplaires += 1
        livre.statut = "disponible"
        livre.save()

        emprunt.date_retour = date.today()
        if emprunt.date_retour_prevue < emprunt.date_retour:
            emprunt.statut = "retard"
        else:
            emprunt.statut = "retourne"
        emprunt.save()

        messages.success(request,"Livre retourné avec succès !")
    emprunts = Emprunt.objects.filter(utilisateur=utilisateur, date_retour__isnull=True)
    context = {
        "utilisateur": utilisateur,
        "emprunts":emprunts,
        message:"message"
    }
    return render(request,"emprunts/emprunts-utilisateur.html", context)

#Dashboard des emprunts
def top_5_livres():
    
    livres = Livre.objects.annotate(nbr_emprunt=Count("emprunts")).order_by("-nbr_emprunt")[:5]
    liste = [{"rang":i+1,"titre":livre.titre,"auteur":livre.auteur,"genre":livre.genre,"nbr_emprunt":livre.nbr_emprunt} for i,livre in enumerate(livres)]
    return liste
     
def dashboard(request):
    nb_livres = Livre.objects.count()
    nb_utilisateurs = Utilisateur.objects.count()
    nb_emprunts = Emprunt.objects.count()
    top_5 = top_5_livres()
    tday = date.today()
    emprunts_encours = Emprunt.objects.filter(date_retour__isnull=True).count()
    emprunts_retads = Emprunt.objects.filter(date_retour__gt=F("date_retour_prevue")).count()
    
    context = {
        "nb_livres": nb_livres,
        "nb_utilisateurs": nb_utilisateurs,
        "nb_emprunts": nb_emprunts,
        "top_5": top_5,
        "emprunts_encours": emprunts_encours,
        "emprunts_retads": emprunts_retads,
        
    }

    return render(request, "dashboard.html", context)

#=================================Livres fonction=================================
def est_dispo(livre_id):
    livre = get_object_or_404(Livre,pk=livre_id)
    if livre.statut == "disponible" and livre.nbr_exemplaires > 0:
        return True
    else:
        return False



#========================Utilisateur====================
def peut_emprunter(id):
    reponse = {
        "statut" : "etudiant",
        "nbr_emprunt": 0,
        "decision" : True
    }
    utilisateur = get_object_or_404(Utilisateur,pk=id)
    nbr_emprunt = Emprunt.objects.filter(utilisateur=utilisateur, date_retour__isnull=True).count()
    if utilisateur.statut == "etudiant" and nbr_emprunt >= 3:
        reponse["nbr_emprunt"] = 3
        reponse["decision"] = False
    elif utilisateur.statut == "enseignant" and nbr_emprunt >= 5:
        reponse["statut"] = "enseignant"
        reponse["nbr_emprunt"] = 5
        reponse["decision"] = False
    elif utilisateur.statut == "personnel" and nbr_emprunt >= 7:
        reponse["statut"] = "personnel"
        reponse["nbr_emprunt"] = 7
        reponse["decision"] = False
    
    return reponse