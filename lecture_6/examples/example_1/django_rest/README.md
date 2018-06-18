# Django-REST example

## Build & run
build docker image
```bash
docker build -t django-rest .
```

run docker image in background

```bash
docker run -d -p 8000:8000 django-rest
```

run docker image with attached volume (for development)

```bash
docker run --rm -p 8000:8000 -v $(pwd)/src:/backend django-rest
```

run docker image with attached volume (for development) and bash
```bash
docker run --rm -p 8000:8000 -v $(pwd)/src:/backend -it django-rest bash
python manage.py runserver 0:8000
```

### Run tests
```bash
docker run --rm -p 8000:8000 -v $(pwd)/src:/backend -it django-rest bash
python manage.py test -t .
```

## Open in browser

### Admin panel:
http://127.0.0.1:8000/admin/

_Note: Do not forget to create a superuser for django-admin._

```bash
python manage.py createsuperuser
```

### API endpoints:

http://127.0.0.1:8000/api/v1/

### Documented API endpoints:

http://127.0.0.1:8000/api/v1/docs/


## Lint and PEP8 code check

```bash
docker run --rm -p 8000:8000 -v $(pwd)/src:/backend -it django-rest bash
python manage.py checkcode
```
