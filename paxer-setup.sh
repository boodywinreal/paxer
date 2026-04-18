#!/bin/sh
paxer () {
    if ! command -v python3 > /dev/null; then
        builtin echo "Python3 couldn't be found"
        return 1
    elif [ ! -f "./paxer-path-parser.py" ]; then
        builtin echo "The python script was not found, please download it and put it with the shell script"
        return 1
    fi
    _NEW_PATH="$(python3 './paxer-path-parser.py')"
    if [ -n "$_NEW_PATH" ]; then
        builtin export PATH="$_NEW_PATH"
        return 0
    fi

    builtin echo "Error while resolving the path"
    return 1
}

paxer