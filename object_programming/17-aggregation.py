class Product:
    def __init__(self, name, value):
        self.__name=name
        self.__value=value

    def product_description(self):
        return f"{self.__name}, {self.__value}"

class ShoppingCart:
    def __init__(self):
        self.__product= []

    def add_product(self, product: Product):
        self.__product.append(product)

    def buy_product(self):
        print("buy products")
        for item in self.__product:
            print(item.product_description())


bmw = Product("BMW", 120_000_000)
ferrari = Product("Ferrari", 140_000_000)
tractor = Product("Tractor", 820_000_000)

shopping_cart = ShoppingCart()

shopping_cart.add_product(bmw)
shopping_cart.add_product(ferrari)
shopping_cart.add_product(tractor)

shopping_cart.buy_product()

