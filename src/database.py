import sqlite3
from sqlite3 import Error

def create_connection():
    try:
        connection = sqlite3.connect("statistics.db")

    except Error:
        print(Error)

    return connection

def close_connection(connection):
    connection.close()

def create_table(connection):
    try:
        cur = connection.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS stats (id INTEGER PRIMARY KEY,
                  players INTEGER, difficulty TEXT, p1_score INTEGER, p2_score INTEGER,
                  max_rally INTEGER)""")

    except Error:
        print(Error)

def insert_data(connection, players, difficulty, score, max_rally):
    try:
        if players == 2:
            difficulty = "-"
        stats = (players, difficulty, score[0], score[1], max_rally)
        sql = ("""INSERT INTO stats (players, difficulty, p1_score, p2_score, max_rally)
               VALUES (?,?,?,?,?)""")
        cur = connection.cursor()
        cur.execute(sql, stats)
        connection.commit()

    except Error:
        print(Error)

def games_played(connection):
    sql = "SELECT COALESCE(COUNT(id), 0) FROM stats"
    cur = connection.cursor()
    cur.execute(sql)
    return cur.fetchone()[0]

def max_rally_ever(connection):
    sql = "SELECT COALESCE(MAX(max_rally), 0) FROM stats"
    cur = connection.cursor()
    cur.execute(sql)
    return cur.fetchone()[0]

def last_game(connection):
    sql = "SELECT p1_score, p2_score FROM stats ORDER BY id DESC"
    cur = connection.cursor()
    cur.execute(sql)
    res = cur.fetchone()
    if res is None:
        res = [0, 0]
    return res
