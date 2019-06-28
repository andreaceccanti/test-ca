#!/usr/bin/env groovy

@Library('sd')_
def kubeLabel = getKubeLabel()

pipeline {

  agent {
    kubernetes {
      label "${kubeLabel}"
      cloud 'Kube mwdevel'
      defaultContainer 'runner'
      inheritFrom 'ci-template'
    }
  }

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
        sh 'make clean'
        sh 'make'
      }
    }
    stage('archive') {
      steps {
        sh "mkdir -p ${env.WORKDIR} ."
        sh "cd  ${env.WORKDIR}"
        sh "find ${env.WORKSPACE} -iname *.rpm -exec mv {} . \\;"
        sh "find ${env.WORKSPACE} -iname *.tar.gz -exec mv {} . \\;"
        archiveArtifacts '**'
      }
    }
  }

  post {
    failure {
      slackSend color: 'danger', message: "${env.JOB_NAME} - #${env.BUILD_NUMBER} Failure (<${env.BUILD_URL}|Open>)"
    }
    changed {
      script{
        if('SUCCESS'.equals(currentBuild.currentResult)) {
          slackSend color: 'good', message: "${env.JOB_NAME} - #${env.BUILD_NUMBER} Back to normal (<${env.BUILD_URL}|Open>)"
        }
      }
    }
  }
}
