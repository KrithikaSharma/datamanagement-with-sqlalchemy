#email: krithikasharma2129@gmail.com
# fullname: Sevda Krithika Sharma

from flask import Flask
from flask_sqlalchemy import SQLAlchemy #loading the library (driver) to interact with database

app=Flask("dbapp") #app name

#giving path(URI) to the app
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///mydb/data.sqlite' #connecting to database


#ORM: Object Relational Model
db = SQLAlchemy(app) # creating a new database for the app
print(db)


class Movies(db.Model):
	mid=db.Column(db.Integer, primary_key=True)
	moviename = db.Column( db.Text )
	actor = db.Column( db.Text )
	actress = db.Column( db.Text )
	yearofrelease = db.Column( db.Integer )
	director  = db.Column( db.Text )

	def __init__(self, moviename, actor, actress, yearofrelease, director):
		self.moviename=moviename
		self.actor=actor
		self.actress=actress
		self.yearofrelease=yearofrelease
		self.director=director

db.create_all()


### CRUD Operations ###


#******  1.Create  ******
def addrecord(mname,actor,actress,yor,director):
	obj=Movies(mname,actor,actress,yor,director)
	db.session.add(obj)
	db.session.commit()

addrecord("Shershaah","Sidhart Malhotra","Kiara Advani",2021,"Vishnu Vardhan")
addrecord("Gunjan Saxsena","Pankaj Tripati","Janhvi Kapoor",2020,"Sharan Sharma")
addrecord("Bhuj","Ajay Devgan","Pranita Subhash",2021,"Abhishek Dundhaiya")
addrecord("Lage Raho Munna Bhai","Sanjay Dutt","Vidya balan",2006,"Rajkumar Hirani")
addrecord("Muna Bhai MBBS","Sanjay Dutt","Gracy Singh",2003,"Rajkumar Hirani")
addrecord("Bajrangi Bhaijan","Salman Khan","Kareena Kapooor",2015,"Kabir Khan")
addrecord("Kesari","Akshay Kumar","Parneeti Chopra",2019,"Anurag Singh")
addrecord("Parmanu","John Abraham","Diana Penty",2018,"Abhishek Sharma")
addrecord("Angrezi Medium","Irfan khan","Radhika Madan",2020,"Homi Adjania")


#******  2.Read  ******

r2c=Movies.query.filter_by(director="Rajkumar Hirani").count()
print(f"There are {r2} records with director as Rajkumar Hirani")


#query all
rall=Movies.query.all()
for i in range(len(rall)):
	print(rall[i].moviename)

#query on parameter
ryor=Movies.query.filter_by(yearofrelease=2021)
for i in range(len(ryor.all())):
	print(ryor.all()[i].moviename, ryor.all()[i].actor, ryor.all()[i].yearofrelease )

#******  3. Update  ******

rsher=Movies.query.filter_by(moviename="Shershaah")
print(rsher.all())
for i in rsher.all():
    i.director="directorchanged"
    print(f"Director of {i} changed")
db.session.commit()

# adding another record
addrecord("Dangal","Amir Khan","Fatima Sana Shaikh",2016,"Nitesh Tiwari")
db.session.commit()
print("New record added!!")

#******  4. Delete  ******
#deleting director "Rajkumar Hirani" films

rdf=Movies.query.filter_by(director="Rajkumar Hirani")
for i in rdf.all():
    print("Deleting Movie : ", rdf.all()[0])
    print(i)
    db.session.delete(rdf.all()[0]) 
    db.session.commit()

#deleting kesari record

rkes=Movies.query.filter_by(moviename="Kesari")
print(rkes.all())
db.session.delete(rkes.all()[0])
db.session.commit()
print(f"Movie {rkes.all()} deleted")

#deleting all records
rall=Movies.query.all()
print(rall)
for i in range((len(rall))):
    print("Deleting Movie")
    db.session.delete(rall[i])
    db.session.commit()


###########     Thank You      ###########