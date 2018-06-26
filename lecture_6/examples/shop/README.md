# Django example

## Build docker images
```bash
docker build -t pl6-shop .
```

## Run docker container shell
```bash
docker run --rm -v "$(pwd)/src:/src" -p 8000:8000 --name django-test -it pl6-shop bash
```

## Run docker container django server
```bash
docker run --rm -v "$(pwd)/src:/src" -p 8000:8000 --name django-test pl6-shop
```
