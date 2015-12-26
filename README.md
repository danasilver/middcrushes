# MiddCrushes

## Development

Setup a virtualenv (assumes you have virtualenv and virtualenvwrapper installed):

```sh
$ mkvirtualenv --python /usr/local/bin/python3
```

```sh
pip install -r requirements/dev.txt
```

## Development Database

A PostgreSQL database. On OS X install [Postgres.app](http://postgresapp.com/).

Create a database for development:

```sh
$ createdb middcrushes
```

Run the migrations:

```sh
$ python manage.py migrate
```
