# wordcount-pyspark

# Build the image.
sudo docker build -t wordcount-pyspark --no-cache .

# Up the cluster.
sudo docker-compose up --scale worker=1

# Get in to docker master.
sudo docker exec -it wordcount_master_1 /bin/bash

# Run the app.
spark-submit --master spark://172.19.0.2:7077 wordcount-pyspark/main.py
