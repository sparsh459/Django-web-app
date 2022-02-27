# Django-web-app
This is a Django web management app which manages the authors and books models in database with exporting it as a csv file 


All the file are already in the repo:

Push on heroku was not possible due to erro : fails to push some ref's to designated url on heroku


for import data from csv to models, steps are listed below:
- go to sqlite.org
- got to downloads
- under the section Preoccupied Binaries for Windows install: 
- download sqlite-tols-win32-x86(A bundle of cmd tools...)
- from this file get the sqlite3.exe and put it in project folder
- go to terminal
- run sqlite3.exe db.sqlite3
- a sqlite terminal will open 
- run .mode csv
- check teh files have no column headings before using it and everything is formatted
- then run :  .import <filename.csv> <model table name>
