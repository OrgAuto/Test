
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

        stage('Post') { 
             when {
              branch 'main'
            }
            
            steps {
                
                // sh """python3 /home/uprince/UploadFileApi.py""" 
                script {
                    def workspace = "${WORKSPACE}"
                    def now = new Date()
                    def build_time = now.format("yyMMdd_HHmm", TimeZone.getTimeZone('PST'))
                    def rtServer = Artifactory.server("ArtifactoryLocal")
                    def buildInfo = Artifactory.newBuildInfo()
                    def uploadSpec = """{
                                "files": [
                                    {
                                        "pattern": "*.zip",
                                        "target": "myrepo/${currentBuild.number}_${build_time}/${env.GIT_COMMIT}/",
                                         "props": "type=zip;status=ready"
                                    }
                                ]
                        }"""
                    def downloadSpec = """{
                                "files": [
                                    {
                                        "pattern": "myrepo/${currentBuild.number}_${build_time}/${env.GIT_COMMIT}/*.zip",
                                        "target": "${workspace}/${env.JOB_BASE_NAME}/",
                                         "props": "p1=v1;p2=v2"
                                    }
                                ]
                        }"""
                    archiveArtifacts artifacts: 'scripts/*', onlyIfSuccessful: true               
                    fileOperations([fileZipOperation(folderPath: 'scripts', outputFolderPath: workspace)])
                    rtServer.upload spec: uploadSpec, buildInfo: buildInfo
                    rtServer.download spec: downloadSpec
                }
                           
            }
            
        }
        
    }

}