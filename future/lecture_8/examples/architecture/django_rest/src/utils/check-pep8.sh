#!/bin/bash

# checking python code for pep8 standards
CHECK_PATH=${1}
if [ -z "${CHECK_PATH}" ]; then
    CHECK_PATH="./"
fi


find ${CHECK_PATH} -name "*.py" -not -path "*migrations*" \
-not -path "*wsgi.py" \
-not -path "*/settings.py*" \
-exec pycodestyle {} \;
