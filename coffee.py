class Coffee:
    def __init__(self, name):
        self._set_coffee = False
        self.name = name
        self._orders = []
        self._customers = []
        self._count = 0
        self._mean = 0
    def __repr__(self):
        return f"{self._name}"
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if self._set_coffee:
            raise Exception("Coffee name is immutable.")
        if  isinstance(name, str) and len(name) >= 3:
            self._name = name
            self._set_coffee = True
        else:
            raise Exception("The coffee name must be a string with at least 3 characters.")


    def orders(self):
        return self._orders
    def customers(self):
        return self._customers
    
    def num_order(self):
        return self._count
    def average_price(self):
        for item in self._orders:
            self._mean = int(item.price *10) / self._count / 10
        return self._mean

my_cofee = Coffee("Americano")
new_coffee = Coffee("Latte")
# my_cofee.name = "Expresso" --> When this is uncommented out, the output will be the Exception of "Coffee name is immutable." because the coffe name is immutable but this tries to assign a new coffee name replacing the already existing coffee name. 
# print(my_cofee.name)

print(my_cofee.orders())
# print(my_cofee.num_order())