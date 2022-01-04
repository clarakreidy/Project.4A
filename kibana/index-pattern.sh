curl -X POST localhost:5601/saved_objects/index-pattern/emploi  -H 'kbn-xsrf: true' -H 'Content-Type: application/json' -d '
{
  "attributes": {
    "title": "emploi*"
  }
}'