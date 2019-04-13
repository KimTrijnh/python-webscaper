## PROJECT FOR BACKEND PRACTICE: WEB SCRAPER

Web Scraper is a process of loading html from a site and convert sepcified information into data. This project is done using a fake twitter site based on [this tutorial](https://hackernoon.com/building-a-web-scraper-from-start-to-finish-bb6b95388184). I write the user story my own and also added more in order to practice implementing python and sql.


final sql table would look like this:
- tweets table displayed: (for 10 first tweets)
!["tweets table" ](https://i.ibb.co/4K8drNn/image.png)


## DESCRIPTION:
![alt text](https://cdn-images-1.medium.com/max/1000/1*hYfIYxGbmEqa0wKqz5HXRA.png "webscaper")

## USER STORY
- [x] loading html from this fake tweeter http://ethans_fake_twitter_site.surge.sh/
- [x] All tweets in raw html can printed in the terminal using python
- [x] Store each tweet in a Jsonformat dict and all tweet objects are stored in an array(list in python)
- [x] the data is saved as JSON file
- [x] count the number of tweet that have 'obama' inside its' content
- [x] Create tweets table in sql that have collum id, author, content, like, share, date
- [x] add 10 tweets to the table

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



