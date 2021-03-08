
pipeline {
    agent any

    environment {
        def workspace = "${WORKSPACE}"
        def curr_commit = "${env.GIT_COMMIT}"
    }

    stages {
        stage('Build') {
            steps {
                echo "${env.JOB_BASE_NAME}"
                echo "${WORKSPACE}"
                echo "${currentBuild.number}"
                echo "${currentBuild.changeSets}"

            }
            
        }
        stage('Download') {            
            steps {
                echo "Download"
                // sh """python3 /home/uprince/testApi.py"""
                
            }
            
        }

        stage('Post') { 
             when {
              branch 'main'
            }
            
            steps {
                archiveArtifacts artifacts: 'scripts/*', onlyIfSuccessful: true
                // sh """python3 /home/uprince/UploadFileApi.py""" 
                script {
                    def rtServer = Artifactory.server("ArtifactoryLocal")
                    def buildInfo = Artifactory.newBuildInfo()
                    def uploadSpec = """{
                                "files": [
                                    {
                                        "pattern": "*.zip",
                                        "target": "myrepo/${currentBuild.number}_${currentBuild.startTimeInMillis}/${env.GIT_COMMIT}",
                                         "props": "type=zip;status=ready"
                                    }
                                ]
                        }"""
                    fileOperations([fileZipOperation(folderPath: 'scripts', outputFolderPath: workspace)])
                    rtServer.upload spec: uploadSpec, buildInfo: buildInfo
                }
                           
            }
            
        }
        
    }

}