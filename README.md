## DFM Technical Exercise Solution

Greetings, and welcome to my solution to the technical exercise.
The purpose of this README is to simply give a basic overview of 
the operation of the code and to offer a glimpse into the reasoning 
behind certain design decisions.

#### Overview

This code is written for user named 'thatguy' accessing the 'exercise' 
database (in Postgres), with the password matching the user name. 
Modifying line 11 in _server.py_ will allow these parameters to be changed.


###### Structure

The server operation code sits in _server.py_. Code related to parsing 
and database retrieval operations can be found in _data_processing.py_ and 
the SQLAlchemy model code is in _ucc_model.py_. There is also a small shared 
file entitled _shared.py_, where the SQLALchemy object is created for Flask 
integration. This is to avoid circular dependencies.


###### Running

This code may be run from the command line in Unix-like systems by 
simply executing the command `python server.py` from withing the 
working directory in which that file is located.

The database user and an empty database with the name used in 
server.py should be available on the local machine for connecting.


###### External Packages

This program does take advantage of some third-party packages to 
facilitate the task. They are outlined in the _requirements.txt_ 
file, which can be used to install any that you may be missing.


#### Design Decisions

And now for the *really* interesting part, a quick overview of some 
of the design decisions made.


###### Packages

I chose to use pandas for easy ingestion and cleanup of the data. 
It also facilitated writing the cleaned-up data to an external CSV. 

SQLAlchemy made for straightforward definition of the databse and quick 
work of querying it.


###### Data

As for data type choices, I opted to make _day_ non-nullable, as it 
seemed to be rather important and necessary to have a date present. 
Most other types were left nullable, as many of them seemed that it 
would be okay for them to be missing, at least until such time as those 
data were available. Missing may not be the desired end result, but 
it was left available to account for incomplete data at intermediate 
steps.

Certain ID fields, such as _Campaign ID_ and _Customer ID_ I converted 
to strings. It was not clear if they should be allowed to contain non-numeric 
characters and/or they might be long enough to exceed the size of a regular 
integer. As such, I opted for strings for flexibility.

Anything with a percentage had the % character stripped and were converted 
to floats for ease of processing, both for this task and in anticipation of 
future number-crunching tasks.


###### Presentation

Finally, the code queries items inserted in the database and collects them 
as a list of Python dictionaries. These are then easily passed to 
_json2html_'s _convert_ method, facilitating their display in an HTML table 
at /results.
