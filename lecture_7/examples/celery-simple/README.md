# celery-simple example

## run with docker-compose

### Build docker images:

```bash
docker-compose build
```

### Run

```bash
docker-compose up
```

### Run celery task

```bash
docker exec -it celerysimple_celery bash
python app.py
```

or

```bash
docker exec -it celerysimple_celery bash -c "python app.py"
```

_Note: Results will be printed in console with running docker-compose._
