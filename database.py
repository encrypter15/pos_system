import sqlite3

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """Create the inventory table if it doesn't exist."""
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS inventory (
                    item_id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    price REAL NOT NULL,
                    stock INTEGER NOT NULL
                )
            """)
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS transactions (
                    transaction_id TEXT PRIMARY KEY,
                    amount REAL NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)

    def add_item(self, item_id, name, price, stock):
        """Add or update an item in the inventory table."""
        with self.conn:
            self.conn.execute("""
                INSERT OR REPLACE INTO inventory (item_id, name, price, stock)
                VALUES (?, ?, ?, ?)
            """, (item_id, name, price, stock))

    def get_all_items(self):
        """Retrieve all items from the inventory table."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT item_id, name, price, stock FROM inventory")
        return cursor.fetchall()

    def update_stock(self, item_id, stock):
        """Update the stock level for an item."""
        with self.conn:
            self.conn.execute("""
                UPDATE inventory SET stock = ? WHERE item_id = ?
            """, (stock, item_id))

    def log_transaction(self, transaction_id, amount):
        """Log a completed transaction."""
        with self.conn:
            self.conn.execute("""
                INSERT INTO transactions (transaction_id, amount)
                VALUES (?, ?)
            """, (transaction_id, amount))

    def close(self):
        """Close the database connection."""
        self.conn.close()

    def __del__(self):
        """Ensure the connection is closed when the object is destroyed."""
        self.close()
