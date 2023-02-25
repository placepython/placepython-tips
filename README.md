# Astuces PlacePython

Le projet herbergé dana ce dépôt a servi de support au WePynaire que j'ai donné en février 2023 sur le déploiement d'une application Python sur un VPS Linux. Pour utiliser et tester ce projet, il faut **installer pipenv** et suivre les étapes suivantes:

1. Cloner ce dépôt de code et ouvrir un terminal à la racine du projet
2. Renommer le fichier env_sqlite3 en .env
2. Installer les dépendances avec la commande `pipenv install` (ou en production `pipenv install --categories production`)
3. Activer l'environnement virtuel avec la commande `pipenv shell`
4. Exécuter les migrations à l'aide de la commande `python manage.py migrate`
5. Créer un superutilisateur à l'aide de la commande `python manage.py createsuperuser`. Répondre aux questions posées.
6. Charger les données de test à l'aide de `python loaddata tips`

