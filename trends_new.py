import sqlite3
from pytrends.request import TrendReq
from datetime import datetime

def update_db(table, column, count, time, id):
    conn = sqlite3.connect('data.sqlite')
    cur = conn.cursor()
    query = f"UPDATE {table} SET {column}=:count, time=:time WHERE id=:id"
    cur.execute(query, (count, time, id))
    conn.commit()
    cur.close()
    conn.close()

pytrends = TrendReq(hl='en-US')

pytrends.build_payload(["bitcoin"], cat=0, timeframe='now 7-d', geo='', gprop='')
df_search = pytrends.interest_over_time()
pytrends.build_payload(["bitcoin"], cat=0, timeframe='now 7-d', geo='', gprop='news')
df_news = pytrends.interest_over_time()
pytrends.build_payload(["bitcoin"], cat=0, timeframe='now 7-d', geo='', gprop='youtube')
df_youtube = pytrends.interest_over_time()

id_count = 0
for index, row in df_search.iterrows():
    id_count += 1
    update_db("trends_week_bitcoin", "search", row["bitcoin"], datetime.timestamp(index), id_count)

id_count = 0
for index, row in df_news.iterrows():
    id_count += 1
    update_db("trends_week_bitcoin", "news", row["bitcoin"], datetime.timestamp(index), id_count)

id_count = 0
for index, row in df_youtube.iterrows():
    id_count += 1
    update_db("trends_week_bitcoin", "youtube", row["bitcoin"], datetime.timestamp(index), id_count)

'''
pytrends.build_payload(["bitcoin"], cat=0, timeframe='now 1-d', geo='', gprop='news')
df_news = pytrends.interest_over_time()
pytrends.build_payload(["bitcoin"], cat=0, timeframe='now 1-d', geo='', gprop='youtube')
df_youtube = pytrends.interest_over_time()


id_count = 0
for index, row in df_search.iterrows():
    id_count += 1
    update_db("search", row["bitcoin"], datetime.timestamp(index), id_count)

id_count = 0
for index, row in df_news.iterrows():
    id_count += 1
    update_db("news", row["bitcoin"], datetime.timestamp(index), id_count)

id_count = 0
for index, row in df_youtube.iterrows():
    id_count += 1
    update_db("youtube", row["bitcoin"], datetime.timestamp(index), id_count)
'''
