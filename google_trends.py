from pytrends.request import TrendReq
from db_class import DBclass
import time

while True:
    pytrends = TrendReq(hl='en-US')

    pytrends.build_payload(["bitcoin"], cat=0, timeframe='now 7-d', geo='', gprop='news')
    df_main = pytrends.interest_over_time()

    others = ["ethereum", "cardano", "solana", "ripple", "polkadot", "dogecoin"]
    for keyword in others:
        pytrends.build_payload([keyword], cat=0, timeframe='now 7-d', geo='', gprop='news')
        df_new = pytrends.interest_over_time()
        trend_list = []
        for index, row in df_new.iterrows():
            trend_list.append(row[keyword])
        df_main[keyword] = trend_list

    google = DBclass("data.sqlite")
    for index, row in df_main.iterrows():
        try:
            google.db_insert_google("google_trends", time=int(index.timestamp()),
                                    bitcoin=row['bitcoin'], ethereum=row['ethereum'],
                                    cardano=row['cardano'], solana=row['solana'],
                                    ripple=row['ripple'], polkadot=row['polkadot'],
                                    dogecoin=row['dogecoin'])
            print("Insert:", int(index.timestamp()))
        except Exception:
            google.db_update_google("google_trends", bitcoin=row['bitcoin'],
                                    ethereum=row['ethereum'], cardano=row['cardano'],
                                    solana=row['solana'], ripple=row['ripple'],
                                    polkadot=row['polkadot'], dogecoin=row['dogecoin'],
                                    time=int(index.timestamp()))
    time.sleep(1800)