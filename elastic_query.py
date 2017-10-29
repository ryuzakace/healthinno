from elasticsearch import Elasticsearch 
from elasticsearch import helpers
import json
import time
import json 


ES_IP = ["18.220.193.187:9200"]
ES_INDEX = "sensor_data"
class Extract_Elastic():
    def __init__(self):
        self.es_conn = Elasticsearch(hosts = ES_IP)
        self.es_index = ES_INDEX
        self.doc_types =['blood-glucose', 'body-fat-percentage','blood-pressure-diastolic', 'blood-pressure-systolic', 'sleep-duration', 'body-temperature', 'tag-data']
    


    def get_data(self, person_id, st_timestamp, end_timestamp):

        query = """
                {
                "query": {
                    "bool": {
                        "must": {
                            "bool": {
                                "must": [{
                                        "match": {
                                            "person_id": {
                                                "query": "%s",
                                                "type": "phrase"
                                            }
                                        }
                                    },
                                    {
                                        "range": {
                                            "timestamp": {
                                                "from": %d,
                                                "to": %d,
                                                "include_lower": true,
                                                "include_upper": true
                                            }
                                        }
                                    }
                                ]
                            }
                        }
                    }
                }
            }"""%(person_id, st_timestamp, end_timestamp)
        data = {}
        for doc in self.doc_types:
            data[doc] = []
            page = self.es_conn.search(
                index = self.es_index,
                scroll = '3m',
                search_type = 'scan',
                doc_type = doc,  
                size = 10000,
                body = query)
            sid = page['_scroll_id']
            scroll_size = page['hits']['total']
            records = []
            while (scroll_size > 0):
                page = self.es_conn.scroll(scroll_id = sid, scroll = '2m')
                sid = page['_scroll_id']
                scroll_size = len(page['hits']['hits'])
                records = []
                for rec in page['hits']['hits']:    
                    es_doc = json.dumps(rec['_source'])
                    print es_doc
                    data[doc].append(es_doc)
        return data

print Extract_Elastic().get_data(person_id = "a123djvbvh23fv4vfd5", st_timestamp = 1509353124, end_timestamp= 1509365104)
                    
