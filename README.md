## Setup
* Pull in the code from this git repository
* This app uses docker and docker-compose
* Create containers using:
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

## Database
* Keeping future scalability in mind I have tried to minimize Database joins
(Instead I am doing multiple queries in the application itself)
* Intially the plan was to use MongoDB. But it is not well supported 
in the latest Django 3.1.0
* So decided to go ahead with Postgres-SQL and make use of the JSONB field 
* The data in Preferences in User Table and Attributes Table seem 
ok if duplicated (and so can be stored as JSON)
* Another option would have been to use Postgres without JSONB 
and do without doing JOINS by using separate queries

## Populating the database
* I have created a management script to populate the data.
* Parts of this code is also used while doing integration tests

## APIs in the application
* Login API (Auth successful with username and pass)
* Show appropriate games API: This API
* Buy Game API: This is a dummy API for demonstrating a POST Request
* Maker-Breaker Game API: have not attempted 
this as per the discussion with Madhusudan 
(can implement once I have a better understanding)

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
* click authorize and enter the value: 'Token <your-key>'
* Explore the APIs!

## User-Interface
* Was not able to add the user interface due to the time constraints
* I have recently created a minimalist blog app using Svelte Framework. 
To demonstrate my skills I am leaving a link to that: 
http://namastespock.eastus.cloudapp.azure.com/#/
          
