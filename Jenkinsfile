
pipeline {
    agent any

    // environment {
    //     // def workspace = "${WORKSPACE}"
    //     // def curr_commit = "${env.GIT_COMMIT}"
    // }

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

        stage('Publish and Download') { 
             when {
              branch 'main'
            }
            
            steps {
                
                // sh """python3 /home/uprince/UploadFileApi.py""" 
                script {
                    def props = readProperties file: 'env.groovy'
                    def rtServer = props.rtServer
                    archiveArtifacts artifacts: 'scripts/*', onlyIfSuccessful: true               
                    fileOperations([fileZipOperation(folderPath: 'scripts', outputFolderPath: props.workspace)])
                    rtServer.upload spec: props.uploadSpec, buildInfo: props.buildInfo
                    rtServer.download spec: props.downloadSpec
                }
                           
            }
            
        }
        
    }

}