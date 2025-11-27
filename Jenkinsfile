pipeline {
    agent any

    environment {
        IMAGE_NAME     = "fastapi-demo"
        CONTAINER_NAME = "fastapi-demo"
        HOST_PORT      = "8090"
        CONTAINER_PORT = "8000"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                sh '''
                  pip3 install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                  echo "=== Running pytest ==="
                  pytest -q
                '''
            }
        }

        stage('Build Docker image') {
            steps {
                sh '''
                  echo "=== Building Docker image ==="
                  docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} .
                  docker tag ${IMAGE_NAME}:${BUILD_NUMBER} ${IMAGE_NAME}:latest
                '''
            }
        }

        stage('Deploy container') {
            steps {
                sh '''
                  echo "=== Stopping old container ==="
                  docker rm -f ${CONTAINER_NAME} 2>/dev/null || true

                  echo "=== Starting new container ==="
                  docker run -d --name ${CONTAINER_NAME} -p ${HOST_PORT}:${CONTAINER_PORT} ${IMAGE_NAME}:latest
                '''
            }
        }
    }
}
