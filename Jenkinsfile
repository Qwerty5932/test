pipeline {
    agent any
    stages {
        stage('version') {
            steps {
                sh 'python --version'
            }
        }
        stage('test') {
            steps {
                sh 'python CreateUser_intranet.py'
            }
        }
    }
}
