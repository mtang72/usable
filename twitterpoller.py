import json
import twitter as tw
import time
#The 'twitter' package is the Minimalist Twitter API, courtesy of Mike Verdone.

f = open('out1.txt', 'w')

# Variables that contains the user credentials to access Twitter API 
# For understandable reasons I am not revealing my access token and secret, or my API key and secret.
ACCESS_TOKEN =  
ACCESS_SECRET = 
CONSUMER_KEY =  
CONSUMER_SECRET = 

oauth = tw.OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
tstream = tw.TwitterStream(auth=oauth)

keywords = """data security,data privacy,cybersecurity,digital security,digital privacy,internet privacy,internet security,
computer privacy,surveillance,internet rights,internet censorship,internet monitoring,internet safety,online privacy"""

# Get tweets with specified keywords
iterator = tstream.statuses.filter(track=keywords, language="en")
time_start = time.time()
delaycheck = time.time()
print("\n---------------------------------------------------\nStarted at time: {}\
        \n---------------------------------------------------\n".format(time.asctime(time.localtime(time_start))),file=f)
for tweet in iterator:
    try:
        print(tweet['text'].strip('\n').lstrip('\n'),file=f)
        print("--------------------------------\n{}".format(tweet['user']),file=f)
    except KeyError:
        print("\n---------------------------------------------------\nConnection dropped at time: {}\
            \n---------------------------------------------------\n".format(time.asctime(time.localtime(delaycheck))),file=f)
        exit()
    if time.time() >= time_start+900:
        break
    delaycheck = time.time()

print("\n---------------------------------------------------\nEnded at time: {}\
        \n---------------------------------------------------\n".format(time.asctime(time.localtime(time.time()))),file=f)
f.close()
