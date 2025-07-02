class FoodProduct:
    def __init__(self):
        self.type = "food product"
        self.name = None

    def _product_type(self):
        return f"{self.type}"

    def _product_name(self):
        return f"{self.name}"


class SignProduct(FoodProduct):
    def __init__(self, id, name):
        super().__init__()
        self.id = id
        self.name = name

    def upsert_product(self):
        if self.id:
            return f"'{self.id}:{self.name}' insert success"


product = FoodProduct()
bread = SignProduct(1, "bread")

print(bread.upsert_product())
print(bread._product_type())  # an other languages its shoud be encapsulation error.
print(bread._product_name())  # an other languages its shoud be encapsulation error.
