from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch('https://localhost:9200')

doc = {
    'date': datetime.now(),
    'text': 'Interensting content...',
    'timestamp': datetime.now(),
}
resp = es.index(index="nessqa",document=doc)
print(resp['result'])