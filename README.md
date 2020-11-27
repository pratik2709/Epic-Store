## Setup
* Pull the code from this git repository
* This app uses docker and docker-compose
* Create containers using this command in the root directory:
```
docker-compose build
```
* Run all database migrations with:
```
sudo docker-compose run web python manage.py makemigrations
sudo docker-compose run web python manage.py migrate
```
* Once the containers are created, 
data can be loaded with the following command:
```
sudo docker-compose run web python manage.py load_data
``` 
* Tests can be run using the following command:
```
sudo docker-compose run web python manage.py test
```
* The containers can be started using the following command:
```
docker-compose up
```
## Database
* Keeping future scalability in mind I have tried to minimize Database joins
(Instead I am doing multiple queries in the application itself)
* Intially the plan was to use MongoDB. But it is not well supported 
in the latest Django 3.1.0
* So decided to go ahead with Postgres-SQL and make use of the JSONB field 
* Another approach would have been to use Postgres without JSONB 
and avoid JOINS by using separate queries

## Populating the database
* I have created a management script to populate the data.
* Part of this code is also used while doing integration tests

## APIs in the application
* Login API (Auth successful with username and pass)
* Show appropriate games API: This API shows 
the recommended games according to the user preferences
* Buy Game API: This is a dummy API for demonstrating a POST Request
* Maker-Breaker Game API: have not attempted 
this as per the discussion
(can implement once I have a better understanding)

## Security
* Uses Django's inbuilt token mechanism to authenticate APIs

## Swagger
* Login into swagger using the following url: http://localhost/swagger/
* Use the 'api-token-auth' API to get the bearer key 
* use the following as credentials:
```
{
  "username": "Adrian",
  "password": "password"
}
```
* click authorize on top right hand corner of the page and enter the value: 
```
'Token <your-key>'
```
* Explore the APIs!

## Deployment
* There are 2 separate docker containers: 
one for database and other for the app
* Another one can be added in future for nginx (as a reverse proxy) 
in case the app needs to be deployed


## User-Interface
* Was not able to add the user interface due to the time constraints
* I have recently created a minimalist blog app using Svelte Framework. 
To demonstrate my front-end skills I am leaving a link to that: 
http://namastespock.eastus.cloudapp.azure.com/#/


          
