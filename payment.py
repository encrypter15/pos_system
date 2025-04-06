import stripe
import time

class PaymentProcessor:
    def __init__(self, api_key):
        self.api_key = api_key
        stripe.api_key = self.api_key

    def process_payment(self, amount):
        """
        Process a payment using Stripe API.
        Amount is in dollars (e.g., 5.50), converted to cents for Stripe.
        Returns a dict with status and transaction details.
        """
        try:
            # Create a payment intent (amount in cents)
            payment_intent = stripe.PaymentIntent.create(
                amount=int(amount * 100),  # Convert dollars to cents
                currency="usd",
                payment_method_types=["card"],
                description="POS Transaction"
            )
            # For simplicity, simulate confirmation (in reality, this requires frontend card input)
            # Using a test card like 4242 4242 4242 4242 would be confirmed here
            stripe.PaymentIntent.confirm(payment_intent["id"])
            return {
                "status": "success",
                "transaction_id": payment_intent["id"],
                "amount": amount
            }
        except stripe.error.StripeError as e:
            return {
                "status": "failed",
                "error": str(e)
            }

    def process_mock_payment(self, amount):
        """
        Mock payment processing for testing without real API calls.
        """
        print(f"Processing mock payment of ${amount:.2f}...")
        time.sleep(2)  # Simulate network delay
        return {
            "status": "success",
            "transaction_id": "mock12345",
            "amount": amount
        }
