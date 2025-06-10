pipeline {
    agent any

    environment {
        EC2_USER = 'ec2-user'
        EC2_HOST = '44.203.147.18'
        PRIVATE_KEY_PATH = 'C:/Users/IT-WORKSTATION/Downloads/aws-electricaa.pem'
        IMAGE_NAME = 'django-kaiadmin'
        IMAGE_TAG = "build-${env.BUILD_NUMBER}"
        GIT_REPO = 'https://github.com/Yemmmyc/django-kaiadmin.git'
        BRANCH_NAME = 'main'
        GIT_BASH = '"C:\\Program Files\\Git\\bin\\bash.exe" -c'
        DOCKERHUB_CREDENTIALS_ID = 'dockerhub-creds'
    }

    stages {
        stage('Clone Code') {
            steps {
                echo "✅ Cloning '${BRANCH_NAME}' from ${GIT_REPO}"
                git branch: "${BRANCH_NAME}", url: "${GIT_REPO}"
            }
        }

        stage('Docker Build, Push & Deploy') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: "${DOCKERHUB_CREDENTIALS_ID}",
                    usernameVariable: 'DOCKERHUB_USER',
                    passwordVariable: 'DOCKERHUB_PASS'
                )]) {
                    echo "🐳 Logging into DockerHub"
                    bat """
                        ${GIT_BASH} "echo ${DOCKERHUB_PASS} | docker login -u ${DOCKERHUB_USER} --password-stdin"
                    """

                    echo "🐳 Building Docker image: ${DOCKERHUB_USER}/${IMAGE_NAME}:${IMAGE_TAG}"
                    bat """
                        ${GIT_BASH} "docker build -t ${DOCKERHUB_USER}/${IMAGE_NAME}:${IMAGE_TAG} ."
                    """

                    echo "📤 Pushing Docker image to DockerHub"
                    bat """
                        ${GIT_BASH} "docker push ${DOCKERHUB_USER}/${IMAGE_NAME}:${IMAGE_TAG}"
                    """

                    echo "🚀 Deploying to EC2: ${EC2_HOST}"
                    script {
                        // Create a shell script with remote commands
                        def remoteScript = """
                            echo ${DOCKERHUB_PASS} | docker login -u ${DOCKERHUB_USER} --password-stdin
                            docker pull ${DOCKERHUB_USER}/${IMAGE_NAME}:${IMAGE_TAG}
                            docker stop ${IMAGE_NAME} || :
                            docker rm ${IMAGE_NAME} || :
                            docker run -d --name ${IMAGE_NAME} -p 80:80 ${DOCKERHUB_USER}/${IMAGE_NAME}:${IMAGE_TAG}
                        """.stripIndent()

                        writeFile file: 'remote-deploy.sh', text: remoteScript

                        // Upload the script to EC2
                        bat """
                            ${GIT_BASH} "scp -o StrictHostKeyChecking=no -i ${PRIVATE_KEY_PATH} remote-deploy.sh ${EC2_USER}@${EC2_HOST}:/home/${EC2_USER}/remote-deploy.sh"
                        """

                        // Execute the uploaded script
                        bat """
                            ${GIT_BASH} "ssh -o StrictHostKeyChecking=no -i ${PRIVATE_KEY_PATH} ${EC2_USER}@${EC2_HOST} 'bash /home/${EC2_USER}/remote-deploy.sh'"
                        """
                    }
                }
            }
        }
    }

    post {
        failure {
            echo "❌ Deployment failed. Check the logs above."
        }
        success {
            echo "✅ Deployment completed successfully."
        }
    }
}


