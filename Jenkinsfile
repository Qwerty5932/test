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
                sh 'python3 CreateUser_intranet.py'
            }
        }
    }
}

// pipeline {
//     agent none 
//     stages {
//         stage('Example Build') {
//             agent { docker 'maven:3.8.1-adoptopenjdk-11' } 
//             steps {
//                 echo 'Hello, Maven'
//                 sh 'mvn --version'
//             }
//         }
//         stage('Example Test') {
//             agent { docker 'openjdk:8-jre' } 
//             steps {
//                 echo 'Hello, JDK'
//                 sh 'java -version'
//             }
//         }
//     }
// }
