#!/bin/bash

# lint test for python code
CHECK_PATH=${1}
if [ -z "${CHECK_PATH}" ]; then
    CHECK_PATH="./"
fi

find ${CHECK_PATH} -name "*.py" -not -path "*migrations*" \
-not -path "*manage.py*" \
-not -path "*wsgi.py" \
-not -path "*/settings.py" \
-exec pylint {} \;  2>&1 \
| grep -v "Using config file `pwd`/.pylintrc"
