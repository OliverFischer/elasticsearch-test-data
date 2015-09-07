__author__ = 'ofischer'

import elasticsearch
import pickle

es = elasticsearch.Elasticsearch()

res = es.search(
    index = "test_data",
    body={"query": {"match_all": {}}, "size" : 100000, "fields" : ["_id"]}
)
ids = [d['_id'] for d in res['hits']['hits']]

pickle.dump(ids, open("grabbed_ids.txt", "wb"))

