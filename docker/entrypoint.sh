#!/bin/bash --login

# Make bashline configurations.
set -e
RESET='\033[0m'
COLOR='\033[1;32m'
COLOR_ERR='\033[1;31m'

function msg {
    echo -e "${COLOR}$(date): $1${RESET}"
}

function msgerr {
    echo -e "${COLOR_ERR}$(date): $1${RESET}"
}

function fail {
    msgerr "Error : $?"
    exit 1
}

function mcd {
    mkdir -p "$1" || fail
    cd "$1" || fail
}

function nvm_has {
    type "$1" > /dev/null 2>&1
}

msg "Developer's environment for Dash JSON Grid Viewer."

BASH=false
RUN_REACT=false
RUN_PYTHON=false
RUN_DEMO=false
WITH_DASH=false
DEMO_NAME="default"

# Pass options from command line
for ARGUMENT in "$@"
do
    KEY=$(echo $ARGUMENT | cut -f1 -d=)
    if [[ $KEY != '--*' ]]
    then
        VALUE=$(echo $ARGUMENT | cut -f2 -d=)   
    fi
    case "$KEY" in
        --bash)         BASH=true ;;
        --python)       RUN_PYTHON=true ;;
        --react)        RUN_REACT=true ;;
        --demo)         RUN_DEMO=true ;;
        --with-dash)    WITH_DASH=true ;;
        demo)           DEMO_NAME="${VALUE}" ;;
        *)
    esac
done

# Enter the virtual environment if necessary.
if [ -s "/opt/pyvenv/bin/activate" ]; then
  source /opt/pyvenv/bin/activate  || fail
  msg "Using the venv $(which python)"
fi

if $BASH
then
    # Run bash
    exec bash --login
    exit 0
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

if $RUN_REACT
then
    # Run React.
    msg "Run React demo app."
    yarn install || fail
    yarn run start || fail
    exit 0
fi

# Compile the module if it has not been compiled yet.
# This step ensures dash-json-grid to be available when entering the following modes.
if [ ! -s "dash_json_grid/DashJsonGrid.py" ]; then
    msg "Compile the dash component from the React codes."
    yarn install || fail
    yarn run build || fail
fi

if $RUN_PYTHON
then
    # Run Python.
    msg "Run Python."
    exec ${PYTHON}
    exit 0
fi

if $RUN_DEMO
then
    # Run python demo.
    if [ "x${DEMO_NAME}" = "xdefault" ] || [ "x${DEMO_NAME}" = "x" ]; then
        msg "Run Python Plotly-Dash demo app."
        ${PYTHON} usage.py || fail
        exit 0
    fi
    msg "Run Python Plotly-Dash example app: ${DEMO_NAME}."
    ${PYTHON} "examples/${DEMO_NAME}.py" || fail
    exit 0
fi

# Run pytests.
msg "Run unit tests."
if $WITH_DASH
then
    ${PYTHON} -m pytest --headless --with-dash || fail
else
    ${PYTHON} -m pytest  || fail
fi
