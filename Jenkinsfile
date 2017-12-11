#!/usr/bin/env groovy

pipeline {
    agent { label 'generic' }
    options {
        buildDiscarder(logRotator(numToKeepStr: '5'))
        timeout(time: 1, unit: 'HOURS')
    }
    triggers { cron('@daily') }
    stages {
        stage('clean') {
            steps {
                container('generic-runner'){
                    sh 'make clean'
                }
            }
        }
        stage('make') {
            steps {
                container('generic-runner'){
                    sh 'make'
                    dir('/tmp/artifacts') {
                        sh "find ${env.WORKSPACE} -iname *.rpm -exec mv {} . \\;"
                        sh "find ${env.WORKSPACE} -iname *.tar.gz -exec mv {} . \\;"
                        archiveArtifacts '**'
                    }
                }
            }
        }
        stage('result') {
            steps {
                script {
                    currentBuild.result = 'SUCCESS'
                }
            }
        }
    }

    post {
        failure {
            slackSend color: 'danger', message: "${env.JOB_NAME} - #${env.BUILD_NUMBER} Failure (<${env.BUILD_URL}|Open>)"
        }
        unstable {
            slackSend color: 'warning', message: "${env.JOB_NAME} - #${env.BUILD_NUMBER} Unstable (<${env.BUILD_URL}|Open>)"
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
