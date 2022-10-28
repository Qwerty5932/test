pipeline {
    agent any
    stages {
        stage('version') {
            steps {
                sh 'python3 --version'
            }
        }
    }
    stages {
        stage('test') {
            steps {
                sh 'python3 CreateUser_intranet.py'
            }
        }
    }
}
