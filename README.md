# Projet Aide pour Malvoyants


Ce projet vise à faciliter l'accessibilité visuelle en développant une application de reconnaissance de textes et un site web accompagnateur. L'application, principalement codée en Python, permet de convertir des textes à partir d'images ou de photos, fournissant une version agrandie et nette pour les utilisateurs malvoyants. 

## Application

### Configuration de l'Application

1. Éditez le fichier `main.py` pour accéder à la configuration de l'application.
   
2. Téléchargez les packages nécessaires en exécutant la commande suivante :

    ```bash
    pip install azure msrest pyautogui pil
    ```

3. Remplacez l'endpoint et la clé de souscription par vos informations créées sur Microsoft Azure (OCR). Cette étape est cruciale pour garantir le bon fonctionnement de l'application.

### Exécution de l'Application

- Après avoir configuré les détails dans `main.py`, exécutez le programme en utilisant votre environnement Python. L'application devrait fonctionner correctement après ces étapes.

- Vous avez également la possibilité de créer directement un fichier exécutable (`.exe`) depuis votre IDE. Pour des instructions spécifiques, consultez [ce lien](https://stackoverflow.com/questions/19071910/how-to-my-exe-from-pycharm-project).

## Site Web

### Pages disponibles

1. **Page d'Accueil :**
   - Une brève explication du projet et de son objectif.

2. **Page À Propos :**
   - Informations sur le développeur et le contexte du projet.

3. **Page Satisfaction :**
   - Un espace pour recueillir les retours d'expérience des utilisateurs.

4. **Page Téléchargement :**
   - Contient un lien vers le téléchargement du fichier zip contenant un échantillon de l'application, y compris le fichier exécutable (`exe`).

### Remarque Importante

Le retour de l'OCR ne fonctionnera pas avec les informations actuelles en utilisant le .exe , car celles-ci ne sont plus valides pour les services Azure. Veuillez mettre à jour les informations Azure (endpoint et clé de souscription) pour permettre la fonctionnalité OCR de l'application.

Pour toute question ou problème, n'hésitez pas à me contacter. Merci de votre intérêt pour le projet !
