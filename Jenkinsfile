    // def rtServer = Artifactory.server("ArtifactoryLocal")
    // def rtServer = Artifactory.server('http://localhost:8082/artifactory/', 'admin', 'Prince@123')
    rtServer (
        id: 'ArtifactoryLocal',
        url: 'http://localhost:8082/artifactory',
        // If you're using username and password:
        username: 'admin',
        password: 'Prince@123'
        )
    def uploadSpec = """{
                    "files": [
                                {
                                    "pattern": "scripts/*",
                                     "target": "myrepo/"
                                }
                            ]
                    }"""
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
                archiveArtifacts artifacts: 'scripts/*', onlyIfSuccessful: true
                sh """python3 /home/uprince/UploadFileApi.py""" 
                script {
                    rtServer.upload(uploadSpec)
                }
                           
            }
            
        }
        
    }

}