pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\amuly\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
        DOCKER_IMAGE = 'hello-uat:1.0'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/amulyakar/devops-uat-demo.git'
            }
        }

        stage('Verify Tools') {
            steps {
                bat '"%PYTHON%" --version'
                bat 'docker --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"%PYTHON%" -m pip install -r requirements.txt'
            }
        }

        stage('Run Pytest') {
            steps {
                bat '"%PYTHON%" -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %DOCKER_IMAGE% .'
            }
        }

        stage('Run Application') {
            steps {
                bat 'docker run --rm %DOCKER_IMAGE%'
            }
        }

        stage('Run Evidently Monitoring') {
            steps {
                script {
                    if (fileExists('monitor.py')) {
                        bat '"%PYTHON%" monitor.py'
                    } else {
                        echo 'monitor.py not found; skipping Evidently monitoring.'
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'UAT pipeline completed successfully!'
        }

        failure {
            echo 'UAT pipeline failed. Check Console Output for errors.'
        }

        always {
            echo 'DevOps UAT pipeline execution finished.'
        }
    }
}
```