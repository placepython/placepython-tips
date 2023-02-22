# Fichiers de configuration pour le serveur

Dans ce WePynaire, la stratégie de déploiement utilise une architecture courante dans le monde Django. Cette architecture se base sur l'usage
d'un serveur web et d'un serveur WSGI. Voici une illustration qui donne une vue d'ensemble du schéma:

![Diagramme de déploiement d'une application Django classique](https://i.gyazo.com/2057449649a2290960194096f06835e7.png)

## Le serveur WSGI

### Qu'est-ce que WSGI ?

WSGI (Web Server Gateway Interface) est une interface standardisée dans la PEP 333 ([comprendre WSGI grâce à ce WePynaire](https://youtu.be/fdA1RDgWLjY)). Ce standard fournit une spécification pour définir comment les serveurs web doivent communiquer avec les applications Python.

### Qu'est-ce qu'un serveur WSGI ?

Un **serveur WSGI** est un serveur web qui implémente l'interface WSGI et fournit un environnement d'exécution pour les applications web Python. Il est chargé de recevoir les requêtes HTTP du client, de les transmettre à l'application web pour traitement, puis de renvoyer les réponses HTTP générées par l'application au client.

Les serveurs WSGI les plus couramment utilisés avec les applications web Python sont gunicorn (utilisé dans ce WePynaire), uWSGI ou mod_wsgi (pour Apache). Ces serveurs prennent en charge l'exécution d'applications web Python développées avec diiférents frameworks tels que Django, Flask ou Fastcgi.

En résumé, **un serveur WSGI est un serveur web qui implémente l'interface standardisée WSGI pour communiquer avec des applications web Python**. Gunicorn, que nous installons avec la commande `pipenv install gunicorn`, est ainsi le serveur responsable de rendre notre application Django accessible sur le web. Il remplace la commande `python manage.py runserver`, utilisable uniquement lors du développement.

## Le serveur web Nginx

Nginx est un serveur web open-source très populaire utilisé pour servir des pages web statiques ou dynamiques sur internet. Il est particulièrement apprécié pour sa haute performance, sa capacité à gérer de nombreuses connexions simultanées, sa stabilité et sa faible consommation de ressources système.

Nginx peut être utilisé comme un serveur web autonome pour servir des fichiers html, des images et d'autres contenus statiques, ou **comme un serveur proxy inverse** pour acheminer le trafic web vers des applications Web telles que des serveurs d'application ou des serveurs de base de données. **C'est dans ce contexte que nous l'utilisons avec notre application Django**.

Il est tout à fait possible de déployer une application Django en utilisant uniquement un serveur d'application WSGI tel que Gunicorn. Cependant, l'utilisation de Nginx en tant que serveur proxy inverse peut présenter plusieurs avantages dans le contexte d'un déploiement d'application Django :

- **Amélioration de la sécurité** : Nginx peut être configuré pour agir comme un pare-feu et un proxy, offrant une couche de sécurité supplémentaire pour votre application Django. En utilisant Nginx, vous pouvez configurer des règles pour limiter l'accès à votre application, bloquer les requêtes malveillantes ou les attaques DoS ou DDoS (Deni de service ou deni de service distribué).
- **Performance améliorée** : Nginx peut être configuré pour gérer les connexions client et les requêtes HTTP en parallèle, ce qui peut améliorer les performances de votre application Django en permettant de gérer plus de requêtes simultanément. De plus, Nginx peut être configuré pour mettre en cache le contenu statique, réduisant ainsi la charge sur le serveur d'application Gunicorn.
- **Gestion du trafic** : Nginx peut agir comme un load balancer (un répartiteur de charge) pour distribuer le trafic sur plusieurs serveurs d'application Gunicorn. Cela peut être particulièrement utile lorsque vous devez mettre à l'échelle votre application pour gérer des volumes de trafic élevés.
- **Configuration flexible** : Nginx offre une grande flexibilité en matière de configuration, ce qui vous permet de personnaliser le comportement du serveur pour répondre aux besoins spécifiques de votre application.

En résumé, l'utilisation de Nginx en combinaison avec Gunicorn peut offrir une meilleure sécurité, des performances améliorées et une gestion du trafic plus efficace pour votre application Django.

## La configuration de Nginx

Sur le serveur, notre fichier de configuration de nginx se situe dans le répertoire `/etc/nginx/sites-available/`. Le fichier [wepynaire](wepynaire) donne un exemple de configuration opérationnelle.

Une fois ce fichier ajouté dans `/etc/nginx/sites-enabled/` à l'aide de la commande `ln -s /etc/nginx/sites-available/wepynaire /etc/nginx/sites-enabled/`, il est nécessaire de redémarrer nginx à l'aide de la commande `sudo systemctl reload nginx`.

## La configuration de gunicorn via supervisor

Sur notre serveur, nous configurons notre serveur WSGI, gunicorn, par l'intermédiaire de l'outil supervisor et d'un de ces fichier de configuration. 

### A quoi sert supervisor ?

Supervisor est un outil open-source pour superviser et contrôler les processus de système sous Linux. Dans le contexte du déploiement d'une application Django avec Gunicorn, Supervisor peut offrir plusieurs avantages :

- **Gestion de processus** : Supervisor peut gérer les processus Gunicorn de manière fiable et les redémarrer automatiquement en cas de panne ou d'erreur. Cela permet de garantir que votre application reste disponible et réactive, même en cas de problèmes de serveur.

- **Automatisation** : Supervisor peut être configuré pour démarrer automatiquement les processus Gunicorn lors du démarrage du serveur, ce qui peut réduire le temps de configuration et simplifier la gestion des processus.

- **Surveillance** : Supervisor peut surveiller les processus Gunicorn en cours d'exécution et fournir des informations sur leur état et leur activité. Cela permet de diagnostiquer rapidement les problèmes et d'optimiser les performances de l'application.

- **Facilité de configuration** : Supervisor est facile à configurer et à utiliser, avec une syntaxe simple et lisible pour la définition des processus.

En résumé, l'utilisation de Supervisor avec Django et Gunicorn peut offrir une gestion de processus fiable, une automatisation de la configuration, une surveillance des processus et une facilité de configuration, permettant ainsi de simplifier le déploiement et la gestion de l'application.

### Configuration de gunicorn

Notre serveur gunicorn et contrôlé et automatisé par supervisor. Le fichier de configuration [/etc/supervisor/conf.d/wepynaire-gunicorn.conf](wepynaire-gunicorn.conf).

Un fois que ce fichier de configuration est placé dans le bon répertoire, on peut exécuter les commandes suivantes:
- `$ sudo supervisorctl reread` pour demander à supervisor de le lire
- `$ sudo supervisorctl update` pour demander à supervisor de mettre à jour son exécution avec les nouvelles configurations
- `$ sudo supervisorctl status` pour vérifier si notre processus gunicorn est bien en cours d'exécution.