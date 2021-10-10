from time import sleep
import json
import requests 


# this links containg the areas per restaurant
f = open ('report_sample_data.json', "r",encoding='utf-8', errors='ignore')     
# Reading from file 
data = json.loads(f.read()) 
# Closing file 
f.close()

#api-endpoint 
URL_API = "http://127.0.0.1:8000/report_end_point/"
# URL_API= "http://13.58.90.148/post_newspaper/"

content={}
content = data


json_object = json.dumps(content, indent=4)
requests.post(url = URL_API, data = json_object)