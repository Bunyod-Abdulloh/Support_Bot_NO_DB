import sqlite3

path_to_db= 'data/main.db'

def create_table():
    conn= sqlite3.connect(path_to_db)
    cur= conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS quran_oyatlar(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    level INTEGER,
    audio VARCHAR(100),
    url TEXT)""")
    conn.commit()
    
    cur.execute("""CREATE TABLE IF NOT EXISTS quran_suralar(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    page INTEGER,
   audio VARCHAR(100),
    url TEXT)""")
    conn.commit()
    
    conn.close()

def get_quran_oyatlar(sahifa):
    conn= sqlite3.connect(path_to_db)
    cur= conn.cursor()
    cur.execute(f"SELECT * FROM quran_oyatlar WHERE level={sahifa}")
    result= cur.fetchall()
    conn.close()
    return result
    
def get_quran_suralar(page):
    conn= sqlite3.connect(path_to_db)
    cur= conn.cursor()
    cur.execute(f"SELECT * FROM quran_suralar WHERE page={page}")
    result= cur.fetchall()
    conn.close()
    return result