pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        bat 'python -m pip install --upgrade pip setuptools six wheel'
        bat 'python -m pip install mypy pytest-cov -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        bat 'mypy .'
      }
    }
  }
}
