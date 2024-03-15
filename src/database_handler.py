from sqlite3 import connect
from src.constants import ROOT_DIR, DATABASE_NAME
from typing import List


class DatabaseHandler:
    def __init__(self):
        super().__init__()
        self.db_path = ROOT_DIR.joinpath(DATABASE_NAME)

    def create_database(self) -> None:
        connection = connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Goods (
        id INTEGER PRIMARY KEY,
        naming TEXT NOT NULL,
        price REAL NOT NULL,
        category TEXT NOT NULL
        )
        ''')
        connection.commit()
        connection.close()

    def get_goods_list(self) -> List:
        connection = connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute('''
        SELECT * FROM Goods
        ''')
        goods_list = cursor.fetchall()
        connection.commit()
        connection.close()
        return goods_list
