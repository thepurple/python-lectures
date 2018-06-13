# Django example

## Build docker images
```bash
docker build -t django-l4 .
```

## Run docker container shell
```bash
docker run --rm -v "$(pwd)/src:/src" -p 8000:8000 --name django-test -it django-l4 bash
```

## Run docker container django server
```bash
docker run --rm -v "$(pwd)/src:/src" -p 8000:8000 --name django-test django-l4
```
