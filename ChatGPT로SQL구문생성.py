import sqlite3
import random
import string

class ElectronicsDatabase:
    def __init__(self, db_name='electronics.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()
    
    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS electronics (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    price REAL NOT NULL
                )
            ''')

    def insert_product(self, name, price):
        with self.conn:
            self.conn.execute('''
                INSERT INTO electronics (name, price) VALUES (?, ?)
            ''', (name, price))
    
    def update_product(self, product_id, name, price):
        with self.conn:
            self.conn.execute('''
                UPDATE electronics
                SET name = ?, price = ?
                WHERE id = ?
            ''', (name, price, product_id))
    
    def delete_product(self, product_id):
        with self.conn:
            self.conn.execute('''
                DELETE FROM electronics
                WHERE id = ?
            ''', (product_id,))
    
    def select_all_products(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT * FROM electronics
        ''')
        return cursor.fetchall()

    def select_product(self, product_id):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT * FROM electronics
            WHERE id = ?
        ''', (product_id,))
        return cursor.fetchone()

# 샘플 데이터 생성 함수
def generate_sample_data(num_samples=100):
    sample_data = []
    for _ in range(num_samples):
        name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        price = round(random.uniform(100.0, 2000.0), 2)
        sample_data.append((name, price))
    return sample_data

# 샘플 데이터를 데이터베이스에 삽입
def insert_sample_data(db, sample_data):
    for name, price in sample_data:
        db.insert_product(name, price)

# 메인 실행 코드
if __name__ == '__main__':
    db = ElectronicsDatabase()
    
    # 샘플 데이터 생성
    sample_data = generate_sample_data(100)
    
    # 샘플 데이터 삽입
    insert_sample_data(db, sample_data)
    
    # 모든 제품 출력
    products = db.select_all_products()
    for product in products:
        print(product)
