class PaymentMethod:
    def pay(self, amount: float):
        pass


class CreditCardPayment(PaymentMethod):
    def pay(self, amount: float):
        print(f"Paying {amount} using Credit Card")


class PayPalPayment(PaymentMethod):
    def pay(self, amount: float):
        print(f"Paying {amount} using PayPal")


class BankTransferPayment(PaymentMethod):
    def pay(self, amount: float):
        print(f"Paying {amount} using Bank Transfer")


# Статичний Factory Method для створення способів оплати
class PaymentFactory:
    @staticmethod
    def create_payment(method: str) -> PaymentMethod:
        if method == "credit":
            return CreditCardPayment()
        elif method == "paypal":
            return PayPalPayment()
        elif method == "bank":
            return BankTransferPayment()
        else:
            raise ValueError("Unknown payment method")


# Приклад використання
def process_payment(method: str, amount: float):
    payment = PaymentFactory.create_payment(method)
    payment.pay(amount)


process_payment("credit", 100.0)  # Виведе: Paying 100.0 using Credit Card
process_payment("paypal", 200.0)  # Виведе: Paying 200.0 using PayPal
