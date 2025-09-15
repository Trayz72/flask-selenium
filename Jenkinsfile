pipeline {
    agent any

    stages {

        stage('Setup Python Env') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install --upgrade pip'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }
        stage('Run Flask in Background') {
            steps {
                sh 'nohup ./venv/bin/python app.py &'
                sh 'sleep 5'  
            }
        }
        stage('Run Selenium Tests') {
            steps {
                sh './venv/bin/python tests/test_login.py --headless'
            }
        }
    }

}
