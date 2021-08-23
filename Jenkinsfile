pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'python -m pip install --upgrade pip setuptools six wheel'
        sh 'python -m pip install mypy pytest-cov -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'mypy .'
      }
    }
  }
}
