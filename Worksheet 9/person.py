import abc

class Person(abc.ABC):
    """
    Abstract Interface Class for a person.
    """
    def __init__(self, name, email=None):
        self.name = name
        self.email = (f"{'.'.join(str.lower(name).split())}@gmail.com" if email is None else email)

    @abc.abstractmethod
    def get_atribute(self, atribute):
        """
        Gets the persons's atribute value.
        Raises exception if atribute not found.
        """
        pass

    @abc.abstractmethod
    def check_atribute(self, atribute, value):
        """
        Checks if the persons's atribute has a given value.
        """
        pass

    @abc.abstractmethod
    def modify_atribute(self, atribute, value):
        """
        Modifies the persons's atribute to a given value.
        Returns if the atribute was successfuly modified.
        """
        pass
    
    def __str__(self) -> str:
        return f"{self.name}"


class Writer(Person):
    """
    Writer as a person.
    """

    def __init__(self, name, email=None):
        super().__init__(name, email)
        self.published_titles = []

    def get_atribute(self, atribute):
        """
        Gets the persons's atribute value.
        Raises exception if atribute not found.
        """
        atribute = str.lower(atribute)
        if atribute == "name":
            return self.name
        elif atribute == "email":
            return self.email
        elif atribute == "published_titles":
            return self.published_titles
        else:
            raise Exception(f"Error 404: {atribute} not found")
        

    def check_atribute(self, atribute, value):
        """
        Checks if the persons's atribute has a given value.
        """
        atribute = str.lower(atribute)
        if atribute == "name":
            return self.name == value
        elif atribute == "email":
            return self.email == value
        elif atribute == "published_titles":
            return value.writer is self
        else:
            return False

    def modify_atribute(self, atribute, value):
        """
        Modifies the persons's atribute to a given value.
        Returns if the atribute was successfuly modified.
        """
        atribute = str.lower(atribute)
        if atribute == "name":
            self.name = value
        elif atribute == "email":
            self.email = value
        elif atribute == "published_titles":
            self.published_titles.append(value) 
        else:
            return False
        return True


class Client(Person):
    """
    Client as a person.
    """

    def __init__(self, name, email=None):
        super().__init__(name, email)
        self.past_orders = []

    def get_atribute(self, atribute):
        """
        Gets the persons's atribute value.
        Raises exception if atribute not found.
        """
        atribute = str.lower(atribute)
        if atribute == "name":
            return self.name
        elif atribute == "email":
            return self.email
        elif atribute == "past_orders":
            return self.past_orders
        else:
            raise Exception(f"Error 404: {atribute} not found")
        

    def check_atribute(self, atribute, value):
        """
        Checks if the persons's atribute has a given value.
        """
        atribute = str.lower(atribute)
        if atribute == "name":
            return self.name == value
        elif atribute == "email":
            return self.email == value
        elif atribute == "past_orders":
            return value.client is self
        else:
            return False

    def modify_atribute(self, atribute, value):
        """
        Modifies the persons's atribute to a given value.
        Returns if the atribute was successfuly modified.
        """
        atribute = str.lower(atribute)
        if atribute == "name":
            self.name = value
        elif atribute == "email":
            self.email = value
        elif atribute == "past_orders":
            self.past_orders.append(value) 
        else:
            return False
        return True
