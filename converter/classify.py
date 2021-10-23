
from search_tweet import scrap_user
import sys


#from twitterscraper import query_tweets
import random
import json

import datetime

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db
import my_loaders as my_utils
import random
from twpy import TwpyClient 
from twpy.serializers import to_pandas, to_json, to_list
import dateutil.parser
#import bs_parser

import joblib
import pickle
import string
from nltk.corpus import stopwords
import os
import subprocess
from os.path import expanduser
import sys




def update_path(path, ref, temp):
    ref.child(path).update(temp)
   

def setup_intention_summary():
    temp_stats= {}
    for item in ['leonel','gonzalo','guillermo','abinader','ramfis','ninguno']:
        temp_stats[item]=0
    return temp_stats


def predict_intention( messages):
    bow4 = bow_transformer_intention.transform([messages])
    tfidf4 = tfidf_transformer_intention.transform(bow4)
    result = intention_model.predict(tfidf4)
    return result[0]

def predict_sentiment( messages):
    bow4 = bow_transformer_sentiment.transform([messages])
    tfidf4 = tfidf_transformer_sentiment.transform(bow4)
    result = sentiment_model.predict(tfidf4)
    return result[0]

# Data Cleaning
def text_process(mess):
    # Check characters to see if they are in punctuation
    nopunc = [char for char in mess if char not in string.punctuation]
    # Join the characters again to form the string.
    nopunc = ''.join(nopunc)
    # Now just remove any stopwords
    return [word.lower() for word in nopunc.split() if word.lower() not in stopwords.words('spanish')]


def load_intention_model():
    global messages_bow_intention, tfidf_transformer_intention, bow_transformer_intention
    global intention_model
    messages_bow_intention = joblib.load("./intention/vectorizer.pkl")
    tfidf_transformer_intention = joblib.load("./intention/bow_transformer.pkl")
    bow_transformer_intention = joblib.load("./intention/bow_transformer2.pkl")
    intention_model = pickle.load(open("./intention/GLN.pkl", "rb"))

def load_sentiment_model():
    global messages_bow_sentiment, tfidf_transformer_sentiment, bow_transformer_sentiment
    global sentiment_model
    messages_bow_sentiment = joblib.load("./sentiment/vectorizer.pkl")
    tfidf_transformer_sentiment = joblib.load("./sentiment/bow_transformer.pkl")
    bow_transformer_sentiment = joblib.load("./sentiment/bow_transformer2.pkl")
    sentiment_model = pickle.load(open("./sentiment/GLN.pkl", "rb"))



def classify_comment(comment):
    result={
        'text':'',
        'candidate':'ninguno',
        'value':0
    }
    candidato=None
    if "text" in comment.keys():
        text = comment["text"]
        result['text']= text
        candidato= predict_intention(text)
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
        #print("Candiato : {}".format(candidato))
        result["candidate"]=candidato
        result["value"] = 1
    return result


def classify_sentiment(text):
        r= predict_sentiment(text)
        sentiment ='neutral'
        if r==1.0:
            sentiment ="positive"
        elif r==2.0:
            sentiment = "negative"
        elif r==3.0:
            sentiment = "neutral"
        return sentiment


# Load Vocabulary for Vectorizer
# messages_bow_intention = None
# tfidf_transformer_intention = None
# bow_transformer_intention = None
# intention_model = None

# messages_bow_sentiment = None
# tfidf_transformer_sentiment = None
# bow_transformer_sentiment = None
# sentiment_model = None

text= sys.argv[1]
code = sys.argv[2]
# is_query = sys.argv[3]
# max_tweets = int(sys.argv[4])
# from_date = sys.argv[5]
# to_date = sys.argv[6]
# is_query= is_query=="true"

print(text)
# print(from_date)
# int_beg= [int(x) for x in from_date.split("-")]
# print(int_beg)
# begin_date= datetime.date(int_beg[0], int_beg[1],int_beg[2])

# int_beg= [int(x) for x in to_date.split("-")]
# end_date= datetime.date(int_beg[0], int_beg[1],int_beg[2])

home = expanduser("~")
my_path=f"{home}/find_and_clasify/"
# print(my_path)
# quit()
os.chdir(my_path)
#subprocess.call(['cd',"/home"])
# print(os.getcwd())
# print(f"Scrapping: {text}")
# print(f"Code: {code}")
# print(f"Limit: {max_tweets}")
# print(f"Query: {is_query}")
# print(f"From: {from_date}")
# print(f"to: {to_date}")
# print(f"being date {begin_date}")
# print(f"end date {end_date}")

print("Loading firebase")
configuration = my_utils.load_configuration("configuration.json")
print("loading json config")
cred = credentials.Certificate(configuration['firebase'])

init_firebase = firebase_admin.initialize_app(
    cred, {'databaseURL': "https://diapedemo.firebaseio.com/"})

print("Setting up paths")
status_path=f"status"
intention_path=f"intention"
sentiment_path=f"sentiment"
tweets_path=f"tweets"

# print(status_path)
status_ref= summary_ref = db.reference(code)

update_path(status_path, status_ref, {"status":"starting classification"})

# print("Loading intention model...")
# load_intention_model()
# print("loading sentiment model..")
# load_sentiment_model()

# intention_summary= setup_intention_summary()
# sentiment_summary= {}
# sentiment_summary['positive'] =0
# sentiment_summary['neutral'] = 0
# sentiment_summary['negative'] =0

#total_samples= 2000
#tweets =scrap_user(text, is_query , limit, from_date, to_date)
# tc = TwpyClient()
# tweets = tc.search(query=text, since=from_date, limit=total_samples)


# tweets= query_tweets(text, limit=total_samples,begindate= begin_date, enddate= end_date, lang="es",)

# print(len(tweets))
# sampled= len(tweets)
# #tweets = tc.search(username=user,  since=from_date, limit=max_news)
# #tweets.reverse()
# #max_tweets= total_samples-1
# random.shuffle(tweets)
# new_tweets=None
# if max_tweets< total_samples:
#     new_tweets = tweets[0:max_tweets]
# else:
#     new_tweets = tweets


# my_tweets =[]
# counter=0
# for tweet in tweets:
   
#     url ="https://twitter.com"+tweet.tweet_link
#     key = tweet.tweet_link[1:].replace('/','_').lower()
#     r= to_json([tweet])[0] 
#     r['url'] = url
#     r['tweet_date']= r['created_at']
#     r['key'] = key #+f"_{counter}"
#     counter+=1
#     my_tweets.append(r)
# print(len(my_tweets))
# for tweet in my_tweets:
#     print(tweet['created_at'])
#     # yourdate = dateutil.parser.parse(tweet['created_at'])
#     # print(yourdate)
#     end_date= datetime.datetime.strptime(tweet['created_at'], "%H:%m - %d %B %Y")
#     print(end_date)
# #     print(tweet)
# quit()
# print(len(my_tweets))


# results = {}
# counter=0
# repeated=0
# print(f"Clasifiying: {max_tweets}")
# for t in tweets:
#     tweet = t.__dict__
#     content  = tweet['text']
#     #timestamp =tweet["timestamp"].replace(tzinfo=timezone.utc).timestamp()

#     tweet["timestamp"] =  tweet["timestamp"].strftime("%Y-%m-%d %H:%M")
   
#     key = tweet["tweet_id"]
#     # print(key)
#     # print(tweet)
#     # quit()
#     if counter>= max_tweets:
#         break

#     if key in results.keys():
#         repeated+=1
#         continue
#     #print(content)
#     r= classify_comment({'text':content})
#     candidate = r['candidate']
#     tweet['candidate']= candidate
#     if candidate in intention_summary.keys():
#         intention_summary[candidate]+=1

#     sentiment = classify_sentiment(content)
#     tweet['sentiment'] = sentiment
#     if sentiment in sentiment_summary.keys():
#         sentiment_summary[sentiment]+=1
   
#     results[key] =tweet
#     counter+=1
#     #print(tweet)
#     #break
    
    

# #print(results)


# counter =len(results)

# debug_info =  {
#          "sampled":sampled,
#         'total':counter,
#          'from_date': from_date,
#          "limit" : max_tweets,
#          "query" : is_query,
#          "repeated": repeated,
#          "v":"1.30"
#         }
# print(debug_info)
# if True:
#     if counter>0:
#         update_path(tweets_path, status_ref, results)
#         update_path('debug', status_ref,debug_info)
#         update_path(sentiment_path, status_ref, sentiment_summary)
#         update_path(intention_path, status_ref,intention_summary )
#     update_path(status_path, status_ref, {"status":"done"})

# print(f"Done: {counter} ")