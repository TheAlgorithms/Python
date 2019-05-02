node {
  checkout scm
  def workspace = pwd()

  if (env.BRANCH_NAME == 'master') {
    stage ('Some Stage 1 for master') {
      sh 'echo master'
    }
    stage ('Another Stage for Master') {
      sh 'echo master step 2'
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