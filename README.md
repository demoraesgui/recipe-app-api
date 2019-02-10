## Recipe APP API ![Build Status](https://travis-ci.com/guilhermevdm/recipe-app-api.svg?branch=master)
API for creating and managing Recipes, also it's able to create Ingredients and Tags. 

## Motivation
This project was created to learn a bit more about Web Development by making a simple API using Test Driven Development and Travis-CI to run the tests and linting.

## Framework
Django and Django REST Framework was used to create this project.

## How to use?
Install [pipenv](https://pypi.org/project/pipenv/)
and then run `pipenv sync`, to activate the virtual environment run `pipenv shell`.
Make sure to have docker and docker-compose installed and then start postgres service by running `docker-compose up -d` 

Then you can run:

```
python manage.py makemigrations
python manage.py migrate
python manage.py test
python manage.py runserver
```
If necessary run `python manage.py createsuperuser` to get access to the admin page.
