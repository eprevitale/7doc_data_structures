class Product:
    """ Single product of a store
    """
    def __init__(self, code, name, price, quantity):
        self.previous_product = None
        self.code = code
        self.name = name
        self.price = price
        self.quantity = quantity
        self.next_product = None

    
    def buy_product(self, qtd):
        self.quantity += qtd
        print(f"{qtd} unidades do produto {self.name} compradas!")

    def sell_product(self, qtd):
        self.quantity -= qtd
        print(f"{qtd} unidades do produto {self.name} vendidas!")



class ProductsList:
    """ A list of all of a store's products
    """
    def __init__(self):
        self.head = None
        self.tail = None


    def list_all_products(self):
        if self.head:
            print(f"HEAD --> {self.head.name}")
            print(f"TAIL --> {self.tail.name}")
            print("Lista de produtos:")
            print("Código \t Nome \t Preço \t Quantidade")
            current_product = self.head
            while current_product != None:
                print(f"{current_product.code} \t {current_product.name} \t {current_product.price} \t {current_product.quantity}")
                current_product = current_product.next_product
            print("\n")
        else:
            print("Nenhum produto na lista.\n")


    def add_product(self, product):
        if not self.head:
            self.head = product
        else:
            product.previous_product = self.tail
            self.tail.next_product = product

        self.tail = product
        print(f"{product.name} adicionado!")


    def remove_product(self, product):
        if not self.head:
            print("Nenhum produto para remover!")
        else:
            if product == self.head:
                product.next_product.previous_product = None
                self.head = product.next_product
            elif product == self.tail:
                product.previous_product.next_product = None
                self.tail = product.previous_product
            else:
                product.previous_product.next_product = product.next_product
                product.next_product.previous_product = product.previous_product
            
            print(f"{product.name} removido!")



def main():
    product1 = Product("123456789", "Produto 1", "10.00", 5)
    product2 = Product("987654321", "Produto 2", "20.00", 4)
    product3 = Product("132457689", "Produto 3", "30.00", 3)

    # add
    products_list = ProductsList()
    products_list.list_all_products() # Nenhum produto na lista.
    products_list.add_product(product1) 
    products_list.add_product(product2) 
    products_list.list_all_products()
    products_list.add_product(product3)
    products_list.list_all_products()

    # remove
    products_list.remove_product(product3)
    products_list.list_all_products()

    # buy
    product1.buy_product(2)
    product2.buy_product(4)
    products_list.list_all_products()

    # sell
    product1.sell_product(2)
    product2.sell_product(4)
    products_list.list_all_products()

main()