''' Set 3 (Online Shopping Cart)
An e-commerce platform manages different product categories.
Scenario:
Base class Product with attributes price and quantity


Subclasses: Electronics, Clothing


Requirements:
Override calculate_discount() for each category


Electronics get warranty cost added


Clothing gets size-based discount


Compute final cart value using method overriding'''
class Product:
    def __init__(self,price,quantity):
        self.price = price
        self.quantity = quantity
    def calculate_discount(self):
        return 0
    def final_price(self):
        discount = self.calculate_discount()
        total = (self.price * self.quantity)- discount
        return total
class Electronics (Product):
    def __init__(self,price,quantity,warrenty_cost):
        super().__init__(price,quantity)
        self.warrenty_cost = warrenty_cost

    def calculate_discount(self):
        return -self.warrenty_cost

    def final_price(self):
        total = self.price * self.quantity
        return total + self.warrenty_cost
class Clothing (Product):
    def __init__(self,price,quantity,size):
        super().__init__(price,quantity)
        self.size = size
    def calculate_discount(self):
        total = self.price * self.quantity
        if self.size in ["L", "XL"]:
            return 0.20 * total
        else:
            return 0.10 * total

cart = [
        Electronics(price=1000, quantity=1, warrenty_cost=2000),
        Clothing(price=1200, quantity=2, size="XL")
]

final_cart_value = 0
for product in cart:
    final_cart_value += product.final_price()

    print("Final cart value: ", final_cart_value)