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
    twitter_hourly_time, twitter_hourly_data, hourly_price_data, hourly_price_mean, twitter_daily_time, twitter_daily_data, daily_price_data, daily_price_mean = get_tweets(pair, keywords)
    reddit_hourly_time, reddit_hourly_data, reddit_daily_time, reddit_daily_data = get_reddit()
    google_day_time, google_day_data, google_week_time, google_week_data = get_google2()
    google_data = get_google(keys_dict[pair.upper()][2])
    return render_template("index.html", twitter_hourly_time=twitter_hourly_time, twitter_hourly_data=twitter_hourly_data,
                           hourly_price_data=hourly_price_data, hourly_price_mean=hourly_price_mean,
                           reddit_hourly_time=reddit_hourly_time, reddit_hourly_data=reddit_hourly_data,
                           google_data=google_data, twitter_daily_time=twitter_daily_time, twitter_daily_data=twitter_daily_data,
                           reddit_daily_time=reddit_daily_time, reddit_daily_data=reddit_daily_data,
                           google_day_time=google_day_time, google_day_data=google_day_data,
                           google_week_time=google_week_time, google_week_data=google_week_data,
                           daily_price_data=daily_price_data, daily_price_mean=daily_price_mean)


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
    df.loc[:, 'price_mean'] = df['price'].rolling(window=24).mean().shift(-24)
    hourly_price_mean = df['price_mean'].fillna("").tolist()
    df[columns[2]] = df[columns[2]] - df[columns[3]]
    df[columns[4]] = df[columns[4]] - df[columns[5]]
    twitter_hourly_time = df['time'].tolist()
    twitter_hourly_data = [df[i].tolist() for i in columns[2:]]
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df = df.set_index('time').resample('D').agg({'price': 'mean', columns[2]: 'sum', columns[3]: 'sum', columns[4]: 'sum', columns[5]: 'sum'})  # sum()
    print(df.tail())
    daily_price_data = df['price'].tolist()
    df.loc[:, 'price_mean'] = df['price'].rolling(window=7).mean()  # .shift(-7)
    daily_price_mean = df['price_mean'].fillna("").tolist()
    twitter_daily_time = df.index.values.tolist()
    twitter_daily_data = [df[i].tolist() for i in columns[2:]]
    return twitter_hourly_time, twitter_hourly_data, hourly_price_data, hourly_price_mean, twitter_daily_time, twitter_daily_data, daily_price_data, daily_price_mean


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
    df.columns = ["time", "cryptocurrency", "bitcoin", "btc", "ethereum", "ethtrader", "cardano", "monero", "dogecoin"]
    reddit_hourly_time = df['time'].tolist()
    reddit_hourly_data = [df[i].tolist() for i in df.columns[1:]]
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df = df.set_index('time').resample('D').sum()
    reddit_daily_time = df.index.values.tolist()
    reddit_daily_data = [df[i].tolist() for i in df.columns[1:]]
    return reddit_hourly_time, reddit_hourly_data, reddit_daily_time, reddit_daily_data

def get_google2():
    ct = get_from_db("trends_day_bitcoin", None)
    df_day = pd.DataFrame(ct)
    df_day.dropna(inplace=True)
    df_day.columns = ["id", "time", "search", "news", "youtube"]
    google_day_time = df_day['time'].tolist()
    google_day_data = [df_day[i].tolist() for i in df_day.columns[2:]]

    ct = get_from_db("trends_week_bitcoin", None)
    df_week = pd.DataFrame(ct)
    df_week.dropna(inplace=True)
    df_week.columns = ["id", "time", "search", "news", "youtube"]
    google_week_time = df_week['time'].tolist()
    google_week_data = [df_week[i].tolist() for i in df_week.columns[2:]]

    return google_day_time, google_day_data, google_week_time, google_week_data

def get_google3():
    ct = get_from_db("trends_day_bitcoin", None)
    df_day = pd.DataFrame(ct)
    df_day.dropna(inplace=True)
    df_day.columns = ["id", "time", "search", "news", "youtube"]
    df_day['time'] = pd.to_datetime(df_day['time'], unit='s')
    df_day = df_day.set_index('time').resample('H').sum()
    google_day_time = df_day.index.values.tolist()
    google_day_data = [df_day[i].tolist() for i in df_day.columns[1:]]

    ct = get_from_db("trends_week_bitcoin", None)
    df_week = pd.DataFrame(ct)
    df_week.dropna(inplace=True)
    df_week.columns = ["id", "time", "search", "news", "youtube"]
    df_week['time'] = pd.to_datetime(df_week['time'], unit='s')
    df_week = df_week.set_index('time').resample('D').sum()
    google_week_time = df_week.index.values.tolist()
    google_week_data = [df_week[i].tolist() for i in df_week.columns[1:]]

    return google_day_time, google_day_data, google_week_time, google_week_data

if __name__ == '__main__':
    app.run(threaded=True)
