# SQLAlchemy + Robot Framework 
This is a demo of a way of saving test execution results into a database, using SQLAlchemy 
library in Python for Robot Framework test automation. The tests are about getting response form a REST Api, and I save part of the response. 

The idea is to create a database and save some of the important values as records in the database so we can review and refer to those records later. For this demo I have selected sqlite because it is easy to use in python.


## Models
This is where the SQLAlchemy models for database tables are developed. Each table will 
have its own model with __tablename__ attribute and each column of table is represented 
as a class attribute of the model.

I have created two tables, first testcases table which will be responsible for keeping 
testcase general information, like name, suite name, time of execution. This model/table 
can have relationship with another table. Here I have people table where I keep record of people that have been returned by the REST Api under test.

## Utils
Place for generic functionalities, initializing the database with the schema is in manageDB.py, creating db session and passing the session to functions arguments are done with a python decorator in manageSession.py, and Test Setup and Test Teardown are also implemented in this directory.

## Queries 
Some helper functions which I use during test setup, teardown, and execution to add and update database records.


