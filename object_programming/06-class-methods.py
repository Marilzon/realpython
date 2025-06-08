from decimal import Decimal


class Checkout:
    tax = 1.15

    def __init__(self, value: Decimal) -> None:
        self.amount = value

    def get_products_amount(self):
        product_value = self.amount * self.tax

        return f"amount: {product_value=:.2f}"

    @classmethod
    def alter_tax(cls, value: Decimal):
        cls.tax = value

checkout_a = Checkout(30.50)
checkout_b = Checkout(50)
checkout_c = Checkout(50)

print(checkout_a.get_products_amount())
print(checkout_b.get_products_amount())
print(checkout_c.get_products_amount())

checkout_c.alter_tax(1)
print(checkout_c.get_products_amount())
