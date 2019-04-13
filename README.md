## PROJECT FOR BACKEND PRACTICE: WEB SCRAPER


- tweets table displayed: (for 10 first tweets)
![alt text](https://ibb.co/0hWH0S0 "tweets table")

## DESCRIPTION:
![alt text](https://cdn-images-1.medium.com/max/1000/1*hYfIYxGbmEqa0wKqz5HXRA.png "webscaper")

## USER STORY
- [x] loading html from this fake tweeter http://ethans_fake_twitter_site.surge.sh/
- [x] All tweets in raw html can printed in the terminal using python
- [x] Store each tweet in a Jsonformat dict and all tweet objects are stored in an array(list in python)
- [x] the data is saved as JSON file
- [x] count the number of tweet that have 'obama' inside its' content
- [x] Create tweets table in sql that have collum id, author, content, like, share, date

## WHAT I LEARN
- [x] create a virtual environment `python -m venv env`
        ** Little diference from the ref tutorial: **
        ```=python
        #to activate virtual env
        cd evn
        ./Scripts/activate
        ```
- [x] File handling in python
- [x] Working with Json data in python


### Libaries used in this project:
1. Beautiful Soup `pip install bs4`
Beautiful Soup contains some easy ways for us to identify the tags 
2. Request `pip install requests`
The Request library allows us to make requests to urls, and access the data on those HTML pages. 
### ref: https://hackernoon.com/building-a-web-scraper-from-start-to-finish-bb6b95388184

