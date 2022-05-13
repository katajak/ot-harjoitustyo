import sqlite3
from sqlite3 import Error

def create_connection():
    try:
        connection = sqlite3.connect("statistics.db")

    except Error:
        print(Error)

    return connection

def create_table(connection):
    try:
        c = connection.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS stats (id INTEGER PRIMARY KEY,
                  players INTEGER, endless BOOLEAN, p1_score INTEGER, p2_score INTEGER,
                  max_rally INTEGER)""")
                  
    except Error:
        print(Error)

def insert_data(connection, players, endless, score, max_rally):
    try:
        stats = (players, endless, score[0], score[1], max_rally)
        sql = ("""INSERT INTO stats (players, endless, p1_score, p2_score, max_rally)
               VALUES (?,?,?,?,?)""")
        c = connection.cursor()
        c.execute(sql, stats)
        connection.commit()

        connection.close()

    except Error:
        print(Error)
