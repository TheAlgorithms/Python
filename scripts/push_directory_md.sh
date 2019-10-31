#!/bin/sh

# Source: https://gist.github.com/willprice/e07efd73fb7f13f917ea

setup_git() {
  git config --global user.email "${gh_email}"
  git config --global user.name "${gh_user}"
}

commit_directory_file() {
  git add .
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
}

fetch_get() {
  git fetch origin pull/$TRAVIS_PULL_REQUEST/head:$TRAVIS_PULL_REQUEST_BRANCH
  git checkout $TRAVIS_PULL_REQUEST_BRANCH
}

upload_files() {
  git remote add origin https://${gh_token}@github.com/$TRAVIS_REPO_SLUG > /dev/null 2>&1
  git push origin $TRAVIS_PULL_REQUEST_BRANCH 
}

commit_directory_file
setup_git
fetch_get
upload_files