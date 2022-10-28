pipeline {
    agent any
    stages {
        stage("Clean Up"){
            steps {
                deleteDir()
            }
        }
        stage("Clone Repo"){
            steps {
                sh "git clone https://github.com/Qwerty5932/test.git"
            }
        }
        stage("Test"){
            steps {
                dir("build"){
                    sh "python CreateUser_intranet.py"
                }
            }
        }
    }
}
