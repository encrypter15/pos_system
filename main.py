#!/usr/bin/env python3

from inventory import Inventory
from payment import PaymentProcessor
from database import Database
from ui import CLI
from config import Config

def main():
    # Initialize components
    config = Config()
    db = Database("pos_database.db")
    inventory = Inventory(db)
    payment_processor = PaymentProcessor(config.stripe_api_key)
    ui = CLI(inventory, payment_processor)

    # Sample inventory setup (in a real system, this would be loaded from DB)
    inventory.add_item("item1", "Coffee", 3.50, 10)
    inventory.add_item("item2", "Sandwich", 5.00, 5)
    inventory.add_item("item3", "Water", 1.50, 20)

    # Main loop
    while True:
        ui.display_menu()
        choice = ui.get_input("Select an option: ")

        if choice == "1":
            ui.add_to_cart()
        elif choice == "2":
            ui.checkout()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
