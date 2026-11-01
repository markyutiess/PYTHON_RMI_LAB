import Pyro5.api

def main():
    ns = Pyro5.api.locate_ns()
    uri = ns.lookup("product.service")
    print("Found object URI:", uri)
    
    product_service = Pyro5.api.Proxy(uri)
    
    print("Requesting product with ID 1...")
    product = product_service.get_product(1)
    
    print("Result from server:", product.get_details())

if __name__ == "__main__":
    main()