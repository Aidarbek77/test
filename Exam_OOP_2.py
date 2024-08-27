import sqlite3

def create_conn(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print("Error making connection", e)
    return conn

def create_table(conn, create_table_sql):
    try:
        cursor = conn.cursor()
        conn.execute(create_table_sql)
        conn.commit()
    except sqlite3.Error as e:
        print("Error making connection", e)



def create_store(cursor):
    try:
        cursor.execute('''
        INSERT INTO store (categories, products, store),
        id PRIMARY KEY AUTOINCREMENT, 
        ''')
    except  sqlite3.Error as e:
        print(e)

def add_categories(cursor):
    try:
        cursor.execute('''
        INSERT INTO categories, 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code (varchar(2)),
        title (varchar(150)),''')
    except sqlite3.Error as e:
        print(e)

def add_products(cursor):
    try:
        cursor.execute('''
        INSERT INTO products,
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title(varcar(250)), 
        category_code (varchar(2)),
        unit_price(FLOAT), 
        stock_quantity (INTEGER), 
        store_id (INTEGER)''')
    except sqlite3.Error as e:
        print(e)

def add_store(cursor):
    try:
        cursor.execute('''
        INSERT INTO store, 
        store_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        title(VARCHAR(100))
        ''')
    except: pass

def view_products(cursor,category_code):
    try:
        cursor.execute('''
        SELECT * FROM products
        where category_code = ?''') (category_code)
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(e)

def identify_store(cursor,store_id):
    try:
        cursor.execute('''
        SELECT * FROM store, 
        where store_id = ?''') (store_id)
    except sqlite3.Error as e:
        print(e)


def main():
    db_name = "hw.db"

    sql_table_products = '''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT(200) NOT NULL,
        unit_price (FLOAT) NOT NULL,
        stock_quantity (INTEGER) NOT NULL,
        store_id (INTEGER) NOT NULL
    )
    '''

    conn = create_conn(db_name)
    if conn is not None:
        print("Connected to database")
        create_table(conn, create_table_sql=True)

        cursor = conn.cursor()
        add_products(cursor, "chocolate", "FD", 10.5, 129, 1)
        add_products(cursor, "Jeans", "CL", 67,55 ,2 )
        add_products(cursor, "mango", "FD", 50, 13,2 )
        add_products(cursor, "orange", "CL",40, 89 ,1)
        add_products(cursor, "strawberry","FD", 90, 76,1)
        add_products(cursor, "pineapple", "FD",185, 100,3)
        add_products(cursor, "dragon fruit", "FD",250, 30,3)
        add_products(cursor, "plum", "CL", 160, 90,3)
        add_products(cursor, "cherry", "CL", 78, 99,2)
        add_products(cursor, "watermelon", "FD",78, 60,2)
        add_products(cursor, "grapes", "FD",70, 80,1)
        add_products(cursor, "lemon", "FD",50, 100,1)
        add_products(cursor, "kiwi","CL", 89, 78,1)
        add_products(cursor, "pear", "FD",45, 67,1)
        add_products(cursor, "apricot", "CL",30, 37,3)

        conn.commit()
        conn.close()
    else:
        print("Error connecting to database")


if __name__ == "__main__":
    main()

print("Вы можете отобразить список продуктов по выбранному id магазина изперечня магазинов ниже, для выхода из программы введите цифру 0 ")
print(add_store())
print