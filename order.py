class Order:
    def __init__(self, customer, coffee, price):
        self._set_my_price = False
        self.customer = customer
        self.coffee = coffee
        self.price = price
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
            raise Exception("The price for order muust be a float between 1.0 and 10.0.")
        


order = Order("Klein", "Americano", 5.0) 
# order.price = 7.0 --> When you have this, the exception is raised since the price is immutable so the output will be the exception "The price for order muust be a float between 1.0 and 10.0."
print(order.price)