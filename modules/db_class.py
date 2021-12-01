import sqlite3

class DBclass():
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()

    def db_insert(self, table_name, **kwargs):
        placeholders = ','.join('?' for i in kwargs.values())
        query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        self.cur.execute(query, tuple(kwargs.values()))
        self.conn.commit()

    def db_insert_google(self, table_name, **kwargs):
        placeholders = ','.join('?' for i in kwargs.values())
        query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        self.cur.execute(query, tuple(kwargs.values()))
        self.conn.commit()

    def db_update_google(self, table_name, **kwargs):
        query = f"UPDATE {table_name} SET bitcoin=:bitcoin, ethereum=:ethereum, cardano=:cardano, solana=:solana, ripple=:ripple, polkadot=:polkadot, dogecoin=:dogecoin WHERE time=:time"
        self.cur.execute(query, tuple(kwargs.values()))
        self.conn.commit()

    def db_insert_twitter(self, table_name, column_name, **kwargs):
        query = f"INSERT INTO {table_name} (time, price, {column_name}) VALUES (:time, :price, :count)"
        print("Insert:", table_name, column_name, kwargs["time"], kwargs["price"], kwargs["count"])
        self.cur.execute(query, tuple(kwargs.values()))
        self.conn.commit()

    def db_update_twitter(self, table_name, column_name, **kwargs):
        query = f"UPDATE {table_name} SET {column_name} = :count, price = :price WHERE time = :time"
        print("Update:", table_name, column_name, kwargs["time"], kwargs["price"], kwargs["count"])
        self.cur.execute(query, (kwargs["count"], kwargs["price"], kwargs["time"]))
        self.conn.commit()

    def db_insert_reddit(self, comments):
        query = f"INSERT INTO reddit_comments VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        self.cur.execute(query, comments)
        self.conn.commit()

    def db_update_reddit(self, comments):
        query = f"UPDATE reddit_comments SET cryptocurrency = ?, bitcoin = ?," \
                f"btc = ?, ethereum = ?, ethtrader = ?, cardano = ?, monero =?," \
                f"dogecoin = ? WHERE time = ?"
        self.cur.execute(query, comments)
        self.conn.commit()

    def db_select_last(self, table_name):
        query = f"SELECT * FROM {table_name} " \
                f"ORDER BY time DESC LIMIT 1"
        self.cur.execute(query)
        data = self.cur.fetchall()
        return data

    def __del__(self):
        self.cur.close()
        self.conn.close()
