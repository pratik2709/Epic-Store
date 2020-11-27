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
* Intially the plan was to use MongoDB. But it is not well supported 
in the latest Django 3.1.0
* So decided to go ahead with Postgres-SQL and make use of the JSONB field 
* Keeping future scalability in mind I have tried to minimize DataBase joins
* The Preferences in User Table and Attributes Table seem 
ok if duplicated (and so can be stored as JSON)
* Another option would have been to use Postgres without JSONB 
and do without doing JOINS by using separate queries

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
          
