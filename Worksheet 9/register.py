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

    def print_register(self):
        """
        Prints all elements in register.
        """
        print(self.register)


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
            if person.check_atribute("name", element):
                return person
        return None


class RegisterProduct(Register):
    """
    Registration for products.
    """
    def __init__(self):
        super().__init__()
    
    def modify_element(self, element, atribute, value):
        """
        Modifies an element's atribute to a value.
        """
        for product in self.register:
            if product is element:
                return product.modify_atribute(atribute, value)
        return False


class RegisterBook(RegisterProduct):
    """
    Registration for books.
    """
    def __init__(self, writer_register):
        super().__init__()
        self.writers = writer_register
    
    def add_element(self, element):
        """
        Adds new book to the register
        """
        for writer in self.writers:
            if writer is element.get_atribute("writer"):
                writer.modify_atribute("published_titles", element)
        super().add_element(element)
    
    def del_element(self, element):
        """
        Deletes book from the register.
        """
        for i in range(len(element.writer.published_titles)):
            if element.writer.published_titles[i] is element:
                del element.writer.published_titles[i]
                return super().del_element(element)
        return False

    def find_element(self, element):
        """
        Finds the book by their title in the registration.
        None if it's not there.
        """
        for book in self.register:
            if book.check_atribute("title", element):
                return book
        return None

    def find_books_writer(self, writer_name):
        """
        Returns all published titles by a writer.
        """
        return self.writers.find_element(writer_name)
