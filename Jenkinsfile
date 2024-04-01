pipeline {
    agent any

    stages {
        stage('setup_pytest') {
            steps {
                sh 'pip install pytest==8.1.1'
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