FROM gettyimages/spark:latest
MAINTAINER Gibran Otazo "gibran.otazo@gmail.com"

USER root

RUN apt-get update \
 && apt-get install -y git python3 python3-pip \

WORKDIR $SPARK_HOME

RUN git clone https://github.com/gibrano/wordcount.git

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.6 2

