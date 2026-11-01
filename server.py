import Pyro5.api
import Pyro5.server
from product import Product

@Pyro5.api.expose
class ProductImpl:
    def get_product(self, product_id):
        if product_id == 1:
            return Product(1, "Laptop", 50000)
        else:
            return Product(product_id, "Unknown", 0)

def main():
    daemon = Pyro5.server.Daemon()
    ns = Pyro5.api.locate_ns()
    uri = daemon.register(ProductImpl)
    ns.register("product.service", uri)
    
    print("Server is ready. Object URI:", uri)
    print("Registered as 'product.service' in Name Server.")
    print("Press Ctrl+C to stop the server.")
    
    daemon.requestLoop()

if __name__ == "__main__":
    main()