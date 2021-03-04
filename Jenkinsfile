pipeline {
    agent any
    environment {
        workspace = "${WORKSPACE}"
        def rtServer = Artifactory.server("ArtifactoryLocal")
        def buildInfo = Artifactory.newBuildInfo()
        def uploadSpec = """{
                    "files": [
                                {
                                    "pattern": "/var/lib/jenkins/workspace/OrgAuto_Test_main/scripts.zip",
                                     "target": "myrepo/${currentBuild.number}/",
                                     "props": "type=zip;status=ready"
                                }
                            ]
                    }"""    
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