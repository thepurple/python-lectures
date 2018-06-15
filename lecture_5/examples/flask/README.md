# Django-REST example

## Build & run
build docker image
```bash
docker build -t flask-test .
```

run docker image in background

```bash
docker run -d -p 5000:5000 flask-test
```

run docker image with attached volume (for development)

```bash
docker run --rm -p 5000:5000 -v $(pwd)/src:/backend flask-test
```

run docker image with attached volume (for development) and bash
```bash
docker run --rm -p 5000:5000 -v $(pwd)/src:/backend -it flask-test bash
python app.py
```

## How to check how it works

http://127.0.0.1:5000/ 

You'll get 404

http://127.0.0.1:5000/user

## Test API with curl:

```
curl -H "Content-Type: application/json" -X POST -d '{"username":"abc","email":"test@test.com"}' http://localhost:5000/user
curl -H "Content-Type: application/json" http://localhost:5000/user/1
curl -H "Content-Type: application/json" -X PUT -d '{"username":"test","email":"test@test.com"}' http://localhost:5000/user/1
curl -H "Content-Type: application/json" -X POST -d '{"username":"test2","email":"test2@test.com"}' http://localhost:5000/user
curl -H "Content-Type: application/json" http://localhost:5000/user
curl -H "Content-Type: application/json" http://localhost:5000/user/1
curl -H "Content-Type: application/json" -X DELETE http://localhost:5000/user/1
curl -H "Content-Type: application/json" http://localhost:5000/user
curl -H "Content-Type: application/json" -X DELETE http://localhost:5000/user/2
curl -H "Content-Type: application/json" http://localhost:5000/user
```
