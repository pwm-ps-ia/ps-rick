# Backend 🖥️

## Execute project:

first you need to build the docker

```
docker-compose build
```

then execute the containers

```
docker-compose up
```

Open 0.0.0.0:8000 and here is going to be the django app

## Migrating db

First we are going to go inside containers shell

```
    docker exec -it container sh
```

then we are going to make the migrations

```
    python3 manage.py makemigrations
```

and last we are going to apply them

```
    python3 manage.py migrate
```
