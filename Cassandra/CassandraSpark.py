from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql import functions

def parseInput(line):
	fields=line.split('|')
	return Row(user_id=int(fields[0]),age=int(fields[1]),gender=fields[2],
		occupation=fields[3],zip=fields[4]

if __name__=="__main__":
	spark=SparkSession.builder.appName("CassandraIntegration").config("spark.cassandra.connection.host","127.0.0.1").getOrCreate()

	lines=spark.sparkContext.textFile("hdfs:///user/maria_dev/ml-100k/u.user")
	users=lines.map(parseInput)
	userDataset=spark.createDataFrame(users)

	userDataset.write.format("org.apache.spark.sql.cassandra")\
		.mode('append')\
		.options(table="users",keyspace="movielens")\
		.save()
	readUser=spark.read\
		.format("org.apache.spark.sql.cassandra")\
		.options(table="users",keyspace="movielens")\
		.load()
	readUser.createOrReplaceTempView("users")
	
	sqlDF= spark.sql("SELECT * FROM users WHERE age<20")
	sqlDF.show()
	spark.stop()

