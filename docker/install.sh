#!/bin/bash

# Install dependencies for the Docker Image.

# Make bashline configurations.
set -e
RESET='\033[0m'
COLOR='\033[1;32m'
COLOR_WARN='\033[1;33m'
COLOR_ERR='\033[1;31m'

function msg {
  echo -e "${COLOR}$(date): $1${RESET}"
}

function msg_warn {
  echo -e "${COLOR_WARN}$(date): $1${RESET}"
}

function msg_err {
  echo -e "${COLOR_ERR}$(date): $1${RESET}"
}

function fail {
  msg_err "Error : $?"
  exit 1
}

function mcd {
  mkdir -p "$1" || fail
  cd "$1" || fail
}

function nvm_has {
    type "$1" > /dev/null 2>&1
}

# Check existence of python3
EXTRA_PY=""
if ! nvm_has "python3"; then
	if ! nvm_has "python"; then
		msg_warn "Need to have python installed in the image. If not provided, will try to install python with apt."
        EXTRA_PY="python3-dev python3-pip"
	fi
fi

APT_OPTIONS="-o Acquire::Retries=5 -o Acquire::http::timeout=20 -o Acquire::https::timeout=20"

# Required packages
apt-get -y update || fail && apt-get $APT_OPTIONS -y install \
    apt-utils apt-transport-https git-core wget jq \
    gnupg2 lsb-release xz-utils ${EXTRA_PY} || fail

if ! nvm_has "lsb_release"; then
    msg_err "lsb_release does not exist. This should not happen. Please contact the author for technical supports."
    exit 1
fi

if nvm_has "python"; then
    PYTHON=python
else
    if nvm_has "python3"; then
        PYTHON=python3
    else
        msgerr "Fail to find Python3 in the base image, stop the build."
        exit 1
    fi
fi

# Check the OS version
NAME_OS=$(lsb_release -is)
if [ "x${NAME_OS}" = "xUbuntu" ] || [ "x${NAME_OS}" = "xDebian" ]; then
	msg "Pass the OS check. Current OS: ${NAME_OS}."
else
	msg_err "The base image is an unknown OS, this dockerfile does not support it: ${NAME_OS}."
fi

# Install browser according to the OS
if [ "x${NAME_OS}" = "xUbuntu" ]; then
  # Need to use the downloaded version because Ubuntu only provides snap version.
  wget -O google-chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb || fail
  apt-get install $APT_OPTIONS -y ./google-chrome.deb || fail
  rm -f google-chrome.deb || fail
else
  if [ "x${NAME_OS}" = "xDebian" ]; then
    apt-get $APT_OPTIONS -y install chromium || fail
  fi
fi

# Install Node.js and Yarn.
mcd /app || fail
wget -O- https://gist.githubusercontent.com/cainmagi/f028e8ac4b06c3deefaf8ec38d5a7d8f/raw/install-nodejs.sh | bash -s -- --all
${PYTHON} -m pip install --compile --no-cache-dir pip wheel setuptools --upgrade || fail
${PYTHON} -m pip install --compile --no-cache-dir -r ./requirements-docker.txt 

msg "Successfully install the python dependencies."
