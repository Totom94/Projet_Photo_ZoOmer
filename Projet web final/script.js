document.addEventListener("DOMContentLoaded", function() {
    // Récupérer le formulaire, les éléments et le champ de commentaire
    var formulaire_satis = document.getElementById("satisfactionForm");
    var commentaire = document.getElementById("comment");
    var note_bouton = document.getElementById("sendRating");
  
    // Envoyer la note
    note_bouton.addEventListener("click", function() {
      // Récupérer valeur note
      var selection_note = document.querySelector('input[name="note"]:checked');
      if (selection_note) {
        var valeur_note = selection_note.value;
        alert("Votre note envoyée : " + valeur_note);
      } else {
        alert("Veuillez sélectionner une note valide");
      }
    });
  
    // Ajouter l'événement submit au formulaire
    formulaire_satis.addEventListener("submit", function(event) {
      // Vérifier présence commentaire
      if (commentaire.value === "" || commentaire.value === "Envoyez votre commentaire à notre équipe") {
        event.preventDefault(); // Empêcher envoi form
        alert("Veuillez entrer un commentaire valide");
      } else {
        alert("Merci pour votre commentaire !");
      }
    });
  });
  