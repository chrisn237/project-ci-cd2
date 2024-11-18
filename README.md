# flask-postgres-CRUD

## A basic CRUD application built in flask using postgres as database

# Taks list
- [x] Dockerfile
- [x] Initial docker-compose - It is working
- [x] Database class/access
- [x] Config files
- [x] Flask initial configs
- [x] CRUD routes
- [x] Basic frontend files to view application
- [ ] PyTest - In development
- [ ] CRUD revision - better management
- [ ] Advanced frontend
  - [ ] Bootstrap - CSS framework
  - [ ] JS - framework is being chosen
- [ ] Dockerfile/dockercompose adjusts - It will be necessary because futures features
- [x] Free hosting on [herokuapp.com/](https://herokuapp.com/) - ~~Whatever I hosting before done~~ - Well, I did! [current version link](https://flask-postgres-crud.herokuapp.com/messages/)

# How to test now
## Make the following steps to debug this application inside a [docker container](https://docs.docker.com/get-started/)
  ``` 

  [example@example]$ git clone https://github.com/PabloEmidio/flask-postgres-CRUD.git

  [example@example]$ cd flask-postgres-CRUD

  [example@example flask-postgres-CRUD]$ docker-compose build

  [example@example flask-postgres-CRUD]$ docker-compose up -d

  [example@example flask-postgres-CRUD]$ URL="http://127.0.0.1:8088/"; xdg-open $URL || sensible-browser $URL || x-www-browser $URL || gnome-open $URL

  ```

# Configuration

  Configurer la base de données : project/db/resources/database.ini
  Configuer le fichier VERSION : par exemple "1.0.0"
  Configurer le fichier Changelog

# Pipeline-cicd

  Le pipeline comprend les étapes suivantes :

  Build et tests :

  Vérifie que les fichiers VERSION et Changelog.md ont été modifiés lors des commits sur la branche main.
  Lit la version depuis le fichier VERSION.
  Construit et pousse l'image Docker vers Docker Hub.
  Déploiement en staging :

  Déploie automatiquement la nouvelle version sur le serveur de staging lorsque des changements sont poussés sur main.
  Déploiement en production :

  Se déclenche lors de la création d'une nouvelle release sur GitHub.
  Déploie la version spécifiée sur le serveur de production.
  Variables et Secrets
  Assurez-vous de configurer les secrets suivants dans votre dépôt GitHub :

  DOCKER_USERNAME
  DOCKER_PASSWORD
  STAGING_VM_IP
  STAGING_VM_USER
  STAGING_VM_PASSWORD
  PROD_VM_IP
  PROD_VM_USER
  PROD_VM_PASSWORD

# Tests

  Test fonctionnels: python -m unittest tests/functional_test.py

  Test de performance: k6 run tests/performances.js

# Déploiement

 
  Environnement de staging:
  Le déploiement en staging est automatique lors des push sur la branche main.

  Environnement de production
  Pour déployer en production :
  Créez une nouvelle release sur GitHub.
  Le pipeline CI/CD se chargera du déploiement sur le serveur de production.




