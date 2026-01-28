# Logs Aggregation

This is a Logs Aggregation pipeline made using an ELK i.e. ElastiSearch, Logstash, Kafka, and Kibana along with zookeeper and kafka. 
The pipeline handles and filters logs produced from multiple simulated microservices from a website. 
Simulated logs of error or critical severity are sent to LogTail for monitoring and alerting. 

# Pipeline Methodology

The simulated log json objects are first detected by Filebeat. 
Filebeat sends the json objects to kafka where the logs are temporarily stored.
If elasticsearch is down, kafka stores the logs temporarily otherwise logs are sent to logstash for further parsing. 
After parsing, the final log is stored in elasticsearch after which it is viewed in Kibana.
Logs of error or critical severity are sent to LogTail for live monitoring of the simulated system. 

# Performance metrics
  - The LAG from kafka consumer group is ~ 0 during the light load test
  - The LAG from kafka consumer group is ~ 525 during the heavy load test
  - The LAG from kafka consumer group is ~ 1600 during the error burst test

# Files
  - filebeat.yml: Input filebeat and output kafka configuration setup
  - app.log/auth.log/payment.log/sql.log/: Stores the simulated messy log json objects
  - logstash_conf: Input kafka configuration, filtering the messy log json objects, and storing of logs in elasticsearch
  - docker-compose.yml: Docker configuration file for dependencies
  - pipeline_dash.ndjson: Kibana dashboard file
  - stress_test.py: simulated stress test on pipeline

# Dependencies 
  - Docker images
    - Filebeat
    - Zookeeper
    - Kafka
    - Logstash
    - ElasticSearch
    - Kibana

# Usage
  The following sequence of commands may be executed to simulate the pipeline:
    - docker compose up -d
    - python3 stress_test.py
  
  - The Kibana dashbaord can viewed using the following procedure:
    - Download the provided ndjson file   
    - Go to Stack Management on Kibana
    - Click Saved Objects and then Import
    - Upload the ndjson file

# Limitations

  Docker configurations were used to setup ELK, Zookeeper and Kafka due to the large amounts of RAM and CPU consumed by the resources.
  The metrics such as LAG values from the kafka consumer group may vary since it is highly dependent on the hardware it is run on. 

# Future Work

  

# Author
  - Shriyans Sharma
