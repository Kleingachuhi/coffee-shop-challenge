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
        self._customer = customer
        self._coffee = coffee
        Order.all.append(self)

    def __repr__(self):
     return f"Order for {self._customer} which is {self._coffee} that costs {self._price}"

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
    @property
    def customer(self):
            return self._customer
    
    @property
    def coffee(self):
            return self._coffee
    

my_customer = Customer("Klein")
my_coffee = Coffee("Americano")
new_customer = Customer("Nate")
new_coffee = Coffee("Latte")
order = Order(my_customer, my_coffee, 5.0)
new_order = Order(new_customer, new_coffee, 7.6)
my_coffee._orders.append(order)
my_coffee._customers.append(order._customer)
for coffee in my_coffee._orders:
    my_coffee._count +=1

my_coffee._mean = int(order._price * 10) / my_coffee._count / 10

# order.price = 7.0 --> When you have this, the exception is raised since the price is immutable so the output will be the exception "Price is immutable."
# print(order.price)
print(order)
print(my_coffee.orders())
print(my_coffee.customers())
print(my_coffee.num_order())
print(my_coffee.average_price())
