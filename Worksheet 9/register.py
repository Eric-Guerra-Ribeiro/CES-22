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


class RegisterPerson(Register):
    """
    Registration for people.
    """
    def __init__(self):
        super().__init__()
    
    def modify_element(self, element, atribute, value):
        """
        Modifies an element's atribute to a value.
        """
        for person in self.register:
            if person is element:
                return person.modify_atribute(atribute, value)
        return False

    def find_element(self, element):
        """
        Finds the person by their name in the registration.
        None if it's not there.
        """
        for person in self.register:
            if person.check_atribute("name") == element:
                return person
        return None
