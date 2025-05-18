class Customer:
    def __init__(self, name):
        self.name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1<= len(name) <= 15:
            self._name = name
        else:
            raise Exception("The  customer name must be a string with characters between 1 and 15.")
        
my_customer = Customer("Klein")