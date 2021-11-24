import json
import dateutil.parser as dp
from db_class import DBclass
from twitter import get_tweets
from binance import get_price
from datetime import datetime
import time

with open('pairs.json') as json_file:
    PAIRS_DICT = json.load(json_file)

def main():
    while True:
        for pair in PAIRS_DICT:
            pair_price = get_price(pair)
            twitter_count(pair, pair_price)
        time.sleep(600)

def parse_tweet_data(tweet_data):
    tweet_count = int(tweet_data['tweet_count'])
    tweet_time_iso = tweet_data['start']
    tweet_time_ut = int(dp.parse(tweet_time_iso).timestamp())
    return tweet_time_ut, tweet_count

def twitter_count(pair, pair_price):
    for index, keyword in enumerate(PAIRS_DICT[pair]):
        twitter = DBclass("data.sqlite")
        start_time_ut = twitter.db_select_last(pair)[0][0]
        start_time_iso = datetime.utcfromtimestamp(start_time_ut).isoformat()+"Z"
        tweet_data = get_tweets(start_time_iso, keyword)
        column = keyword.replace('#', 'q_h') if '#' in keyword else keyword.replace(keyword, 'q_' + keyword)
        if len(tweet_data) > 1 and index == 0:
            tweet_time_ut, tweet_count = parse_tweet_data(tweet_data[1])
            twitter.db_insert_twitter(pair, column, time=tweet_time_ut, price=pair_price, count=tweet_count)
        else:
            tweet_time_ut, tweet_count = parse_tweet_data(tweet_data[0])
            twitter.db_update_twitter(pair, column, time=tweet_time_ut, price=pair_price, count=tweet_count)

if __name__ == '__main__':
    main()
