from tkinter import *  # Pour créer l'interface graphique
from tkinter import filedialog, messagebox   # Pour afficher des boîtes de dialogue
from azure.cognitiveservices.vision.computervision import ComputerVisionClient  # Pour créer un client pour l'API de reconnaissance de texte
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes  # Pour gérer les codes de statut de l'analyse
from msrest.authentication import CognitiveServicesCredentials  # Pour authentifier le client
import os  # Pour manipuler les fichiers
import time  # Pour gérer les délais d'attente
import subprocess  # Pour lancer l'application Caméra Windows
import pyautogui  # Pour simuler des clics de souris
from PIL import ImageTk, Image


# Créer un client pour l'API de reconnaissance de texte
subscription_key = "0000"                                   #(A VOUS DE METTRE VOS INFOS)
endpoint = "https://endpoint.com/"                          #(A VOUS DE METTRE VOS INFOS)
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

# Fonction pour lancer l'analyse OCR sur une image
def azure_ocr(local_image_path):
    with open(local_image_path, "rb") as image:
        read_response = computervision_client.read_in_stream(image, raw=True)  # Analyse OCR de l'image
    read_operation_location = read_response.headers["Operation-Location"]  # Récupérer l'URL de l'analyse
    operation_id = read_operation_location.split("/")[-1]   # Récupérer l'ID de l'analyse
    while True:
        read_result = computervision_client.get_read_result(operation_id) # Récupérer le résultat de l'analyse
        if read_result.status not in ['notStarted', 'running']: # Si l'analyse est terminée, sortir de la boucle
            break
        time.sleep(1)
    return read_result  # Retourner le résultat de l'analyse


# Fonction pour extraire le texte d'un résultat d'analyse OCR
def extract_text(read_result):
    lines = []
    if read_result.status == OperationStatusCodes.succeeded:  # Si l'analyse est terminée
        for text_result in read_result.analyze_result.read_results:  # Pour chaque texte extrait
            for line in text_result.lines:  # Pour chaque ligne de texte
                lines.append(line.text)  # Ajouter le texte de la ligne à la liste
    return "\n".join(lines)  # Retourner le texte extrait sous forme d'une chaîne de caractères


# Fonction pour sauvegarder le texte extrait dans un fichier
def sauvegarder_texte(texte, chemin_sauvegarde):
    nom_fichier = f"extraction_{time.strftime('%Y%m%d_%H%M%S')}.txt"  # Nom du fichier de sauvegarde (utilisation du format de date/heure actuel pour le rendre unique)
    chemin_fichier = os.path.join(chemin_sauvegarde, nom_fichier)  # Chemin complet du fichier de sauvegarde
    with open(chemin_fichier, "w") as fichier:  # Écrire le texte extrait dans le fichier
        fichier.write(texte)  # Écrire le texte extrait dans le fichier
    print(f"Le texte extrait a été sauvegardé dans le fichier : {chemin_fichier}")  # Afficher le chemin du fichier de sauvegarde


# Fonction pour prendre une photo avec la caméra de l'ordinateur
def take_photo():
    # Afficher la boîte de dialogue pour sélectionner le répertoire de sauvegarde
    directory = filedialog.askdirectory(parent=root, title='Sélectionner le répertoire de sauvegarde')
    if not directory:
        return
    photo_path = directory  # Chemin du répertoire de sauvegarde
    print("Ouverture de l'application Caméra Windows...")
    subprocess.Popen('explorer.exe shell:AppsFolder\Microsoft.WindowsCamera_8wekyb3d8bbwe!App') # Lancer l'application Caméra Windows
    pyautogui.sleep(5) # Attendre 5 secondes
    print("Clic sur le bouton pour prendre une photo...")
    pyautogui.click(x=960, y=540)  # Clic sur le bouton pour prendre une photo
    pyautogui.sleep(10) # Attendre 10 secondes
    print("Fermeture de l'application Caméra Windows...")
    subprocess.call('taskkill /IM WindowsCamera.exe /F')
    time.sleep(2)
    print("Récupération de la dernière photo prise...")
    photos = [f for f in os.listdir(photo_path) if os.path.isfile(os.path.join(photo_path, f)) and f.lower().endswith(('.jpg', '.jpeg', '.png')) and f.lower() != 'desktop.ini'] # Liste des fichiers du répertoire de sauvegarde
    latest_photo = max(photos, key=lambda x: os.path.getmtime(os.path.join(photo_path, x))) # Nom du fichier le plus récent
    file_name = os.path.join(photo_path, latest_photo) # Chemin du fichier le plus récent
    print("Nom du fichier le plus récent :", latest_photo)
    ocr_analysis = azure_ocr(file_name)
    extracted_text = extract_text(ocr_analysis)
    print("Texte extrait de l'analyse OCR :\n", extracted_text)
    # Afficher le texte extrait dans l'interface
    text_area.delete("1.0", END)
    text_area.insert(END, extracted_text)
    # Sauvegarder le texte extrait dans un fichier
    sauvegarder_texte(extracted_text, directory)


# Fonction pour sélectionner une image depuis le gestionnaire de fichiers
def select_image():
    choice = filedialog.askopenfilename(parent=root, initialdir="/", title='Veuillez sélectionner une image', filetypes=[('Image Files', '*.jpg *.jpeg *.png')]) # Afficher la boîte de dialogue pour sélectionner une image
    if not choice:
        return
    if choice.endswith(('.jpg', '.jpeg', '.png')):
        file_name = choice # Chemin du fichier sélectionné
        chemin = "Chemin du fichier sélectionné :"+ file_name
        affichage = Label(root, width=200, text=chemin)
        affichage.grid(row=3, column=1)
        ocr_analysis = azure_ocr(file_name)
        extracted_text = extract_text(ocr_analysis)
        print("Texte extrait de l'analyse OCR :\n", extracted_text)
        # Afficher le texte extrait dans l'interface
        text_area.delete("1.0", END)
        text_area.insert(END, extracted_text)
        # Sauvegarder le texte extrait dans un fichier
        sauvegarder_texte(extracted_text, os.path.dirname(file_name))


# Créer la fenêtre principale
root = Tk()
root.title("OCR Analyzer")

img = ImageTk.PhotoImage(Image.open("Logo Projet transversemini.png"))
label = Label(image = img, )
label.grid(row =0, column= 0 )

# Bouton pour sélectionner une image
select_button = Button(root, text="Sélectionner une image", command=select_image)
select_button.grid(row = 0, column=1)

# Bouton pour prendre une photo
capture_button = Button(root, text="Prendre une photo", command=take_photo)
capture_button.grid(row= 1, column=1)

# Zone de texte pour afficher le texte extrait
text_area = Text(root, blockcursor=True, height=90 , width=90)
text_area.grid(row = 5, column=1)
text_area.config(font=("Arial", 16))

# Lancer la boucle principale de l'interface graphique
root.mainloop()