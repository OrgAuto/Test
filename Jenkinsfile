    def rtServer = Artifactory.server("ArtifactoryLocal")
    def buildInfo = Artifactory.newBuildInfo()

    // def rtServer = Artifactory.server('http://localhost:8082/artifactory/', 'admin', 'Prince@123')
    def uploadSpec = """{
                    "files": [
                                {
                                    "pattern": "${WORKSPACE}/*",
                                     "target": "myrepo/",
                                     "props": "type=zip;status=ready"
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
                // @buildInfo.env.collect()
                script {
                    rtServer.upload spec: uploadSpec, buildInfo: buildInfo
                }
                           
            }
            
        }
        
    }

}