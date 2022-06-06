import abc

class Register(abc.ABC):
    """
    Abstract Class for registration of things.
    """
    def __init__(self):
        self.register = []
    
    def add_element(self, element):
        """
        Adds new element.
        """
        self.register.append(element)
    
    def del_element(self, element):
        """
        Deletes element.
        """
        for i in range(len(self.register)):
            if self.register[i] is element:
                del self.register[i]
                return True
        return False

    @abc.abstractmethod
    def modify_element(self, element, atribute, value):
        """
        Modifies an element's atribute to a value.
        """
        pass

    @abc.abstractmethod
    def find_element(self, element):
        """
        Finds the element in the registration.
        None if it's not there.
        """
        pass
