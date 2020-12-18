# ResourceIdea API

API for the ResourceIdea app.

## Backend Dev setup

### Local setup

##### Install postgres on docker:
- Pull postgres docker image.
```
$ docker pull postgres:[tag]
```
- Create volume location that will be used to persist the changes made.
```
$ mkdir -p $HOME/docker/volumes/postgres
```
- Run the postgres container.
```
$ docker run --rm --name pg-docker -e POSTGRES_PASSWORD=<your_password> -d -p 54320:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data postgres
```

##### Database setup
- Create the database.
```
$ docker exec -it pg-docker psql -U postgres -c "create database resourceidea"
```
- Load the environment variables.
```$ export $(cat .env.local)```
- Run migrations
```
$ python manage.py makemigrations

$ python migrate
```
- Create admin user
```$ python manage.py createsuperuser```

##### Run server
```$ python manage.py runserver```