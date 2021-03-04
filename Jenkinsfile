    def rtServer = Artifactory.server("ArtifactoryLocal")
    def buildInfo = Artifactory.newBuildInfo()

    // def rtServer = Artifactory.server('http://localhost:8082/artifactory/', 'admin', 'Prince@123')
    def uploadSpec = """{
                    "files": [
                                {
                                    "pattern": workspace/"*.zip",
                                     "target": "myrepo/${currentBuild.number}/",
                                     "props": "type=zip;status=ready"
                                }
                            ]
                    }"""

pipeline {
    agent any
    environment {
        workspace = "${WORKSPACE}"
    }

    stages {
        stage('Build') {
            steps {
                echo "${env.JOB_BASE_NAME}"
                echo "${WORKSPACE}"
                echo "${currentBuild.number}"

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
                // sh """python3 /home/uprince/UploadFileApi.py""" 
                // @buildInfo.env.collect()
                script {
                    fileOperations([fileZipOperation(folderPath: 'scripts', outputFolderPath: workspace)])
                    rtServer.upload spec: uploadSpec, buildInfo: buildInfo
                }
                           
            }
            
        }
        
    }

}