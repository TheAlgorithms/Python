#!/bin/sh

# Source: https://gist.github.com/willprice/e07efd73fb7f13f917ea

setup_git() {
  git config --global user.email "${gh_email}"
  git config --global user.name "${gh_user}"
}

commit_website_files() {
  git checkout $TRAVIS_PULL_REQUEST_BRANCH
  git add .
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
}

upload_files() {
  git remote add origin https://${gh_token}@github.com/$TRAVIS_REPO_SLUG > /dev/null 2>&1
  git push --set-upstream origin $TRAVIS_PULL_REQUEST_BRANCH 
}

setup_git
commit_website_files
upload_files