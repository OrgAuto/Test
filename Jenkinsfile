
pipeline {
    agent any

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
                echo "Executing another scripted pipeline Job"
                script {
                    def bRun = build 'DeployPipeline' 
                    for(String line : bRun.getRawBuild().getLog(100)){
                        echo "${line}"
                    }

                }

            }
        }

        stage('Publish and Download') { 
             when {
              branch 'main'
            }
            
            steps {
                
                script {
                    load "env.groovy"
                    def rtServer = Artifactory.server("ArtifactoryLocal")
                    def buildInfo = Artifactory.newBuildInfo()
                    archiveArtifacts artifacts: 'scripts/*', onlyIfSuccessful: true               
                    fileOperations([fileZipOperation(folderPath: 'scripts', outputFolderPath: env.workspace)])
                    rtServer.upload spec: env.uploadSpec, buildInfo: env.buildInfo
                    rtServer.download spec: env.downloadSpec
//                     jiraAddComment comment: 'Auto comment from Jenkins', idOrKey: 'LOC-10', site: 'Jira-Local-Site'
                    jiraNewIssue issue: "New Issue from Jenkins" idOrKey: "LOC" site: 'Jira-Local-Site'
                }
                           
            }
            
        }

    }

}