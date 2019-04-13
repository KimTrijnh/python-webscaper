import os
import sqlite3
import json

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')

#connect to dababase
def db_connect(db_path=DEFAULT_PATH):
    con = sqlite3.connect(db_path)
    return con

def create_tweets():
    con = db_connect()
    cur = con.cursor()
    sql="""
    CREATE TABLE tweets(
        id INTEGER PRIMARY KEY,
        author TEXT NOT NULL,
        content TEXT NOT NULL,
        date TEXT,
        likes INTEGER,
        shares INTEGER
    )
    """
    cur.execute(sql)
    con.close()
    print('tweets created')

def add_tweet(author, content, date, likes, shares):
    con = db_connect()
    cur = con.cursor()
    sql="""
    INSERT INTO tweets(author, content, date, likes, shares)
    VALUES (?,?,?,?,?)
    """
    cur.execute(sql, (author, content, date, likes, shares))
    con.commit()
    con.close()


def print_tweets():
    con = db_connect()
    cur = con.cursor()
    sql="""
    SELECT * FROM tweets
    """
    cur.execute(sql)
    result = cur.fetchall()
    for i in result:
        print(i)
    con.close()

def add_tweets(num):
    tweetsJs = open('tweets.json', 'r')
    tweets = json.loads(tweetsJs.read())[0:num]
    for t in tweets:
        author, content, date, likes, shares = t['author'], t['content'], t['date'].split()[0], int(t['likes'].split()[1]), int(t['shares'].split()[1])
        add_tweet(author, content, date, likes, shares)
        print('tweet added to db')
    print(num, 'tweets added to db')

#add 10 first tweets to table tweets
#add_tweets(10)


def clear_rows():
    con = db_connect()
    cur = con.cursor()
    sql="""
    DELETE FROM tweets
    """
    cur.execute(sql)
    con.commit()
    con.close()
    print('all tweets are deleted from table tweets')

