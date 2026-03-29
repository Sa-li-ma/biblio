pipeline {
    agent any

    stages {

        stage('Cloner le projet') {
            steps {
                git 'https://github.com/Sa-li-ma/biblio.git'
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
                sh 'docker exec biblio python manage.py migrate'
            }
        }

        stage('Tests (optionnel)') {
            steps {
                sh 'docker exec biblio python manage.py test || true'
            }
        }
    }

    post {
        success {
            echo ' Pipeline réussie !'
        }
        failure {
            echo ' Pipeline échouée'
        }
    }
}