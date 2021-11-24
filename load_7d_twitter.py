import requests
from db_class import DBclass
import json
import dateutil.parser as dp

with open('pairs.json') as json_file:
    PAIRS_DICT = json.load(json_file)

TOKEN = "AAAAAAAAAAAAAAAAAAAAALofUgEAAAAAQKqm4w1f%2FQ3gEdq2QcYvO4oF3xQ%3DthLM0LF4jNuuzFy8GF9yE7AcmhTgk90v1ZEMRdD4vRHXcHCjxS"

def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {TOKEN}"
    r.headers["User-Agent"] = "v2RecentTweetCountsPython"
    return r

def get_tweets(query):
    response = requests.request("GET", "https://api.twitter.com/2/tweets/counts/recent",
                                auth=bearer_oauth,
                                params={'query': query, 'granularity': 'hour'})

    return response.json()['data']

def parse_tweet_data(tweet_data):
    tweet_count = int(tweet_data['tweet_count'])
    tweet_time_iso = tweet_data['start']
    tweet_time_ut = int(dp.parse(tweet_time_iso).timestamp())
    return tweet_time_ut, tweet_count

def main():
    pair = input("Type pair in UPPER case: ")
    for index, keyword in enumerate(PAIRS_DICT[pair]):
        twitter = DBclass("data.sqlite")
        column = keyword.replace('#', 'q_h') if '#' in keyword else keyword.replace(keyword, 'q_' + keyword)
        tweet_data = get_tweets(keyword)
        for i in tweet_data:
            if index == 5:
                tweet_time_ut, tweet_count = parse_tweet_data(i)
                twitter.db_insert_twitter(pair, column, time=tweet_time_ut, count=tweet_count)
                print("Insert: ", pair, column, tweet_time_ut, tweet_count)
            else:
                tweet_time_ut, tweet_count = parse_tweet_data(i)
                twitter.db_update_twitter(pair, column, time=tweet_time_ut, count=tweet_count)
                print("Update: ", pair, column, tweet_time_ut, tweet_count)

if __name__ == '__main__':
    main()