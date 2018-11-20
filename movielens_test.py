from starbase import Connection
import csv

c=Connection()
ratings=c.table('ratings')
if(ratings.exists()):
	ratings.drop()
ratings.create('ratings')

batch=ratings.batch()
if batch:
	print("Batch update....\n")
	with open("c:/Users/NB69/Desktop/TIL/movie")