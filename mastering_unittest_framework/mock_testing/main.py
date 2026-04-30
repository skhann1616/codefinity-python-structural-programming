import unittest
from unittest.mock import MagicMock

class MoneyTransferService:
    def transfer(self, source_account, destination_account, amount):
        if source_account.balance < amount:
            raise ValueError("Insufficient funds")
        source_account.balance -= amount
        destination_account.balance += amount
        return True

# Write your tests below:
# - Define a test class that inherits from unittest.TestCase
# - Implement the required test methods as described in the instructions
class TestMoneyTransferService(unittest.TestCase):
    def setUp(self):
        self.transfer_service = MoneyTransferService()
        self.source_account = MagicMock()
        self.destination_account = MagicMock()

    def test_successful_transfer(self):
        # Set up the account balances
        self.source_account.balance = 1000
        self.destination_account.balance = 500

        # Perform the transfer
        successful = self.transfer_service.transfer(self.source_account, self.destination_account, 200)
        
        # Check balances
        self.assertTrue(successful)
        self.assertEqual(self.source_account.balance, 800)
        self.assertEqual(self.destination_account.balance, 700)

    def test_failed_transfer_due_to_insufficient_funds(self):
        # Set up the account balances
        self.source_account.balance = 100
        self.destination_account.balance = 500

        # Attempt to transfer more than the source balance
        with self.assertRaises(ValueError):
            self.transfer_service.transfer(self.source_account, self.destination_account, 200)
        
        # Verify that balances remain unchanged
        self.assertEqual(self.source_account.balance, 100)
        self.assertEqual(self.destination_account.balance, 500)