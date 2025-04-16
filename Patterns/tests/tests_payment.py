import sys
import unittest
from io import StringIO

from examples_factory_method.payment_factory_method import process_payment


class TestPaymentFactory(unittest.TestCase):

    def setUp(self):
        # Захоплюємо стандартний вивід для перевірки результатів
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        # Відновлюємо стандартний вивід
        sys.stdout = sys.__stdout__

    def test_credit_card_payment(self):
        """Тест для CreditCardPayment"""
        process_payment("credit", 100.0)
        self.captured_output.seek(0)
        output = self.captured_output.read().strip()
        expected_output = "Paying 100.0 using Credit Card"
        self.assertEqual(output, expected_output)

    def test_paypal_payment(self):
        """Тест для PayPalPayment"""
        process_payment("paypal", 200.0)
        self.captured_output.seek(0)
        output = self.captured_output.read().strip()
        expected_output = "Paying 200.0 using PayPal"
        self.assertEqual(output, expected_output)

    def test_bank_transfer_payment(self):
        """Тест для BankTransferPayment"""
        process_payment("bank", 300.0)
        self.captured_output.seek(0)
        output = self.captured_output.read().strip()
        expected_output = "Paying 300.0 using Bank Transfer"
        self.assertEqual(output, expected_output)

    def test_invalid_payment_method(self):
        """Тест для невідомого методу оплати"""
        with self.assertRaises(ValueError) as context:
            process_payment("crypto", 400.0)
        self.assertEqual(str(context.exception), "Unknown payment method")


if __name__ == "__main__":
    unittest.main()
