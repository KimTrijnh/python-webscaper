from bs4 import BeautifulSoup
import requests
import json


url = 'http://ethans_fake_twitter_site.surge.sh/'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, 'html.parser')

# for tweet in content.findAll('p', attrs={"class": "content"}):
#     print(tweet.text)

tweet = {'author': 'jim',
'content': 'text',
'date': '2019-2-3',
'like': 2,
'share': 4}


tweetArr= []
for tweet in content.findAll('div', attrs={'class': 'tweetcontainer'}):
    tweetObj = {
        'author': tweet.find('h2', attrs={'class': 'author'}).text,
        'date': tweet.find('h5', attrs={'class': 'dateTime'}).text,
        'content': tweet.find('p', attrs={'class': 'content'}).text,
        'likes': tweet.find('p', attrs={'class': 'likes'}).text,
        'shares': tweet.find('p', attrs={'class': 'shares'}).text
            }
    tweetArr.append(tweetObj)   

f = open('tweets.json','w')
json.dump(tweetArr, f)
f.close()

# f= open('tweets.json', 'r')
# print(f.read())

# with open("data_file.json", "w") as write_file:
#     json.dump(tweetArr, write_file)

