# SQLAlchemy + Robot Framework 
This is a demo of a way of saving test execution results into a database, using SQLAlchemy 
library in Python for Robot Framework test automation. The tests are about getting response form a REST Api, and I save part of the response. 

The idea is to create a database and save some of the important values as records in the database so we can review and refer to those records later. For this demo I have selected sqlite because it is easy to use in python.

## DB
It contains generic functionalities for creating Base for models, creating database, and managing session by creating and closing.


## Models
This is where the SQLAlchemy models for database tables are developed. Each table will 
have its own model with __tablename__ attribute and each column of table is represented 
as a class attribute of the model. The models will extend a custom base model, which does has not tablename
and implement some common functionalities such as saving, deleting, updating, and __repr__ for each record.
</br>
I have created two tables, first testcases table which it will be responsible for keeping general information for each testcase, like name, suite name, time of execution. This model/table can have relationship with another table. H ere I have people table where I keep record of people that have been returned by the REST Api under test.


## Utils
Place for some functionalities to help with connecting Robot Framework and SQLAlchemy, for example creating session, adding new testcase in Test Setup, updating testcase status 
when testcase execution is done, and saving new person to db.

## Tests
This contains Robot Framework test suites. For this project I am using swapi.dev.



