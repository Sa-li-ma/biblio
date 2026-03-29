pipeline {
    agent any

    environment {
        COMPOSE_PROJECT_NAME = "biblio_project"
    }

    stages {

        stage('Cloner le projet') {
            steps {
                deleteDir() // Nettoyer workspace
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

        stage('Tests (optionnel)') {
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