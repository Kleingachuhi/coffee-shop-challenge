class Coffee:
    def __init__(self, name):
        self._set_coffee = False
        self.name = name
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
my_cofee = Coffee("Americano")
# my_cofee.name = "Expresso" --> When this is uncommented out, the output will be the Exception of "Coffee name is immutable." because the coffe name is immutable but this tries to assign a new coffee name replacing the already existing coffee name. 
# print(my_cofee.name)

