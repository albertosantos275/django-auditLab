import random
import json
import greenstalk
import unidecode
import datetime
import time
#from model.model import load_model, predict
#import  model.predict
import string
import my_utils

#REMOVE THIS
import joblib
import pickle
import string
from nltk.corpus import stopwords


def replace_accent(accented_string):
    # accented_string is of type 'unicode'
    unaccented_string = unidecode.unidecode(accented_string)
    return unaccented_string

def get_provincia(provincia):
    if provincia is None:
        return 'none'
    print(provincia)
    provincia = provincia.lower()
    provincia= replace_accent(provincia)
    vals= provincia.split(',')
    return vals


def parse_data(item):
     #print(item['user'])
    location="none"
    if "location" in item['user'].keys():
        location=item['user']['location']
    if "extended_tweet" in item.keys():
        text= item["extended_tweet"]["full_text"]
        #print("has extended text")
    else:
        text = item['text']
    date= item["created_at"]
    date= date.replace("+0000",'')
    #d = datetime.datetime.strptime(date)
    d=time.strptime(date)
    date_str= "%d%02d%02d"%(d.tm_year,d.tm_mon,d.tm_mday)
    vals= get_provincia(location)
    #print(vals)
    temp = {
        'date' : date_str, #date,
        'provincia': vals[0], #  prov,
        'candidate':  '', #candidate,
        'value':1
    }
    return text, temp




###############REMOVE THIS LATER
#Predict
def predict( messages):
    bow4 = bow_transformer.transform([messages])
    tfidf4 = tfidf_transformer.transform(bow4)
    loaded_model = pickle.load(open("./pesos/GLN.pkl", "rb"))
    result = loaded_model.predict(tfidf4)
    return result[0]


# Data Cleaning
def text_process(mess):
    # Check characters to see if they are in punctuation
    nopunc = [char for char in mess if char not in string.punctuation]
    # Join the characters again to form the string.
    nopunc = ''.join(nopunc)
    # Now just remove any stopwords
    return [word.lower() for word in nopunc.split() if word.lower() not in stopwords.words('spanish')]


# Load Vocabulary for Vectorizer
messages_bow = joblib.load("./pesos/vectorizer.pkl")
tfidf_transformer = joblib.load("./pesos/bow_transformer.pkl")
bow_transformer = joblib.load("./pesos/bow_transformer2.pkl")


credentials = my_utils.load_configuration("configuration.json")
queue = greenstalk.Client(host= credentials['b_host'], port=credentials['b_port'])
queue.watch(credentials['tweets_tube'])
queue.use(credentials['stats_tube'])
#model = load_model()

# 1- Gonzalo
# 2- Abinader
# 3- Leonel
# 4-Ramfis 
# 5- Ninguno
while True:
    job= queue.reserve()
    data = json.loads(job.body)
    text, temp= parse_data(data)
    candidato= predict(text)
    print(candidato)
    if candidato==1.0:
        candidato ="gonzalo"
    elif candidato==2.0:
        candidato = "abinader"
    elif candidato==3.0:
        candidato = "leonel"
    elif candidato ==4.0:
        candidato = "ramfis"
    else:
        candidato="ninguno"
    
    temp["candidate"]=candidato
    
    print(text)
    print("Clasifado como: {}".format(candidato))
    print("Conteo {}\n".format(temp))
    
    queue.delete(job)
    r = {'stats': temp , 'tweet': data}
    body = json.dumps(r)
    print("json : {}".format(body))
    queue.put(body)


