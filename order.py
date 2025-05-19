from coffee import Coffee
from customer import Customer


class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self._set_my_price = False
        self.price = price
        if not isinstance(customer, Customer):
            raise Exception("Customer must be an instance of the Customer class.")
        if not isinstance(coffee, Coffee):
            raise Exception("Coffee must be an instance of the Coffee class.")
        self.customer = customer
        self.coffee = coffee
        Order.all.append(self)
    def __repr__(self):
     return f"Order for {self.customer} which is {self.coffee} that costs {self.price}"
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, price):
        if self._set_my_price:
            raise Exception("Price is immutable.")
        if isinstance(price, float) and 1.0<= price <= 10.0:
            self._price = price    
            self._set_my_price = True
        else:
            raise Exception("The price for order must be a float between 1.0 and 10.0.")


my_customer = Customer("Klein")
my_coffee = Coffee("Americano")
new_customer = "Nate"
new_coffee = "Latte"
order = Order(my_customer, my_coffee, 5.0) 
# order.price = 7.0 --> When you have this, the exception is raised since the price is immutable so the output will be the exception "Price is immutable."
# print(order.price)
