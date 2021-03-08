
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
                    load "env.groovy"
                    def rtServer = Artifactory.server("ArtifactoryLocal")
                    archiveArtifacts artifacts: 'scripts/*', onlyIfSuccessful: true               
                    fileOperations([fileZipOperation(folderPath: 'scripts', outputFolderPath: workspace)])
                    rtServer.upload spec: uploadSpec, buildInfo: buildInfo
                    rtServer.download spec: downloadSpec
                }
                           
            }
            
        }
        
    }

}