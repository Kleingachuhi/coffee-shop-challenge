class Coffee:
    def __init__(self, name):
        self.name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise Exception("The coffee name must be a string with at least 3 characters.")
my_cofee = Coffee("Americano")