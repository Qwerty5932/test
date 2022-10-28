pipeline {
    agent { docker { image 'python:3.10.7-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
    stages {
        stage('test') {
            steps {
                sh 'python CreateUser_intranet.py'
            }
        }
    }
}
