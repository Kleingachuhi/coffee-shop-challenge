class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []
        self.new_order = []
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1<= len(name) <= 15:
            self._name = name
        else:
            raise Exception("The  customer name must be a string with characters between 1 and 15.")
    def __repr__(self):
        return f"{self._name}"
    def add_order_to_orders_list(self, order):
        from order import Order
        if isinstance(order, Order):
            self._orders.append(order)
    def orders(self):
        return self._orders    
    def coffees(self):
         return [order.name for order in self._orders]    
    def customers(self):
         return [order.name for order in self._orders]
            
    def create_order(self, coffee, price):
        self.coffee = coffee
        self.price = price
    def add_order(self):
        self.new_order.append(self)
        return self.new_order
    
    @classmethod
    def most_aficionado(cls, coffee):
        pass
    
my_customer = Customer("Klein")
new_customer = Customer("Nate")
my_customer.create_order("Macchiatto", 5.6)
# my_customer.create_order("Americano", 4000)
# print(my_customer)
print(my_customer.add_order())
