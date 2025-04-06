# Point of Sale (POS) System

**Author**: Encrypter15  
**Email**: encrypter15@gmail.com  
**License**: BSD License (see below for details)  
**Date**: April 06, 2025

## Description

This is a fully-fledged Point of Sale (POS) system written in Python, designed to manage inventory, process payments, and log transactions. It includes a command-line interface (CLI) for user interaction, with modular components that can be extended to support a graphical user interface (GUI) or additional features. The system integrates with the Stripe API for real payment processing, though it includes a mock payment option for testing.

### Features
- **Inventory Management**: Add, update, and track stock levels for items.
- **Payment Processing**: Supports Stripe API for card payments, with a mock processor for testing.
- **Database Storage**: Uses SQLite to persistently store inventory and transaction data.
- **CLI Interface**: Simple command-line interaction to add items to a cart, checkout, and exit.
- **Modular Design**: Separates concerns into distinct modules (`main.py`, `payment.py`, `inventory.py`, `database.py`, `ui.py`, `config.py`).

## Directory Structure
```
pos_system/
├── main.py          # Main entry point and CLI loop
├── payment.py       # Payment processing logic (Stripe integration)
├── inventory.py     # Inventory management
├── database.py      # SQLite database handling
├── ui.py            # Command-line user interface
├── config.py        # Configuration settings (API keys, etc.)
└── README.md        # This file
```

## Requirements
- Python 3.6 or higher
- SQLite (included with Python)
- Stripe Python library (`pip install stripe`) for real payment processing

## Installation
1. **Clone or Download**: Obtain the `pos_system/` directory.
2. **Install Dependencies**:
   ```bash
   pip install stripe
   ```
3. **Update Configuration**:
   - Open `config.py` and replace `"sk_test_your_test_key_here"` with your Stripe API key (get it from [stripe.com](https://stripe.com)).
   - Optionally adjust `currency`, `tax_rate`, or other settings.

## Usage
1. **Navigate to the Directory**:
   ```bash
   cd pos_system
   ```
2. **Run the System**:
   ```bash
   ./main.py
   ```
3. **Interact with the CLI**:
   - **Option 1**: Add items to the cart by entering an item ID (e.g., `item1`) and quantity.
   - **Option 2**: Checkout to process payment (uses mock payment by default; edit `ui.py` to use real Stripe payments).
   - **Option 3**: Exit the program.

### Example Run
```
=== Point of Sale System ===
1. Add item to cart
2. Checkout
3. Exit
Select an option: 1
Available items:
item1: Coffee - $3.50 (Stock: 10)
item2: Sandwich - $5.00 (Stock: 5)
item3: Water - $1.50 (Stock: 20)
Enter item ID: item1
Enter quantity: 2
Added 2 x Coffee to cart.
```

## Configuration
- **Stripe Integration**: To use real payments, replace `process_mock_payment` with `process_payment` in `ui.py`’s `checkout` method and ensure a valid API key is set in `config.py`.
- **Database**: The SQLite database (`pos_database.db`) is created automatically in the `pos_system/` directory.

## Extending the System
- **GUI**: Replace `ui.py` with a GUI framework (e.g., Tkinter, PyQt).
- **Tax Calculation**: Add tax logic in `ui.py` using `config.tax_rate`.
- **Hardware**: Integrate card readers via Stripe Terminal or Square SDKs.

## License
BSD 3-Clause License

Copyright (c) 2025, Encrypter15

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
EOF

echo "README.md created and populated successfully!"
```

---

### How to Use
1. Save the script as `populate_readme.sh`.
2. Ensure you’re in the same directory as `pos_system/` (where the initial setup was run).
3. Run it with:
   ```bash
   bash populate_readme.sh
   ```
4. This will create and populate `pos_system/README.md` with the content above.

---

### Explanation of `README.md`
- **Metadata**: Includes author, email, license, and date (April 06, 2025, per the current date provided).
- **Description**: Details the system’s purpose, features, and structure.
- **Instructions**: Provides steps for installation, usage, and configuration.
- **License**: Uses the BSD 3-Clause License as requested, with standard terms.

---

### Notes
- The `README.md` assumes the system is complete with all previous files (`main.py`, `payment.py`, `inventory.py`, `database.py`, `ui.py`, `config.py`).
- You can view the file with:
  ```bash
  cat pos_system/README.md
  ```

