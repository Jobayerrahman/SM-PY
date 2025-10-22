class Mobile:
    # Class variable (same for all mobiles)
    brand = "Samsung"

    def __init__(self, model, price):
        # Instance variables (different per object)
        self.model = model
        self.price = price


mobile1 = Mobile("Galaxy A12", 15000)
mobile2 = Mobile("Galaxy S22", 90000)

print(mobile1.brand)  # Access class variable
print(mobile2.brand)

print(mobile1.model)  # Access instance variable
print(mobile2.model)



# ---------------------- Real-Life Example ----------------------


class FoodOrder:
    delivery_charge = 50  # Class variable (same charge for all orders)

    def __init__(self, customer_name, food_item, price):
        self.customer_name = customer_name  # instance variable
        self.food_item = food_item          # instance variable
        self.price = price                  # instance variable

    def total_price(self):
        return self.price + FoodOrder.delivery_charge


order1 = FoodOrder("Rahim", "Burger", 200)
order2 = FoodOrder("Karim", "Pizza", 400)

print(order1.total_price())  # 200 + 50 = 250
print(order2.total_price())  # 400 + 50 = 450
