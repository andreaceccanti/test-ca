#!/usr/bin/env groovy

pipeline {

  agent { label 'java11' }
  
  options {
	buildDiscarder(logRotator(numToKeepStr: '5'))
	timeout(time: 1, unit: 'HOURS')
  }

  triggers { cron('@daily') }

  environment {
    WORKDIR = "/tmp/${env.BUILD_TAG}/artifacts"
  }

  stages {
    stage('clean') {
      steps {
        cleanWs()
        checkout scm
      }
    }
    stage('build') {
      steps {
        sh 'make clean'
        sh 'make'
      }
    }
    stage('archive') {
      steps {
        sh "mkdir -p ${env.WORKDIR}"
        dir('voms-test-ca') {
          sh "cp *.tar.gz ${env.WORKDIR}"
          sh "cp rpmbuild/RPMS/noarch/*.rpm ${env.WORKDIR}"
        }
        dir('igi-test-ca') {
          sh "cp *.tar.gz ${env.WORKDIR}"
          sh "cp rpmbuild/RPMS/noarch/*.rpm ${env.WORKDIR}"
        }
        dir('igi-test-ca-2') {
          sh "cp *.tar.gz ${env.WORKDIR}"
          sh "cp rpmbuild/RPMS/noarch/*.rpm ${env.WORKDIR}"
        }
        dir('igi-test-ca-256') {
          sh "cp *.tar.gz ${env.WORKDIR}"
          sh "cp rpmbuild/RPMS/noarch/*.rpm ${env.WORKDIR}"
        }
        dir('igi-test-ca-email') {
          sh "cp *.tar.gz ${env.WORKDIR}"
          sh "cp rpmbuild/RPMS/noarch/*.rpm ${env.WORKDIR}"
        }
        dir("${env.WORKDIR}") {
          sh "ls -l ."
          archiveArtifacts '**'
        }
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
