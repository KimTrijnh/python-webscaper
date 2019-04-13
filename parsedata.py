import json


# for tweet in json.loads(tweetsJs.read()):
#     if 'obama' in tweet['content'].lower():
#         print(tweet['content'])

def search(keyword):
    tweetsJs = open('tweets.json', 'r')
    tweets = json.loads(tweetsJs.read())
    count = 0
    for t in tweets:
        if keyword.lower() in t['content'].lower():
            count = count + 1
    print('tweet contain', keyword, ':', count)


search('obama') 
