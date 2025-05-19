class Customer:
    order_list = []
    # all_orders = []
    def __init__(self, name):
        self.name = name
        # Customer.all_orders.append(self)
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1<= len(name) <= 15:
            self._name = name
        else:
            raise Exception("The  customer name must be a string with characters between 1 and 15.")
    def orders(self):
            from order import Order
            return [item for item in Order.all ]
    
    def coffees(self):
         from order import Order
         return [order.coffee for order in Order.all]
    
    def customers(self):
         from order import Order
         return [order.customer for order in Order.all if isinstance(my_customer, Customer)]
            
    # def create_order(self, coffee, price):
    #     self.coffee = coffee
    #     self.price = price
    #     Customer.all_orders.append(self)
        
my_customer = Customer("Klein")
# my_customer.create_order("Americano", 4000)
# print(my_customer)
print(my_customer.customers())