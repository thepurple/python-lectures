# Django-REST example

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
```
