#!/bin/sh
SCRIPT_DIR="$(cd "$(dirname "$1")" && pwd)"
paxer () {
    _PARSER="$SCRIPT_DIR/paxer-path-parser.py"
    _NEW_PATH="$(command python3 "$_PARSER")"
    if [ -n "$_NEW_PATH" ]; then
        export PATH="$_NEW_PATH"
        return 0
    fi
    builtin echo "Error while generating the path"
    return 1
}

paxer