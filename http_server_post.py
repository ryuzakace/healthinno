#POST HTTP SERVER
from elasticsearch import Elasticsearch
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import re
import json

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>hi!</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = json.loads(self.rfile.read(content_length))
        print post_data
        self.process_invoke(post_data)
        self._set_headers()
        self.wfile.write("Data Received")

    def process_invoke(self, post_data):
        dp = DataPreprocessing()
        std_json_dict =  dp.format_json(post_data)
        elastic_ind = PushToElastic("sensor_data")
        for key in std_json_dict.keys():
            if key == 'blood-pressure':

                elastic_ind.put_doc(json.loads(std_json_dict[key][0]), "blood-pressure-diastolic")
                elastic_ind.put_doc(json.loads(std_json_dict[key][1]), "blood-pressure-systolic")
            else:
                elastic_ind.put_doc(json.loads(std_json_dict[key]), key)
        return 




class PushToElastic():
    def __init__(self, index_name):
        self.es_conn = Elasticsearch(hosts = ["localhost:9200"])
        self.index_name = index_name

    def checkIndex(self, index_name):
        if self.es_conn.indices.exists(index_name):
            return 0
        else:
            return 1

    def create_index(self):
        es_mapping ="""{
    "template": "Sensor Data",

    "mappings": {
        "heart-rate": {
            "dynamic_templates": [{
                "strings": {
                    "match": "*",
                    "mapping": {
                        "type": "string"
                    }
                }
            }],
            "properties": {
                "timestamp": {
                    "type": "date",
                    "null_value": "null"
                },
                "value": {
                    "type": "string",
                    "null_value": ""
                },

                "unit": {
                    "type": "string",
                    "null_value": ""
                },
                "sensor_name": {
                    "type": "string",
                    "null_value": ""
                },
                "sensor_id": {
                    "type": "string",
                    "null_value": ""
                },
                "person_id": {
                    "type": "string",
                    "null_value": ""
                }
            }
        }
    },

    "blood-glucose": {
        "dynamic_templates": [{
            "strings": {
                "match": "*",
                "mapping": {
                    "type": "string"
                }
            }
        }],
        "properties": {
            "timestamp": {
                "type": "date",
                "null_value": "null"
            },
            "value": {
                "type": "string",
                "null_value": ""
            },

            "unit": {
                "type": "string",
                "null_value": ""
            },
            "sensor_name": {
                "type": "string",
                "null_value": ""
            },
            "sensor_id": {
                "type": "string",
                "null_value": ""
            },
            "person_id": {
                "type": "string",
                "null_value": ""
            }

        }
    },
    "body-fat-percentage": {
        "dynamic_templates": [{
            "strings": {
                "match": "*",
                "mapping": {
                    "type": "string"
                }
            }
        }],
        "properties": {
            "timestamp": {
                "type": "date",
                "null_value": "null"
            },
            "value": {
                "type": "string",
                "null_value": ""
            },

            "unit": {
                "type": "string",
                "null_value": ""
            },
            "sensor_name": {
                "type": "string",
                "null_value": ""
            },
            "sensor_id": {
                "type": "string",
                "null_value": ""
            },
            "person_id": {
                "type": "string",
                "null_value": ""
            }

        }
    },
    "blood-pressure-diastolic": {
        "dynamic_templates": [{
            "strings": {
                "match": "*",
                "mapping": {
                    "type": "string"
                }
            }
        }],
        "properties": {
            "timestamp": {
                "type": "date",
                "null_value": "null"
            },
            "value": {
                "type": "string",
                "null_value": ""
            },

            "unit": {
                "type": "string",
                "null_value": ""
            },
            "sensor_name": {
                "type": "string",
                "null_value": ""
            },
            "sensor_id": {
                "type": "string",
                "null_value": ""
            },
            "person_id": {
                "type": "string",
                "null_value": ""
            }

        }
    },
    "blood-pressure-systolic": {
        "dynamic_templates": [{
            "strings": {
                "match": "*",
                "mapping": {
                    "type": "string"
                }
            }
        }],
        "properties": {
            "timestamp": {
                "type": "date",
                "null_value": "null"
            },
            "value": {
                "type": "string",
                "null_value": ""
            },

            "unit": {
                "type": "string",
                "null_value": ""
            },
            "sensor_name": {
                "type": "string",
                "null_value": ""
            },
            "sensor_id": {
                "type": "string",
                "null_value": ""
            },
            "person_id": {
                "type": "string",
                "null_value": ""
            }

        }
    },
    "sleep-duration": {
        "dynamic_templates": [{
            "strings": {
                "match": "*",
                "mapping": {
                    "type": "string"
                }
            }
        }],
        "properties": {
            "timestamp": {
                "type": "date",
                "null_value": "null"
            },
            "value": {
                "type": "string",
                "null_value": ""
            },

            "unit": {
                "type": "string",
                "null_value": ""
            },
            "sensor_name": {
                "type": "string",
                "null_value": ""
            },
            "sensor_id": {
                "type": "string",
                "null_value": ""
            },
            "person_id": {
                "type": "string",
                "null_value": ""
            }

        }
    },
    "body-temperature": {
        "dynamic_templates": [{
            "strings": {
                "match": "*",
                "mapping": {
                    "type": "string"
                }
            }
        }],
        "properties": {
            "timestamp": {
                "type": "date",
                "null_value": "null"
            },
            "value": {
                "type": "string",
                "null_value": ""
            },

            "unit": {
                "type": "string",
                "null_value": ""
            },
            "sensor_name": {
                "type": "string",
                "null_value": ""
            },
            "sensor_id": {
                "type": "string",
                "null_value": ""
            },
            "person_id": {
                "type": "string",
                "null_value": ""
            }

        }
    },
    "tag-data": {
        "dynamic_templates": [{
            "strings": {
                "match": "*",
                "mapping": {
                    "type": "string"
                }
            }
        }],
        "properties": {
            "timestamp": {
                "type": "date",
                "null_value": "null"
            },
            "value": {
                "type": "string",
                "null_value": ""
            },
            "person_id": {
                "type": "string",
                "null_value": ""
            }
        }
    }
}"""
        json.loads(es_mapping)
        resp = self.es_conn.indices.create(index= self.index_name , body = es_mapping)


    def put_doc(self, data, doc_type):
        if self.checkIndex(self.index_name) ==1:
            self.create_index()
        if len(data.keys())==3:

            resp =  self.es_conn.create(index = self.index_name, doc_type = doc_type,id=(str(data['person_id'])+str(data['timestamp'])), body = json.dumps(data))
            return  
        print data
        key = str(data['person_id'])+str(data['sensor_id'])+str(data['timestamp'])
        try:
            resp =  self.es_conn.create(index = self.index_name, doc_type = doc_type,id= key, body = json.dumps(data))
        except:
            print "Already Exists %s"%id



class DataPreprocessing():
    
    def __init__(self):

        self.field_name = {}
        # self.field_name['heart-rate'] = ["person_id","timestamp","sensor_id","value","unit"]
        # self.field_name['blood-glucose'] = ["value","unit","person_id","timestamp","sensor_id"]
        # self.field_name['body-fat-percentage'] = ["person_id","timestamp","value","unit","sensor_id"]
        # self.field_name['blood-pressure-diastolic'] = ["person_id","timestamp","value","unit","sensor_id"]
        # self.field_name['blood-pressure-systolic'] = ["person_id","timestamp","value","unit","sensor_id"]
        # self.field_name['sleep-duration'] = ["person_id","timestamp","value","unit","sensor_id"]
        # self.field_name['body-temperature'] = ["person_id","timestamp","value","unit","sensor_id"]
        self.regs= {
        "heart-rate":"heart_",
        "blood-glucose": "glucose_",
        "body-fat-percentage": "fat_", 
        "blood-pressure" : "bp_", 
        "sleep-duration": "sleep_", 
        "body-temperature" : "temperature_"}

        #self.sensor_names = ["heart-rate", "blood-pressure", "blood-glucose", "sleep-duration", "body-fat-percentage", "body-temperature"]

        self.field_mapping = {"value": "value", "timestamp":"timestamp", "fullform":"sensor_name", "user":"person_id","sensor_id":"sensor_id", "unit":"unit",}

        self.field_name['tag-data'] = ["person_id","timestamp","value"]


        self.sensor_ids = {"heart-rate":101, "blood-glucose":201, "body-fat-percentage":301, "blood-pressure-diastolic":401, "blood-pressure-systolic":401,"sleep-duration":501, "body-temperature":601}

    def process_bp(self, keys):
        common_keys= ['user', 'timestamp', 'fullform']
        data_systolic = {}
        data_diastolic = {}
        for i in common_keys:
            data_systolic[self.field_mapping[i]]= data_diastolic[self.field_mapping[i]] = self.data[self.regs["blood-pressure"]+i]

        data_diastolic['value'] = self.data['bp_value1']
        data_diastolic['unit'] = self.data['bp_unit1']
        data_diastolic['sensor_id'] = self.sensor_ids['blood-pressure-diastolic']
        
        data_systolic['value'] = self.data['bp_value']
        data_systolic['unit'] = self.data['bp_unit']
        data_systolic['sensor_id'] = self.sensor_ids['blood-pressure-systolic']
        
        return [json.dumps(data_diastolic), json.dumps(data_systolic)]
        
    
    def format_json(self, data):

        self.data = data
        headers = data.keys()
        if len(headers) == 3:
            return {"tag-data":json.dumps(data)}
        else:
            sensor_data = {}
            for sensor in self.regs.keys():
                keys = [re.sub(self.regs[sensor], "", key) for key in headers if re.match(self.regs[sensor], key)]
                if len(keys) > 6:
                    sensor_data["blood-pressure"] = self.process_bp(keys)
                else:
                    temp = {}
                    for key in keys:
                        if key in self.field_mapping:
                            temp[self.field_mapping[key]] = self.data[self.regs[sensor]+key]
                        else:
                            continue
                    temp["sensor_id"] = self.sensor_ids[sensor]
                    sensor_data[sensor] = json.dumps(temp)
            return sensor_data


    
        
def run(server_class=HTTPServer, handler_class=S, port=49091):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()