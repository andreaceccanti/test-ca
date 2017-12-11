#!/usr/bin/env groovy

pipeline {
  agent { label 'generic' }

  options {
	buildDiscarder(logRotator(numToKeepStr: '5'))
	timeout(time: 1, unit: 'HOURS')
  }

  triggers { cron('@daily') }

  environment {
    WORKDIR = "/srv/scratch/${env.BUILD_TAG}/artifacts"
  }

  stages {
    stage('build') {
      steps {
        container('generic-runner'){
          sh 'make clean'
          sh 'make'
        }
      }
    }
    stage('archive') {
      steps {
        container('generic-runner'){
          dir("${env.WORKDIR}") {
            sh "find ${env.WORKSPACE} -iname *.rpm -exec mv {} . \\;"
            sh "find ${env.WORKSPACE} -iname *.tar.gz -exec mv {} . \\;"
            archiveArtifacts '**'
          }
        }
      }
    }
    stage('result') {
      steps {
        script { currentBuild.result = 'SUCCESS' }
      }
    }
  }

  post {
    failure {
      slackSend color: 'danger', message: "${env.JOB_NAME} - #${env.BUILD_NUMBER} Failure (<${env.BUILD_URL}|Open>)"
    }
    changed {
      script{
        if('SUCCESS'.equals(currentBuild.result)) {
          slackSend color: 'good', message: "${env.JOB_NAME} - #${env.BUILD_NUMBER} Back to normal (<${env.BUILD_URL}|Open>)"
        }
      }
    }
  }
}
