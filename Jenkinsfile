def JobName = Jenkins.instance.getItem('test2')
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo "${env.JOB_BASE_NAME}"
                echo "${WORKSPACE}"
                
                sh '''
                    git remote -v
                    git branch
                    git status
                    git rev-parse --short HEAD
                '''
                
                
            }
        }
    }
}

