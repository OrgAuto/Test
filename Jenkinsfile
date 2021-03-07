def rtServer = Artifactory.server("ArtifactoryLocal")
def buildInfo = Artifactory.newBuildInfo()
def uploadSpec = """{
        "files": [
            {
                "pattern": "*.zip",
                 "target": "myrepo/${currentBuild.number}_${currentBuild.startTimeInMillis}/",
                 "props": "type=zip;status=ready"
            }
                ]
        }"""

pipeline {
    agent any
    environment {
        def workspace = "${WORKSPACE}"
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
        stage('master-branch-stuff') {
            when {
              branch 'main'
            }
        steps {
        echo 'run this stage - ony if the branch = master branch'
            }
        }
        
    }

}