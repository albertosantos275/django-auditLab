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
from google.cloud import storage as cloud_storage
from pdf2text_mine import text2pdf 

import pprint
from os.path import expanduser

import string
from nltk.corpus import stopwords
import joblib
import pickle

classifier_bow=None
tidf_classifier= None
bow_transformer_classifier = None
classifier_model =  None

# Data Cleaning
def text_process(mess):
    # Check characters to see if they are in punctuation
    nopunc = [char for char in mess if char not in string.punctuation]
    # Join the characters again to form the string.
    nopunc = ''.join(nopunc)
    # Now just remove any stopwords
    return [word.lower() for word in nopunc.split() if word.lower() not in stopwords.words('spanish')]


def getDocClass(docType):
    print(docType)
    if docType == 1.0:
        return "acto"
    elif docType == 2.0:
        return "sentencia"
    else:
        return "none"

def load_classifier():
    global classifier_bow, tidf_classifier, bow_transformer_classifier
    global classifier_model
    classifier_bow = joblib.load("./classifier/vectorizer.pkl")
    tidf_classifier = joblib.load("./classifier/tfidf_transformerpdf.pkl")
    bow_transformer_classifier = joblib.load("./classifier/bow_transformerpdf.pkl")
    classifier_model = pickle.load(open("./classifier/MODELOPDF.pkl", "rb"))


def do_classification( messages):
    bow4 = bow_transformer_classifier.transform([messages])
    tfidf4 = tidf_classifier.transform(bow4)
    result = classifier_model.predict(tfidf4)
   
    return result[0]


text= sys.argv[1]
code = sys.argv[2]
where = sys.argv[3]
docClass="none"

# if where =="home":
#     home = expanduser("~")
# else:
# my_path=f"{home}/classify/"
# # print(my_path)
# # quit()
# os.chdir(my_path)
cred = credentials.Certificate("./diapedemo-firebase-adminsdk-2x6oa-b2893547e5.json")

init_firebase = firebase_admin.initialize_app(
    cred, {'databaseURL': "https://diapedemo.firebaseio.com/",  
    'storageBucket': "diapedemo.appspot.com",})

cities_ref = db.reference(code)    
d={"status": "loading....."}
cities_ref.update(d)

try:
    load_classifier()
except Exception as e:
    print(e)
    cities_ref.update(
        {"status": "done", 
        "error": f"Error with file: {text} loading model \n {e}",
        "doc":"none"
        }
    )
    quit()


cities_ref = db.reference(code)    
d={"status": "downloading....."}
cities_ref.update(d)


bucket= storage.bucket('diapedemo.appspot.com')

output_filename= f"./temp/{int(time.time())}.pdf"
print(output_filename)
try:

   
    blob = bucket.blob(text)
    blob.download_to_filename(output_filename)
except Exception as e: 
    print(e)
    cities_ref.update(
        {"status": "done", 
        "error": f"Error downloading file: {text} \n {e}",
        "doc":"none"
        }
    )
    quit()
    

if not os.path.exists(output_filename):
    print("file does no exists")
    cities_ref.update(
        {"status": "done", 
        "error": f"file does not exist: {output_filename} ",
        "doc":"none"
        }
    )
    quit()


try:
    #change to text 
    d={"status": "changing pdf to text....."}
    cities_ref.update(d)

    pdf_text = text2pdf(output_filename)
    if os.path.exists(output_filename):
        os.remove(output_filename)
   
    #pdf_text=text_process(pdf_text)
    # print(pdf_text)
    #need to preprocess
    docType = do_classification(pdf_text)
    docClass = getDocClass(docType)
    

    #classify


    #remove files
    
    d={"status": "done", "doc": docClass, "docType": f"{docType}",
    "error":"none"}
    cities_ref.update(d)
except Exception as e:
     print(e)
     cities_ref.update(
        {"status": "done", 
        "error": f"Error with file: {text} \n {e}",
        "doc":"none"
        }
    )


 