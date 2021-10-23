# import pusher
import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db
from firebase_admin import storage
import time
import if01, ca01, fdo03b, de11
import de13, de15, de14, tp01, fd01
import os
import sys
from os.path import expanduser

# pusher_client = pusher.Pusher(
#   app_id='1170010',
#   key='09e7967cab3e368a361a',
#   secret='b669598e15011f056182',
#   cluster='us2',
#   ssl=True
# )


print("changing path")
home = expanduser("~")
my_path=f"{home}/converter/"
os.chdir(my_path)

cred = credentials.Certificate("./fileconverter-56a82-firebase-adminsdk-qfx0l-3b2f1c2a17.json")
init_firebase = firebase_admin.initialize_app(
    cred, {'databaseURL': "https://fileconverter-56a82-default-rtdb.firebaseio.com",  
    'storageBucket': "fileconverter-56a82.appspot.com",})

bucket= storage.bucket('fileconverter-56a82.appspot.com')


start_time=datetime.datetime.timestamp(datetime.datetime.utcnow())


parsers ={
    'if01' :if01.parse,
    'ca01': ca01.parse,
    'fd03b':fdo03b.parse,
    'de11' : de11.parse,
    'de13': de13.parse,
    'de15' : de15.parse,
    'de14': de14.parse,
    'tp01': tp01.parse,
    'fd01': fd01.parse,
}

inputfile =  sys.argv[1]
outputfile=sys.argv[2]
code = sys.argv[4]
filetype = sys.argv[3]



# 'unmodified/if1.xlsx','modified/if1.xlsx','if01'

#pusher_client.trigger('converter', 'started', {'started': start_time, 'code': code})

def download_file(input_file):
    output_filename= f"./temp/{int(time.time())}.xlsx"
    print(output_filename)
    try:
        blob = bucket.blob(input_file)
        blob.download_to_filename(output_filename)
    except Exception as e: 
        print(e)
        return
    return output_filename

def upload_file(filename, input_file):
    try:
        blob = bucket.blob(filename)
        with open(input_file, 'rb') as my_file:
            blob.upload_from_file(my_file)
    except Exception as e: 
        print(e)
        return

    return

def remove_file(myfile):
    try:
        os.remove(myfile)
    except OSError as e:  
        print ("Error: %s - %s." % (e.filename, e.strerror))

def do_convert(input_file, output_file, parser_type):
    filename = download_file(input_file)
    r = None
    if filename !=None:
        temp_output = filename.replace(".xlsx","_m.xlsx")
        if parser_type in parsers.keys():
            r=parsers[parser_type](filename, temp_output)
            upload_file(output_file,temp_output)
        remove_file(filename)
        remove_file(temp_output)
    return r


try:
    cities_ref = db.reference(code)    
    d={"status": "starting....."}
    cities_ref.update(d)
    result= do_convert(inputfile,outputfile, filetype)
    start_time=datetime.datetime.timestamp(datetime.datetime.utcnow())

    d={"status": "done",
    "error":"none",
    "inputfile" : inputfile,
    "outputfile":  outputfile,
    "filetype" : filetype,
    "doneAt": start_time,
    "result" : result
    
    }
    cities_ref.update(d)
except Exception as ex:
    print(ex)
    cities_ref.update(
        {
        "status": "done", 
        "error": f"Error with file: {inputfile} loading model \n {ex}",
        "doc":"none"
        }
    )


