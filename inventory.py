class Inventory:
    def __init__(self, database):
        self.db = database
        self.items = {}
        # Load initial inventory from database (if any)
        self.load_from_db()

    def load_from_db(self):
        """Load inventory from the database into memory."""
        inventory_data = self.db.get_all_items()
        for item_id, name, price, stock in inventory_data:
            self.items[item_id] = {
                "name": name,
                "price": price,
                "stock": stock
            }

    def add_item(self, item_id, name, price, stock):
        """Add or update an item in the inventory and database."""
        self.items[item_id] = {
            "name": name,
            "price": price,
            "stock": stock
        }
        self.db.add_item(item_id, name, price, stock)

    def get_item(self, item_id):
        """Retrieve an item by ID."""
        return self.items.get(item_id, None)

    def update_stock(self, item_id, quantity):
        """Update stock levels after a sale."""
        if item_id in self.items and self.items[item_id]["stock"] >= quantity:
            self.items[item_id]["stock"] -= quantity
            self.db.update_stock(item_id, self.items[item_id]["stock"])
            return True
        return False

    def list_items(self):
        """Return all items in the inventory."""
        return self.items
