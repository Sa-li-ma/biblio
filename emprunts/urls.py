from django.urls import path
from .views import *
urlpatterns = [
    path("emprunt-via-utilisateur/<int:id>",emprunter_via_utilisateur, name="emprunt-via-utilisateur"),
    path("retour-via-utilisateur/<int:id>",retourner_via_utilisateur, name="retour-via-utilisateur"),
    path("emprunts-historiques/<int:id>",emprunts_historiques,name="emprunts-historiques"),
    path("emprunts-utilisateur/<int:id>",emprunts_utilisateur,name="emprunts-utilisateur"),
    path("emprunts-retads/<int:id>",emprunts_utilisateur_retard,name="emprunts-retads"),
    path("dashboard",dashboard,name="dashboard")
]
