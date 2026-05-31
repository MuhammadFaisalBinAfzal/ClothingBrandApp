import pyodbc
from datetime import datetime

class Database:
    def __init__(self):
        # --- CONFIGURATION ---
        # PASTE YOUR SERVER NAME FROM STEP 1 BELOW inside the quotes
        SERVER = r'M-FAISAL\SQLEXPRESS'
        DATABASE = 'BrandManagerDB'
        
        # This connection string connects Python to SQL Server
        self.conn_string = (
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={SERVER};'
            f'DATABASE={DATABASE};'
            f'Trusted_Connection=yes;'
        )
        
        try:
            self.conn = pyodbc.connect(self.conn_string)
            self.cursor = self.conn.cursor()
            print("Successfully connected to SQL Server!")
        except Exception as e:
            print("Error connecting to database:", e)
            print("Make sure your Server Name is correct and SQL Server is running.")

    # --- PRODUCT METHODS ---
    def add_product(self, name, category, cost, price, stock):
        self.cursor.execute("INSERT INTO products (name, category, cost_price, selling_price, stock) VALUES (?, ?, ?, ?, ?)",
                            (name, category, cost, price, stock))
        self.conn.commit()

    def get_all_products(self):
        self.cursor.execute("SELECT * FROM products")
        return self.cursor.fetchall()

    def add_category(self, category_name):
        try:
            self.cursor.execute("INSERT INTO categories (name) VALUES (?)", (category_name,))
            self.conn.commit()
            return True
        except Exception:
            return False

    def get_all_categories(self):
        self.cursor.execute("SELECT name FROM categories ORDER BY name ASC")
        return [row[0] for row in self.cursor.fetchall()]

    def update_stock(self, product_id, new_stock):
        self.cursor.execute("UPDATE products SET stock = ? WHERE id = ?", (new_stock, product_id))
        self.conn.commit()

    # --- SALES METHODS ---
    def add_sale(self, product_id, product_name, qty, total, profit):
        # SQL Server uses datetime objects directly
        self.cursor.execute("INSERT INTO sales (product_id, product_name, quantity, total_amount, profit, date) VALUES (?, ?, ?, ?, ?, ?)",
                            (product_id, product_name, qty, total, profit, datetime.now()))
        self.conn.commit()

    def get_total_sales(self):
        self.cursor.execute("SELECT SUM(total_amount) FROM sales")
        result = self.cursor.fetchone()[0]
        return result if result else 0.0

    def get_total_profit(self):
        self.cursor.execute("SELECT SUM(profit) FROM sales")
        result = self.cursor.fetchone()[0]
        return result if result else 0.0
    
    def get_daily_sales_data(self):
        # CHANGED: Syntax for SQL Server dates
        self.cursor.execute("SELECT CAST(date AS DATE), SUM(total_amount) FROM sales GROUP BY CAST(date AS DATE) ORDER BY CAST(date AS DATE) DESC")
        # Python will handle the limit of 7 items if you need it in your graph code, 
        # or we can use "SELECT TOP 7..." if strictly needed.
        return self.cursor.fetchall()

    def get_all_sales(self, limit=0):
        # CHANGED: SQL Server uses "TOP" instead of "LIMIT"
        if limit and isinstance(limit, int) and limit > 0:
            query = f"SELECT TOP {limit} id, product_id, product_name, quantity, total_amount, profit, date FROM sales ORDER BY date DESC"
            self.cursor.execute(query)
        else:
            self.cursor.execute("SELECT id, product_id, product_name, quantity, total_amount, profit, date FROM sales ORDER BY date DESC")
        return self.cursor.fetchall()

    def get_sales_sum_between(self, start_date, end_date):
        # CHANGED: CAST(date AS DATE) for SQL Server
        self.cursor.execute("SELECT SUM(total_amount) FROM sales WHERE CAST(date AS DATE) BETWEEN CAST(? AS DATE) AND CAST(? AS DATE)", (str(start_date), str(end_date)))
        result = self.cursor.fetchone()[0]
        return result if result else 0.0

    def get_expenses_sum_between(self, start_date, end_date):
        self.cursor.execute("SELECT SUM(amount) FROM expenses WHERE CAST(date AS DATE) BETWEEN CAST(? AS DATE) AND CAST(? AS DATE)", (str(start_date), str(end_date)))
        result = self.cursor.fetchone()[0]
        return result if result else 0.0

    def get_sales_between(self, start_date, end_date):
        self.cursor.execute("SELECT id, product_id, product_name, quantity, total_amount, profit, date FROM sales WHERE CAST(date AS DATE) BETWEEN CAST(? AS DATE) AND CAST(? AS DATE) ORDER BY date DESC", (str(start_date), str(end_date)))
        return self.cursor.fetchall()

    def get_expenses_between(self, start_date, end_date):
        self.cursor.execute("SELECT id, date, title, category, amount, notes FROM expenses WHERE CAST(date AS DATE) BETWEEN CAST(? AS DATE) AND CAST(? AS DATE) ORDER BY date DESC", (str(start_date), str(end_date)))
        return self.cursor.fetchall()

    # --- EXPENSE METHODS ---
    def add_expense(self, title, category, amount, date=None, notes=None):
        if date is None:
            date = datetime.now()
        self.cursor.execute("INSERT INTO expenses (title, category, amount, date, notes) VALUES (?, ?, ?, ?, ?)",
                            (title, category, amount, date, notes))
        self.conn.commit()

    def get_all_expenses(self, limit=0):
        # CHANGED: SQL Server uses "TOP" instead of "LIMIT"
        if limit and isinstance(limit, int) and limit > 0:
            query = f"SELECT TOP {limit} id, date, title, category, amount, notes FROM expenses ORDER BY date DESC"
            self.cursor.execute(query)
        else:
            self.cursor.execute("SELECT id, date, title, category, amount, notes FROM expenses ORDER BY date DESC")
        return self.cursor.fetchall()

    def get_total_expenses(self):
        self.cursor.execute("SELECT SUM(amount) FROM expenses")
        result = self.cursor.fetchone()[0]
        return result if result else 0.0

    def clear_all_data(self):
        try:
            # Delete data from tables
            self.cursor.execute("DELETE FROM products")
            self.cursor.execute("DELETE FROM sales")
            self.cursor.execute("DELETE FROM expenses")
            self.cursor.execute("DELETE FROM categories")
            
            # Reset Identity (Auto Increment) in SQL Server
            self.cursor.execute("DBCC CHECKIDENT ('products', RESEED, 0)")
            self.cursor.execute("DBCC CHECKIDENT ('sales', RESEED, 0)")
            self.cursor.execute("DBCC CHECKIDENT ('expenses', RESEED, 0)")
            self.cursor.execute("DBCC CHECKIDENT ('categories', RESEED, 0)")
            
            self.conn.commit()
            return True
        except Exception:
            return False