def workspace = "${WORKSPACE}"
def now = new Date()
def build_time = now.format("yyMMdd_HHmm", TimeZone.getTimeZone('PST'))
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
                    "pattern": "myrepo/${currentBuild.number}_${build_time}/${env.GIT_COMMIT}/**",
                    "target": "${WORKSPACE}/${env.JOB_BASE_NAME}/temp/",
                    "recursive": "true"
                }
            ]
    }"""