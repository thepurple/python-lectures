# Django example

## Run with sqllite3 in a single docker

### Build docker images
```bash
docker build -t pl6-shop .
```

### Run docker container shell
```bash
docker run --rm -v "$(pwd)/src:/src" -p 8000:8000 --name django-test -it pl6-shop bash
```

### Run docker container django server
```bash
docker run --rm -v "$(pwd)/src:/src" -p 8000:8000 --name django-test pl6-shop
```

# Run with PostgreSQL in two dockers

Update `./src/shop/settings.py`

From:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'test',
#         'USER': 'postgres',
#         'PASSWORD': 'postgres',
#         'HOST': 'test_postgresql',
#         'PORT': '5432',
#     }
# }
```

To:
```
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'test_postgresql',
        'PORT': '5432',
    }
}

```

Build and run dockers:
```bash
docker-compose up
```

Run migrations (just once on the first start)
```
$ docker exec -it test_backend bash
user@c624c2a0a4fa:/backend$ python manage.py migrate
```
