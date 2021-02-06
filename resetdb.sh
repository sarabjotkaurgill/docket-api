#!/bin/sh

# Droping existing databse
dropdb docket

# Creating new 
createdb docket

# exporting environemnt
APP_ENV=local

# Delete Exisiting migration files
rm -r docket/db/migrations

# Creating new migrations
python ./manage.py makemigrations db --settings=docket.settings.local

# Delete Exisiting migration files
python ./manage.py migrate --settings=docket.settings.local
