pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo "${env.JOB_BASE_NAME}"

            }
            
        }
        stage('Download') {
            steps {
                sh """python3 /home/uprince/testApi.py"""
                
            }
            
        }        
        stage('Post') {
            steps {
                sh """python3 /home/uprince/UploadFileApi.py"""
                sh """
                last_commit_id=`git rev-parse --short HEAD`
                git diff-tree --no-commit-id --name-only -r $last_commit_id
                """
                
            }
            
        }
        
    }
}
