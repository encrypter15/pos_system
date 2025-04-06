class Config:
    def __init__(self):
        # Stripe API key (replace with your own test or live key from stripe.com)
        self.stripe_api_key = "sk_test_your_test_key_here"

        # Currency for transactions
        self.currency = "usd"

        # Database name
        self.db_name = "pos_database.db"

        # Default settings
        self.tax_rate = 0.08  # 8% tax rate (adjust as needed)
        self.timeout_seconds = 30  # Payment timeout in seconds (for mock purposes)
