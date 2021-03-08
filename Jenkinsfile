
pipeline {
    agent any

    environment {
        def now = new Date()
        
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
                
                // sh """python3 /home/uprince/UploadFileApi.py""" 
                script {
                    def workspace = "${WORKSPACE}"
                    def my_time = "${currentBuild.startTimeInMillis}"
                    echo(env.now.format("yyMMdd_HHmm", TimeZone.getTimeZone('UTC')))
                    def rtServer = Artifactory.server("ArtifactoryLocal")
                    def buildInfo = Artifactory.newBuildInfo()
                    def uploadSpec = """{
                                "files": [
                                    {
                                        "pattern": "*.zip",
                                        "target": "myrepo/${currentBuild.number}_${my_time}/${env.GIT_COMMIT}/",
                                         "props": "type=zip;status=ready"
                                    }
                                ]
                        }"""
                    def downloadSpec = """{
                                "files": [
                                    {
                                        "pattern": "*.zip",
                                        "target": "myrepo/${currentBuild.number}_${my_time}/${env.GIT_COMMIT}",
                                         "props": "type=zip;status=ready"
                                    }
                                ]
                        }"""
                    echo "${my_time}"
                    archiveArtifacts artifacts: 'scripts/*', onlyIfSuccessful: true               
                    fileOperations([fileZipOperation(folderPath: 'scripts', outputFolderPath: workspace)])
                    rtServer.upload spec: uploadSpec, buildInfo: buildInfo
                }
                           
            }
            
        }
        
    }

}