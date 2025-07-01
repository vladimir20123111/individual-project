import sqlite3
from config import DATABASE


class DB_Manager:
    def __init__(self, database):
        self.database = database
    
    def create_tables(self):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute('''
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER NOT NULL,
                name TEXT,
                info TEXT,
            )
        ''')
        conn.commit()
    
    def get_data(start_date, end_date):
        con = sqlite3.connect('data.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM data WHERE date BETWEEN ? AND ? ORDER BY date ", (start_date, end_date))
        res = cur.fetchall()
        con.close()
        dates = [res[i][0] for i in range(len(res))]
        prices = [res[i][1] for i in range(len(res))]
        return dates, prices
    

    
if __name__ == '__main__':
    manager = DB_Manager(DATABASE)
    manager.create_tables()

