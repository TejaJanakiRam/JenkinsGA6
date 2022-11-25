pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/TejaJanakiRam/JenkinsGA6.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x multi.py"
                sh "./multi.py"
            }
        }
        stage('Tests') {
            steps {
                sh "chmod u+x test.py"
                sh "./test.py"
            
            
            }
        }
    } 
}
