    def rtServer = Artifactory.server("ArtifactoryLocal")
    def buildInfo = Artifactory.newBuildInfo()

    // def rtServer = Artifactory.server('http://localhost:8082/artifactory/', 'admin', 'Prince@123')
    def uploadSpec = """{
                    "files": [
                                {
                                    "pattern": "scripts/*.zip",
                                     "target": "myrepo/${currentBuild.number}/",
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
                echo "${currentBuild.timestamp}"

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
                zip zipFile: 'scripts.zip', dir: './scripts/' glob: '', archive: true
                // sh """python3 /home/uprince/UploadFileApi.py""" 
                // @buildInfo.env.collect()
                script {
                    rtServer.upload spec: uploadSpec, buildInfo: buildInfo
                }
                           
            }
            
        }
        
    }

}