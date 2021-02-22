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
                shortCommit = sh(returnStdout: true, script: "git log -n 1 --pretty=format:'%h'").trim()
                
            }
            
        }
        
    }
}
