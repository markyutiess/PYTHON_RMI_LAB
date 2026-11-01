import Pyro5.api

@Pyro5.api.expose
class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def get_details(self):
        return f"Product ID: {self.id}, Name: {self.name}, Price: {self.price}"