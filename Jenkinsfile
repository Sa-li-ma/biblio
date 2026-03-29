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