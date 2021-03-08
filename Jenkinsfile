environment {
    def workspace = "${WORKSPACE}"
    def curr_commit = "${env.GIT_COMMIT}"
}
def rtServer = Artifactory.server("ArtifactoryLocal")
def buildInfo = Artifactory.newBuildInfo()
def uploadSpec = """{
        "files": [
            {
                "pattern": "*.zip",
                 "target": "myrepo/${currentBuild.number}_${currentBuild.startTimeInMillis}/,
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
                echo "${curr_commit}"
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
                // script {
                //     fileOperations([fileZipOperation(folderPath: 'scripts', outputFolderPath: workspace)])
                //     rtServer.upload spec: uploadSpec, buildInfo: buildInfo
                // }
                           
            }
            
        }
        
    }

}