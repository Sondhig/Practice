pipeline {
    agent any

    stages {
        stage('Git'){
            steps{
                  checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/Sondhig/Practice.git']]])
            }
        }
        stage('Script1') {
            steps {
               sh 'python3 "Perfect Square".py'
            }
        }
        stage('Script2') {
            steps {
              sh 'python3 "Prime Number".py'
            }
        }
        stage('Script3') {
            steps {
               sh 'python3 "Tic Tac Toe".py'
            }
        }
        
    }
}
