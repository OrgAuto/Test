    // def rtServer = Artifactory.server("ArtifactoryLocal")
    // def rtServer = Artifactory.server('http://localhost:8082/artifactory/', 'admin', 'Prince@123')
    rtServer (
        id: 'Artifactory-1',
        url: 'http://localhost:8082/artifactory',
        // If you're using username and password:
        username: 'admin',
        password: 'Prince@123'
        // // If you're using Credentials ID:
        // credentialsId: 'ccrreeddeennttiiaall'
        // If Jenkins is configured to use an http proxy, you can bypass the proxy when using this Artifactory server:
        // bypassProxy: true
        // Configure the connection timeout (in seconds).
        // The default value (if not configured) is 300 seconds:
        timeout = 300
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