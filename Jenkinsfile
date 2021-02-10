def JobName = Jenkins.instance.getItem('test2')
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo "${env.JOB_BASE_NAME}"
                
            }
        }
    }
}

