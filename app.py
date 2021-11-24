from flask import Flask, render_template
import sqlite3
import pandas as pd
import json

app = Flask(__name__, template_folder='templates')


@app.route("/<pair>")
def index(pair):
    with open('pairs.json') as json_file:
        keys_dict = json.load(json_file)
    keywords = keys_dict[pair.upper()]
    twitter_hourly_time, twitter_hourly_data, hourly_price_data, twitter_daily_time, twitter_daily_data = get_tweets(pair, keywords)
    reddit_hourly_time, reddit_hourly_data, reddit_daily_time, reddit_daily_data = get_reddit()
    google_data = get_google(keys_dict[pair.upper()][2])
    return render_template("index.html", twitter_hourly_time=twitter_hourly_time, twitter_hourly_data=twitter_hourly_data,
                           hourly_price_data=hourly_price_data, reddit_hourly_time=reddit_hourly_time, reddit_hourly_data=reddit_hourly_data,
                           google_data=google_data, twitter_daily_time=twitter_daily_time, twitter_daily_data=twitter_daily_data,
                           reddit_daily_time=reddit_daily_time, reddit_daily_data=reddit_daily_data)


def db_tweets(pair):
    conn = sqlite3.connect('data.sqlite')
    cur = conn.cursor()
    cur.execute(f"SELECT * from '{pair}' ORDER BY time DESC")
    ct = cur.fetchall()
    cur.close()
    conn.close()
    return ct


def get_tweets(pair, keywords):
    ct = db_tweets(pair)
    df = pd.DataFrame(ct)
    columns = ['time', 'price']
    for keyword in keywords:
        columns.append(keyword.replace('#', 'q_h') if '#' in keyword else keyword.replace(keyword, 'q_' + keyword))
    df.columns = columns
    hourly_price_data = df['price'].tolist()
    df[columns[2]] = df[columns[2]] - df[columns[3]]
    df[columns[4]] = df[columns[4]] - df[columns[5]]
    twitter_hourly_time = df['time'].tolist()
    twitter_hourly_data = [df[i].tolist() for i in columns[2:]]
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df = df.set_index('time').resample('D').sum()
    twitter_daily_time = df.index.values.tolist()
    twitter_daily_data = [df[i].tolist() for i in columns[2:]]
    return twitter_hourly_time, twitter_hourly_data, hourly_price_data, twitter_daily_time, twitter_daily_data


def get_from_db(table, column):
    conn = sqlite3.connect('data.sqlite')
    cur = conn.cursor()
    if column:
        cur.execute(f"SELECT time, {column} from {table}")
    else:
        query = f"SELECT * from {table}"
        cur.execute(query)
    ct = cur.fetchall()
    cur.close()
    conn.close()
    return ct

def get_google(pair):
    ct = get_from_db("google_trends", pair)
    df = pd.DataFrame(ct)
    # for i in df.columns:
    #    df[i] = df[i].rolling(window=48).mean().shift(-48)
    df.dropna(inplace=True)
    columns = ["time", pair]
    google_json = [dict(zip(columns, i)) for i in ct]
    return google_json

def get_reddit():
    ct = get_from_db("reddit_comments", None)
    df = pd.DataFrame(ct)
    df.dropna(inplace=True)
    columns = ["time", "cryptocurrency", "bitcoin", "btc", "ethereum", "ethtrader", "cardano", "monero", "dogecoin"]
    df.columns = columns
    reddit_hourly_time = df['time'].tolist()
    reddit_hourly_data = [df[i].tolist() for i in columns[1:]]
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df = df.set_index('time').resample('D').sum()
    reddit_daily_time = df.index.values.tolist()
    reddit_daily_data = [df[i].tolist() for i in columns[1:]]
    return reddit_hourly_time, reddit_hourly_data, reddit_daily_time, reddit_daily_data


if __name__ == '__main__':
    app.run(threaded=True)
