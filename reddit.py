import praw
from db_class import DBclass
from datetime import datetime
import time

reddit = praw.Reddit(
    client_id="tvC9dmt_MPORiuWOXvUY7w",
    client_secret="Ht6U8SouHWDHez-MkIOMHCdWAMXwDg",
    password="xvt192nv2r",
    user_agent="crypto-mentions",
    username="IvashkovMG",
)

subs = ["cryptocurrency", "bitcoin", "btc", "ethereum",
        "ethtrader", "cardano", "monero", "dogecoin"]

def check_reddit():
    reddit_class = DBclass("data.sqlite")
    target_timestamp = reddit_class.db_select_last("reddit_comments")[0][0]
    current_timestamp = datetime.now().replace(second=0, microsecond=0, minute=0).timestamp()
    comments_list = [current_timestamp]

    for sub in subs:
        count = 0
        for comment in reddit.subreddit(sub).comments(limit=None):
            comment_timestamp = int(comment.created_utc)
            count += 1
            if comment_timestamp < target_timestamp:
                break
        comments_list.append(count)
    upload_to_db(reddit_class, target_timestamp, current_timestamp, comments_list)

def upload_to_db(reddit_class, target_timestamp, current_timestamp, comments_list):
    if target_timestamp < current_timestamp:
        print('[Insert]', comments_list)
        reddit_class.db_insert_reddit(tuple(comments_list))
    else:
        comments_list.append(comments_list.pop(comments_list.index(current_timestamp)))
        reddit_class.db_update_reddit(tuple(comments_list))
        print('[Update]', comments_list)

while True:
    check_reddit()
    time.sleep(300)