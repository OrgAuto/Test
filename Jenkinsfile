    def rtServer = Artifactory.server("ArtifactoryLocal")
    // def server = Artifactory.newServer('artifactory-url', 'username', 'password')
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
                script {
                    rtServer.upload(uploadSpec)
                }
                sh """python3 /home/uprince/UploadFileApi.py"""            
            }
            
        }
        
    }
    post {
        always {
            archiveArtifacts artifacts: 'scripts/*', onlyIfSuccessful: true
            
        }
    }

}