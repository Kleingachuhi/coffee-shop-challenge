class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, price):
        if isinstance(price, float) and 1.0<= price <= 10.0:
            self._price = price    
        else:
            raise Exception("The price for order muust be a float between 1.0 and 10.0.")