# Astuces PlacePython

Le projet herbergé dans ce dépôt a servi de support au WePynaire que j'ai donné en février 2023 sur le déploiement d'une application Python sur un VPS Linux. Pour utiliser et tester ce projet, il faut **installer pipenv** et suivre les étapes suivantes:

1. Cloner ce dépôt de code et ouvrir un terminal à la racine du projet
2. Renommer le fichier `.env-exemple` en `.env` et renseigner les données à l'intérieur
3. Créer un répertoire `.venv` vide
4. Installer les dépendances avec la commande `pipenv install`
5. Activer l'environnement virtuel à l'aide de la commande `pipenv shell`
6. Exécuter les migrations à l'aide de la commande `python manage.py migrate`
7. Créer un superutilisateur à l'aide de la commande `python manage.py createsuperuser`. Répondre aux questions posées.
8. Charger les données de test à l'aide de `python loaddata tips`

