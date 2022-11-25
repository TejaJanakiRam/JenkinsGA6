pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/TejaJanakiRam/JenkinsGA6.git'
            }
        }
        stage('Permissions'){
            steps{
                sh "chmod u+x multi.py"
                sh "chmod u+x test.py"
            }
        }
        stage('Build Code') {
            steps {
                sh "./multi.py"
            }
        }
        stage('Tests') {
            steps {               
                sh "./test.py"       
            }
        }
    } 
}
