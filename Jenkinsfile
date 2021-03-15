def issue = [fields: [ project: [key: 'LOC'],
                             summary: 'Release x.y.z Review',
                             description: 'Review changes for release x.y.z ',
                             issuetype: [name: 'Task']]]
def newIssue = jiraNewIssue issue: issue
issueKey = newIssue.data.key
def transitionInput = [transition: [id: 15]]
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
                    jiraTransitionIssue idOrKey: issueKey, input: transitionInput, site: 'Jira-Local-Site'
                }
                           
            }
            
        }

    }

}