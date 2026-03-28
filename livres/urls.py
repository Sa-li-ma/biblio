from django.urls import path
from .views import *
urlpatterns = [
    path("create-livre/", create_livre,name="create-livre"),
    path("liste-livres/", read_livres,name="liste-livres"),
    path("update-livre/<int:id>", update_livre,name="update-livre"),
    path("details-livre/<int:id>", details_livre,name="details-livre"),
    path("supprimer-livre/<int:id>", supprimer_livre,name="supprimer-livre"),
    path("success/", success_view, name="success"),
    path("menu/", menu, name="menu"),
    path("", accueil, name="accueil"),
]
