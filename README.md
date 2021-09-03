# datamanagement-with-sqlalchemy
In this article, We will be creating a table named Movies and do CRUD operations on it using Python.

## What is Data Management?
Data management is the practice of collecting, keeping, and using data securely, efficiently, and cost-effectively.
We can manage the data through OOPS(classes) also. But, why database? the only difference is the data in the database world is stored in the hard disk persistently(permanently) whereas in classes the data is stored but in the instance(variables) which are stored in RAM(memory) temporarily.

## What is SQLite?
SQLite is a relational database management system contained in a C library. In contrast to many other database management systems, SQLite is not a client-server database engine. Rather, it is embedded into the end program. SQLite generally follows PostgreSQL syntax.

## What is SQLAlchemy?
SQLAlchemy is a library that facilitates the communication between Python programs and databases. Most of the time, this library is used as an Object Relational Mapper (ORM) tool that translates Python classes to tables on relational databases and automatically converts function calls to SQL statements.
* Let’s start, we require Python software, Flask_SQLAlchemy library, and DB Browser for SQLite(GUI tool for seeing the table(database)).
Since python is already installed we will be installing DB browser and Flask-SQLAlchemy using pip:
<b><i>pip install Flask-SQLAlchemy</i></b>

* In Class, we create a template we never give values there…similarly while creating a table we give the column names. The class name is the Table name.
Creating an Object(instantiate) of the class is similar to creating a record of the table.
class name =table name, class attributes = table column names, objects=records this relation between the class and the table is known as Object Relational Mapper(ORM).
We just need to use classes and functions all the database things will be taken care of and will be abstracted by SQLAlchemy. We as programmer don’t have to know SQL, all the things will be taken care by SQLAlchemy(ORM Library).
We will also be using Flask(It is an API of Python that allows us to build up web applications)
.
.
![ReadMore](https://krithikasharma2129.medium.com/data-management-with-python-sqlite-and-sqlalchemy-44cbb41aa9cf)

### Thank you! keep learning! keep growing! keep sharing!
