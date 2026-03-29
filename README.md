
# Bibliothèque DIT

Cette application gère la bibliothèque de DIT. Les utilisateurs sont enregistrés et peuvent emprunter des livres, le quota d'emprunt en cours dépend de leur statut.

## Il y a plusieurs manières de télécharger et d'excuter ce projet:


### I- Avec jenkins:

#### 1- Télécharger Jenkins personnalisé 

Chercher l'image personnalisée de Jenkins (elle contient docker, docker-compose et tout ce qui est essentiel au bon fonctionnement de la pipeline Jenkins)

```bash
  docker pull salimaaa06/jenkins-docker

```
#### 2- Créer un conteneur avec Jenkins personnalisé 


```bash
docker run -d -p 8085:8080 -v jenkins_home:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock salimaaa06/jenkins-docker

```

#### 3- Aller à Aller à http://localhost:8085
pour avoir la clé taper ceci:
```bash
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```
créer un compte 

#### 4- Créer une pipeline:
New Item → Pipeline \
Pipeline script from SCM \
Repository : https://github.com/Sa-li-ma/biblio.git \
Script : coller ceci
```bash
pipeline {
    agent any

    environment {
        COMPOSE_PROJECT_NAME = "biblio_project"
    }

    stages {

        stage('Cloner le projet') {
            steps {
                deleteDir() 
                git url: 'https://github.com/Sa-li-ma/biblio.git', branch: 'main'
            }
        }

        stage('Build Docker') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Lancer les conteneurs') {
            steps {
                sh 'docker-compose up -d'
            }
        }

        stage('Migrations Django') {
            steps {
                sh 'docker-compose exec -T backend-service python manage.py migrate'
            }
        }

        stage('Tests ') {
            steps {
                sh 'docker-compose exec -T backend-service python manage.py test || true'
            }
        }
    }

    post {
        success {
            echo 'Pipeline réussie !'
        }
        failure {
            echo 'Pipeline échouée'
            sh 'docker-compose down'
        }
    }
}

```
#### 5- Lancer le build et aller à http://localhost:8000/

### II- Télécharger et construire avec docker-compose

#### 1- Clonner le projet sur github et se déplacer dans biblio/
```bash
git clone https://github.com/Sa-li-ma/biblio.git
cd biblio
```
#### 2- Construire une image personnalisée Jenkins
```bash
docker build -t jenkins-docker -f Dockerfile.jenkins .

```
#### 3- Créer un conteneur avec image personnalisée Jenkins
```bash
docker run -d -p 8085:8080 -v jenkins_home:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock jenkins-docker

```
#### 4- Lancer les conteneurs
```bash
docker-compose up --build

```
### Accès :
Backend Django : http://localhost:8000
PgAdmin : http://localhost:8082


### Fonctionnement du pipeline:
#### 1- stage 1 : Clonage du projet sur la branche main
#### 2- stage 2 : Construction de l'architecture avec docker-compose
#### 3- stage 3 : Lancement de tous les conteneurs, tous les service du docker-compose
#### 4- stage 4 : Application des migrations pour créer les tables dans la db
#### 5- stage 5 : Application des tests, vérification des bonnes pretiques



