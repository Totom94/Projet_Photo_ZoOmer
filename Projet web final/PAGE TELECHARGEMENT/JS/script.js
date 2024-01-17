function downloadFile() {
    var link = document.createElement("a");
    link.href = "chemin_vers_fichier";
    link.download = "Photo_ZoOMER.jpg";
    link.click();
  }