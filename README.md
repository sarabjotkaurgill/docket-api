# Docket api

A pre-configured Django template

## Setting Up local Env

Create a new python3 virtual environment.

```
$ virtualenv venv
```

Activate the virtual env using

```
$ source venv/bin/activate
```

For deactivating the virtual env

```
$ deactivate
```

## Installing Packages

Before we start the project you need to install required packages to run this server.

```
pip install -r requirements.txt
```

Add .env file at the root of the project with the following contents.

```
APP_ENV=local
DATABASE_NAME=docket
```

## Running the Project

```
python manage.py runserver
```

## Creating Migrations

```
python manage.py makemigrations
```

## Migrate Models

```
python manage.py migrate
```
