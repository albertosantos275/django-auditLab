import json
import time
import os
import datetime
import sys
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db
from firebase_admin import storage

import pprint
from os.path import expanduser


text= sys.argv[1]
code = sys.argv[2]

home = expanduser("~")
my_path=f"{home}/classify/"
# print(my_path)
# quit()
os.chdir(my_path)
cred = credentials.Certificate("./diapedemo-firebase-adminsdk-2x6oa-b2893547e5.json")

init_firebase = firebase_admin.initialize_app(
    cred, {'databaseURL': "https://diapedemo.firebaseio.com/",  
    'storageBucket': "diapedemo.appspot.com",})


cities_ref = db.reference(code)    
d={"status": "downloading....."}
cities_ref.update(d)


file2Download= storage.bucket('diapedemo.appspot.com')



#print(input_file)
# data= my_loaders.load_json(input_file)
# screen_name= data['screen_name']
# print(f"uploaded: {screen_name}")
# tweets_ref.child(screen_name).update(data)

time.sleep(10)

    
d={"status": "done", "doc": "sentencia"}
cities_ref.update(d)