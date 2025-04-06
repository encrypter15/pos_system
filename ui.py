class CLI:
    def __init__(self, inventory, payment_processor):
        self.inventory = inventory
        self.payment_processor = payment_processor
        self.cart = []

    def display_menu(self):
        """Display the main menu options."""
        print("\n=== Point of Sale System ===")
        print("1. Add item to cart")
        print("2. Checkout")
        print("3. Exit")

    def get_input(self, prompt):
        """Get user input with a prompt."""
        return input(prompt).strip()

    def add_to_cart(self):
        """Add an item to the cart."""
        print("Available items:")
        for item_id, details in self.inventory.list_items().items():
            print(f"{item_id}: {details['name']} - ${details['price']:.2f} (Stock: {details['stock']})")
        
        item_id = self.get_input("Enter item ID: ")
        if item_id not in self.inventory.list_items():
            print("Invalid item ID.")
            return
        
        try:
            quantity = int(self.get_input("Enter quantity: "))
            if quantity <= 0:
                print("Quantity must be positive.")
                return
            
            if self.inventory.update_stock(item_id, quantity):
                item = self.inventory.get_item(item_id)
                self.cart.append({"item_id": item_id, "name": item["name"], "price": item["price"], "quantity": quantity})
                print(f"Added {quantity} x {item['name']} to cart.")
            else:
                print("Insufficient stock or item not found.")
        except ValueError:
            print("Invalid quantity. Please enter a number.")

    def calculate_total(self):
        """Calculate the total cost of items in the cart."""
        return sum(item["price"] * item["quantity"] for item in self.cart)

    def checkout(self):
        """Process the checkout and payment."""
        if not self.cart:
            print("Cart is empty!")
            return
        
        total = self.calculate_total()
        print(f"\nCart Contents:")
        for item in self.cart:
            print(f"{item['name']} x {item['quantity']} - ${item['price'] * item['quantity']:.2f}")
        print(f"Total: ${total:.2f}")

        confirm = self.get_input("Proceed with payment? (y/n): ").lower()
        if confirm != "y":
            print("Checkout cancelled.")
            return

        # Process payment (using mock for now; switch to real in production)
        payment_result = self.payment_processor.process_mock_payment(total)
        # Uncomment the line below and comment the mock one for real Stripe integration
        # payment_result = self.payment_processor.process_payment(total)

        if payment_result["status"] == "success":
            print(f"Payment successful! Transaction ID: {payment_result['transaction_id']}")
            self.cart.clear()  # Clear cart after successful payment
        else:
            print(f"Payment failed: {payment_result.get('error', 'Unknown error')}")
