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

    def add_good(self, naming: str, price: float, category: str) -> None:
        connection = connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute('''
        INSERT INTO Goods 
        (naming, price, category) VALUES (?, ?, ?)
        ''',
                       (naming, price, category)
                       )
        connection.commit()
        connection.close()

    def del_good(self, id: int) -> None:
        connection = connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute('''
        DELETE FROM Goods 
        WHERE id = ?
        ''',
                       id
                       )
        connection.commit()
        connection.close()

    def update_good(self, id: int, naming: str, price: float, category: str) -> None:
        connection = connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute('''
        UPDATE Goods SET 
        naming = ?,
        price = ?,
        category = ?
        WHERE id = ?
        ''',
                       (naming, price, category, id)
                       )
        connection.commit()
        connection.close()
