from django.urls import path
from .views import *
urlpatterns = [
    path("create-utilisateur/", create_utilisateur,name="create-utilisateur"),
    path("liste-utilisateurs/", read_utilisateurs,name="liste-utilisateurs"),
    path("update-utilisateur/<int:id>", update_utilisateur,name="update-utilisateur"),
    path("details-utilisateur/<int:id>", details_utilisateur,name="details-utilisateur"),
    path("supprimer-utilisateur/<int:id>", supprimer_utilisateur,name="supprimer-utilisateur"),
    path("success/", success_view, name="success"),

]
