class Order:
    """ Single order made by a customer
    """
    def __init__(self, name, customer_table):
        self.name = name
        self.customer_table = customer_table



class OrdersQueue:
    """ A list of all orders that are waiting to be delivered
    """
    def __init__(self):
        self.queue = []


    def add_order(self, order):
        self.queue.append(order)
        print(f"Pedido adicionado: {order.name}")


    def remove_order(self, order):
        """ If the order should be cancelled
        """
        self.queue.remove(order)
        print(f"Pedido removido: {order.name}")


    def complete_order(self):
        completed_order = self.queue.pop(0)
        print(f"Pedido concluído: {completed_order.name}")
        return completed_order
    

    def list_all_orders(self):
        if self.queue:
            print("Fila de pedidos")
            for obj in self.queue:
                print(f"{obj.name} \t Mesa {obj.customer_table}")
        else:
            print("Nenhum pedido na fila.")
        print("\n")


def main():
    print("\n")

    orders_queue = OrdersQueue()
    order1 = Order("Pizza de Frango", 49)
    order2 = Order("Pizza de Brócolis", 72)
    order3 = Order("Lasanha à Bolonhesa", 23)

    orders_queue.list_all_orders()

    # add
    orders_queue.add_order(order1)
    orders_queue.add_order(order2)
    orders_queue.list_all_orders()

    # remove
    orders_queue.remove_order(order1)
    orders_queue.list_all_orders()

    # add
    orders_queue.add_order(order3)
    orders_queue.add_order(order1)
    orders_queue.list_all_orders()

    # complete
    orders_queue.complete_order()
    orders_queue.list_all_orders()
    # complete
    orders_queue.complete_order()
    orders_queue.list_all_orders()
    # complete
    orders_queue.complete_order()
    orders_queue.list_all_orders()


main()