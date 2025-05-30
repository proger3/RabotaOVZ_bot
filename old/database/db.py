import sqlite3

def init_db():
    conn = sqlite3.connect('database/vacancies.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS vacancies
                      (id TEXT PRIMARY KEY, title TEXT, company TEXT, url TEXT)''')
    conn.commit()
    conn.close()
