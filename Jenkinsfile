pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t my-app .'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
            }
        }
    }
}