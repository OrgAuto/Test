def JobName = Jenkins.instance.getItem('test2')
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo "${env.JOB_BASE_NAME}"
                echo "${WORKSPACE}"
                
                sh '''
                    git remote -v
                    git branch
                    git status
                    commit_id=`git rev-parse --short HEAD`
                    git diff-tree --no-commit-id --name-only -r $commit_id
                '''
                
                
            }
        }
    }
}

