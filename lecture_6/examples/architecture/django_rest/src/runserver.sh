#!/bin/bash
# run migrations and django server

PROJECT_SETTINGS=${1}
PROJECT_PATH=${2}
PROJECT_ADDRPORT=${3}

if [[ ! "" == "${PROJECT_PATH}" ]]; then
    cd ${PROJECT_PATH}
else
    PROJECT_PATH="."
fi

if [[ "" == "${PROJECT_ADDRPORT}" ]]; then
    PROJECT_ADDRPORT="0.0.0.0:8000"
fi

echo ""
echo "================================================================="
echo "Checking PIP requirements"
echo ""
pip install -r ./requirements.txt
echo "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"

echo ""
echo "================================================================="
echo "Checking Dajngo-REST project"
python manage.py check ${PROJECT_SETTINGS}
EXIT_CODE=${?}
if [ ${EXIT_CODE} -eq 0 ]; then
    echo "OK"
else
    echo ""
    echo "Dajngo-REST PROJECT CHECKING IS FAILED"
    echo ""
    exit ${EXIT_CODE}
fi
echo "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"

echo ""
echo "================================================================="
echo "Run migrations"
echo ""
python manage.py migrate ${PROJECT_SETTINGS}
EXIT_CODE=${?}
if [ ${EXIT_CODE} -ne 0 ]; then
    PAUSE=30
    echo "================================================================="
    echo "It seems that this is a first start and DB is not initialized yet"
    echo "Waiting for db initialization for ${PAUSE} sec and will try again"
    echo "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
    sleep ${PAUSE}
    echo "Run migrations"
    python manage.py migrate ${PROJECT_SETTINGS}
    EXIT_CODE=${?}
    if [ ${EXIT_CODE} -ne 0 ]; then
        echo ""
        echo "UNABLE TO DO MIGRATIONS"
        echo ""
        exit ${EXIT_CODE}
    else
        echo "OK"
    fi
else
    echo "OK"
fi

pushd ${PROJECT_PATH}

echo ""
echo "Create Superuser if it does not exist"
echo "from django.contrib.auth import get_user_model; User = get_user_model(); ec = 0 if User.objects.filter(username='admin') else User.objects.create_superuser('admin', 'admin@example.test.com', 'admin123'); exit(ec)" | python manage.py shell --settings=shop.settings.docker

popd

echo "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
echo ""
echo "================================================================="
echo "Start \"Dajngo-REST\" server"
echo ""

python manage.py runserver ${PROJECT_SETTINGS} ${PROJECT_ADDRPORT}
