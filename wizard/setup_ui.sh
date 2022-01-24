#!/bin/bash

# Wait for Elasticsearch to start up before doing anything.
until curl -s http://elasticsearch:9200/_cat/health -o /dev/null; do
    echo Waiting for Elasticsearch...
    sleep 1
done

# Wait for Kibana to start up before doing anything.
until curl -s http://kibana:5601/api/task_manager/_health -o /dev/null --head --fail; do
    echo Waiting for Kibana...
    sleep 1
done

# Wait for logstash to load the index
until curl -s http://elasticsearch:9200/emploi -o /dev/null --head --fail; do
  echo Waiting for index...
  sleep 1
done

cd /tmp

#load index pattern
#curl -X POST http://kibana:5601/api/index_patterns/index_pattern \
#  -H 'kbn-xsrf: true' \
#  -H 'Content-Type: application/json' \
#  -d'{"index_pattern": { "title":"emploi*", "type":"index-pattern", "id":"emploi-index-pattern-id", "timeFieldName":"date"}}'

#load dashboard
# curl -X POST http://kibana:5601/api/saved_objects/_import?createNewCopies=true -H "kbn-xsrf: true" --form file=@export.ndjson