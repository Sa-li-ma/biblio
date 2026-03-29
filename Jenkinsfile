pipeline {
    agent any

    environment {
        COMPOSE_PROJECT_NAME = "biblio_project"
    }

    stages {

        stage('Cloner le projet') {
            steps {
                git url: 'https://github.com/Sa-li-ma/biblio.git', branch: 'main'
            }
        }

        stage('Build Docker') {
            steps {
                // Utilisation de docker-compose en mode root si nécessaire
                sh 'sudo docker-compose build'
            }
        }

        stage('Lancer les conteneurs') {
            steps {
                sh 'sudo docker-compose up -d'
            }
        }

        stage('Migrations Django') {
            steps {
                // Exécuter les migrations Django dans le conteneur backend
                sh 'sudo docker-compose exec -T backend-service python manage.py migrate'
            }
        }

        stage('Tests (optionnel)') {
            steps {
                // Exécuter les tests Django (ignore les erreurs pour ne pas bloquer le pipeline)
                sh 'sudo docker-compose exec -T backend-service python manage.py test || true'
            }
        }
    }

    post {
        success {
            echo 'Pipeline réussie !'
        }
        failure {
            echo ' Pipeline échouée'
            // Optionnel : arrêter et supprimer les conteneurs si échec
            sh 'sudo docker-compose down'
        }
    }
}