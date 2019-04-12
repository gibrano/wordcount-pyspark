from pyspark import SparkContext, SparkConf
from operator import add
import time

conf = SparkConf().setAppName("PythonWordCount 1 worker")
sc = SparkContext(conf=conf)

#"https://raw.githubusercontent.com/subpath/ChatBot/master/data/cornell%20movie-dialogs%20corpus/movie_lines.txt"
file = "movie_lines.txt"

lines = sc.textFile(file, 1)

start = time.time()

counts = lines.flatMap(lambda x: x.split(' ')).map(lambda x: (x, 1)).reduceByKey(add).collect()

end = time.time()
print(end - start)

for (word, count) in counts:
        print("%s: %i" % (word, count))

sc.stop()
