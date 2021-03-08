env.workspace = "${WORKSPACE}"
env.now = new Date()
env.build_time = now.format("yyMMdd_HHmm", TimeZone.getTimeZone('PST'))
env.buildInfo = Artifactory.newBuildInfo()
env.uploadSpec = """{
            "files": [
                {
                    "pattern": "*.zip",
                    "target": "myrepo/${currentBuild.number}_${build_time}/${env.GIT_COMMIT}/",
                    "props": "type=zip;status=ready"
                }
            ]
    }"""
env.downloadSpec = """{
            "files": [
                {
                    "pattern": "myrepo/${currentBuild.number}_${build_time}/${env.GIT_COMMIT}/**",
                    "target": "${WORKSPACE}/${env.JOB_BASE_NAME}/temp/",
                    "recursive": "true"
                }
            ]
    }"""