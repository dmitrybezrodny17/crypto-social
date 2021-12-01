import requests
from settings import TOKEN


def bearer_oauth(r):
    r.headers[
        "Authorization"] = f"Bearer {TOKEN}"
    r.headers["User-Agent"] = "v2RecentTweetCountsPython"
    return r

def get_tweets(start_time, query):
    response = requests.request("GET", "https://api.twitter.com/2/tweets/counts/recent",
                                auth=bearer_oauth,
                                params={'query': query, 'granularity': 'hour', 'start_time': start_time})

    return response.json()['data']
