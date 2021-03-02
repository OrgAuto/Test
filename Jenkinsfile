pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo "${env.JOB_BASE_NAME}"
                echo "${WORKSPACE}"

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
                
                
            }
            
        }
        
    }
    post {
        always {
            archiveArtifacts artifacts: 'xyz.py', onlyIfSuccessful: true
        }
    }
}