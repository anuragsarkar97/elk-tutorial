import sys
import json
from pprint import pprint
from elasticsearch import Elasticsearch


es = Elasticsearch(
    ['localhost'],
    port=9200
)
print(es)
with open('data.json') as f:
  data = json.load(f)
i = 0
for value in data:
    # if i > 3:
    #     break
    # value["name"]  = {
    #     "input" : list(value["authors"].split(","))
    # }
    value["name"] = value["authors"]
    es.index(index='book_index', doc_type='_doc', id= "_"+str(i) , body=value)
    i += 1
