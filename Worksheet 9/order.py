import abc

class OrderInterface(abc.ABC):
    """
    Class interface for client's buy orders.
    """
    def __init__(self, client, order_list=[]):
        self.client = client
        self.order_list = order_list
        
    @abc.abstractmethod
    def add_order_item(self, **kwargs):
        """
        Adds order item to list
        """
        pass

    @abc.abstractmethod
    def modify_order_item(self, **kwargs):
        """
        Modify order item in list.
        Returns if modification was successful.
        """
        pass

    @abc.abstractmethod
    def delete_order_item(self, **kwargs):
        """
        Deletes order item in list.
        """
        pass


class OrderProduct(OrderInterface):
    """
    Class interface for client's buy product orders.
    """
    def __init__(self, client, order_list=[]):
        super().__init__(client, order_list)

    def add_order_item(self, **kwargs):
        """
        Adds product to list
        """
        price = kwargs["price"] if "price" in kwargs.keys() else kwargs["product"].get_atribute("sell_price")
        self.order_list.append({"product":kwargs["product"], "qnty":kwargs["qnty"], "price":price})
    
    def modify_order_item(self, **kwargs):
        """
        Modify product item in list.
        Returns if modification was successful.
        """
        if kwargs["new_qnty"] == 0:
            return self.delete_order_item(kwargs)
        product = kwargs["product"]
        for order in self.order_list:
            if order["product"] is product:
                order["qnty"] = kwargs["new_qnty"]
                return True
        return False

    def delete_order_item(self, **kwargs):
        """
        Deletes product item in list.
        """
        product = kwargs["product"]
        for i in range(len(self.order_list)):
            if self.order_list[i]["product"] is product:
                del self.order_list[i]
                return True
        return False
