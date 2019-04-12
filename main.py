from pyspark import SparkContext, SparkConf
from operator import add
import time

conf = SparkConf().setAppName("PythonWordCount 16 worker")
sc = SparkContext(conf=conf)

#"https://raw.githubusercontent.com/subpath/ChatBot/master/data/cornell%20movie-dialogs%20corpus/movie_lines.txt"
file = "movie_lines.txt"

lines = sc.textFile(file, 1).collect()

rdd = sc.parallelize(lines)

start = time.time()

counts = rdd.flatMap(lambda x: x.split(' ')).map(lambda x: (x, 1)).reduceByKey(lambda x,y:x+y).collect()

end = time.time()
print("time:", end - start)

sc.stop()

