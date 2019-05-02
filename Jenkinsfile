node {
  checkout scm
  def workspace = pwd()

  if (env.BRANCH_NAME == 'master') {
    stage('SonarQube analysis') {
// requires SonarQube Scanner 2.8+
def scannerHome = tool 'scan';
  withSonarQubeEnv('sonar-server') {
     sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=python -Dsonar.sources=. -Dsonar.qualitygate=python-goal -Dsonar.projectVersion=1.0.${BUILD_NUMBER}"
    }
  }
  
//perform quality gate step setting the time and retrieving the status from sonar webhook and then pass the QG status
stage("Quality Gate"){
 timeout(time: 5, unit: 'MINUTES') {
 def qg = waitForQualityGate()
 if (qg.status != 'OK') {
 error "Pipeline aborted due to quality gate failure: ${qg.status}"
   }
  }
 }
  }

  else if (env.BRANCH_NAME == 'dev') {
    stage ('Some stage branch step') {
      sh 'echo dev'
    }
    stage ('Deploy to stage target') {
      sh 'echo dev 2'
    }
  }

  else {
    sh 'echo "Branch not applicable to Jenkins... do nothing"'
  }
}
