
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/amulyakar/devops-uat-demo.git'
            }
        }

        stage('Verify Tools') {
            steps {
                bat 'python --version'
                bat 'docker --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Pytest') {
            steps {
                bat 'python -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t hello-uat:1.0 .'
            }
        }

        stage('Run Application') {
            steps {
                bat 'docker run --rm hello-uat:1.0'
            }
        }
    }

    post {
        success {
            echo 'UAT pipeline completed successfully!'
        }
        failure {
            echo 'UAT pipeline failed. Check Console Output.'
        }
    }
}
