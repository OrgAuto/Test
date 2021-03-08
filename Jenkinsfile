environment {
    def workspace = "${WORKSPACE}"
}
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

    stages {
        stage('Build') {
            steps {
                echo "${env.JOB_BASE_NAME}"
                echo "${WORKSPACE}"
                echo "${currentBuild.number}"

            }
            
        }
        stage('Download') {
            echo "Download"
            // steps {
            //     sh """python3 /home/uprince/testApi.py"""
                
            // }
            
        }

        stage('Post') { 
             when {
              branch 'main'
            }
            
            steps {
                echo "${env.GIT_COMMIT}"
                echo "${workspace}"
            //     archiveArtifacts artifacts: 'scripts/*', onlyIfSuccessful: true
            //     // sh """python3 /home/uprince/UploadFileApi.py""" 
            //     // @buildInfo.env.collect()
            //     script {
            //         fileOperations([fileZipOperation(folderPath: 'scripts', outputFolderPath: workspace)])
            //         rtServer.upload spec: uploadSpec, buildInfo: buildInfo
            //     }
                           
            }
            
        }
        
    }

}