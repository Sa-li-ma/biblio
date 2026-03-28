/* Ajout produit*/
var addLivreModal = document.getElementById('addLivreModal')
var addLivreInput = document.getElementById('addLivreInput')

addLivreModal.addEventListener('shown.bs.modal', function () {
  addLivreInput.focus()
})

/* modif produit*/
var updateLivreModal = document.getElementById('updateLivreModal')
var updateLivreInput = document.getElementById('updateLivreInput')

updateLivreModal.updateEventListener('shown.bs.modal', function () {
  updateLivreInput.focus()
})
/* details produit*/
var detailsLivreModal = document.getElementById('detailsLivreModal')
var detailsLivreInput = document.getElementById('detailsLivreInput')

detailsLivreModal.detailsEventListener('shown.bs.modal', function () {
  detailsLivreInput.focus()
})
/* delete produit*/
var deleteLivreModal = document.getElementById('deleteLivreModal')
var deleteLivreInput = document.getElementById('deleteLivreInput')

deleteLivreModal.deleteEventListener('shown.bs.modal', function () {
  detailsLivreInput.focus()
})





/* Ajout produit*/
var addutilisateurModal = document.getElementById('addutilisateurModal')
var addutilisateurInput = document.getElementById('addutilisateurInput')

addutilisateurModal.addEventListener('shown.bs.modal', function () {
  addutilisateurInput.focus()
})

/* modif produit*/
var updateutilisateurModal = document.getElementById('updateutilisateurModal')
var updateutilisateurInput = document.getElementById('updateutilisateurInput')

updateutilisateurModal.updateEventListener('shown.bs.modal', function () {
  updateutilisateurInput.focus()
})
/* details produit*/
var detailsutilisateurModal = document.getElementById('detailsutilisateurModal')
var detailsutilisateurInput = document.getElementById('detailsutilisateurInput')

detailsutilisateurModal.detailsEventListener('shown.bs.modal', function () {
  detailsutilisateurInput.focus()
})
/* delete produit*/
var deleteutilisateurModal = document.getElementById('deleteutilisateurModal')
var deleteutilisateurInput = document.getElementById('deleteutilisateurInput')

deleteutilisateurModal.deleteEventListener('shown.bs.modal', function () {
  detailsutilisateurInput.focus()
})

