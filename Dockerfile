FROM gettyimages/spark:latest
MAINTAINER Gibran Otazo "gibran.otazo@gmail.com"

USER root

RUN apt-get update \
 && apt-get install -y nano wget git python3 python3-pip \

WORKDIR $SPARK_HOME

RUN git clone https://github.com/gibrano/wordcount-pyspark.git
RUN cd wordcount-pyspark
RUN wget "https://raw.githubusercontent.com/subpath/ChatBot/master/data/cornell%20movie-dialogs%20corpus/movie_lines.txt"
