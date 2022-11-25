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
                sh "chmod u+x test1.py"
                sh "./test1.py"
            
                sh "chmod u+x test2.py"
                sh "./test2.py"
            
                sh "chmod u+x test3.py"
                sh "./test3.py"
            
                sh "chmod u+x test4.py"
                sh "./test4.py"
            
                sh "chmod u+x test5.py"
                sh "./test5.py"
            }
        }
    } 
}
