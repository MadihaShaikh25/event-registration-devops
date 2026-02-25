pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/YOUR_USERNAME/event-registration-devops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t event-registration-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker stop event-registration-container || exit 0'
                bat 'docker rm event-registration-container || exit 0'
                bat 'docker run -d -p 5000:5000 --name event-registration-container event-registration-app'
            }
        }
    }
}
