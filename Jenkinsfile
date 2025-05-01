pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/felipeaprata/projetoJenkins02.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('flask-app:latest')
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    docker.image('flask-app:latest').inside {
                        sh 'python -m unittest discover tests'
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    sh 'docker stop flask-app || true'
                    sh 'docker rm flask-app || true'
                    docker.image('flask-app:latest').run('-d -p 5000:5000 --name flask-app')
                }
            }
        }
    }
}