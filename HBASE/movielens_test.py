from starbase import Connection
import csv

c=Connection(port=8881)
ratings=c.table('ratings')
if(ratings.exists()):
	ratings.drop()
ratings.create('ratings')

batch=ratings.batch()
if batch:
	print("Batch update....\n")
	with open("c:/Users/NB69/Desktop/TIL/HBASE/ratings.csv","r")as f:
		reader=csv.reader(f,delimeter=',')
		next(reader)
		for row in reader:
			batch.update(row[0],{'rating':{ros[1]:row[2]}})
	print("Committing...\n")
	batch.commit(finalize=true)

	print("Get ratings for users...\n")
	print("Ratings for UserID 1: ")
	print(ratings.fetch("1"))

	print("\n")
	print("Ratings for UserID 33: ")
	print(ratings.fetch("33"))
