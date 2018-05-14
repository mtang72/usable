import json
import twitter as tw
import time

f = open('out.txt', 'w')

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '346936472-BuK6K6BvgXjxy3oHY9q0B5ibP01Ve5exjzRCQzuf'
ACCESS_SECRET = 'y2tGQgFpISWPMfpEb60BosmKmGErCNlvHKqycZBJSbvU7'
CONSUMER_KEY = 'n4BAY7E7l7t1559wblkn425UR'
CONSUMER_SECRET = 'oi7Ra9tsu9nzcDcf6sxVVqnLa9x7HdUFGoYjaDdDKibsjx65KF'

oauth = tw.OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
tstream = tw.TwitterStream(auth=oauth)

keywords = """data security,data privacy,cybersecurity,digital security,digital privacy,internet privacy,internet security,
computer privacy,surveillance,internet rights,internet censorship,internet monitoring,internet safety,online privacy"""
# Get a sample of the public data following through Twitter
iterator = tstream.statuses.filter(track=keywords, language="en")
time_start = time.time()
delaycheck = time.time()
print("\n---------------------------------------------------\nStarted at time: {}\
        \n---------------------------------------------------\n".format(time.asctime(time.localtime(time_start))),file=f)
for tweet in iterator:
    try:
        print(tweet['text'].strip('\n').lstrip('\n'),file=f)
    except KeyError:
        print("\n---------------------------------------------------\nConnection dropped at time: {}\
            \n---------------------------------------------------\n".format(time.asctime(time.localtime(delaycheck))),file=f)
        exit()
    if time.time() >= time_start+28800:
        break
    delaycheck = time.time()

print("\n---------------------------------------------------\nEnded at time: {}\
        \n---------------------------------------------------\n".format(time.asctime(time.localtime(time.time()))),file=f)
f.close()
