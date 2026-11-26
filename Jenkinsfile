pipeline {
    agent {
        label 'python'
    }

    stages {
        stage('Entorno') {
            steps {
                sh 'python3 --version'
                sh 'pip3 --version'
                sh 'pip install --break-system-packages pytest'
            }
        }

        stage('Descarga') {
            steps {
                git url: 'https://github.com/David12Salas/agente_python.git', branch: 'main'
            }
        }

        stage('Ejecutar') {
    steps {
        sh 'python3 -c "import Conversion; print(\"Modulo Conversion cargado correctamente\")"'
    }
}

        stage('Probar') {
            steps {
                sh 'mkdir -p reports'
                sh 'python3 -m pytest --junitxml=reports/results.xml'
            }
            post {
                always {
                    junit 'reports/results.xml'
                }
            }
        }
    }
}