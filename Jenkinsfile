pipeline {
    agent any

    stages {
        stage('Version') {
            steps {
                sh 'Python3 --version'
            }
        }
        stage('setup') {
            steps {
                sh 'Python3 setup.py'
            }
        }
        stage('run') {
            steps {
                sh 'pytest -m tcid99'
            }
        }
    }
}