import abc

import taxes

class Product(abc.ABC):
    """
    Abstract Interface Class for a product.
    """
    def __init__(self):
        pass

    @abc.abstractmethod
    def get_atribute(self, atribute):
        """
        Gets the product's atribute value.
        Raises exception if atribute not found.
        """
        pass

    @abc.abstractmethod
    def check_atribute(self, atribute, value):
        """
        Checks if the product's atribute has a given value.
        """
        pass

    @abc.abstractmethod
    def modify_atribute(self, atribute, value):
        """
        Modifies the product's atribute to a given value.
        Returns if the atribute was successfuly modified.
        """
        pass


class Book(Product):
    """
    Book as a product.
    """
    taxes_calculator = taxes.BookTaxCalculator()

    def __init__(self, title, writer, genre, edition, publisher, sell_price, buy_price):
        super().__init__()
        self.title = title
        self.writer = writer
        self.genre = genre
        self.edition = edition
        self.publisher = publisher
        self.sell_price = sell_price
        self.buy_price = buy_price
        self.taxes = self.taxes_calculator.get_taxes(genre=self.genre, sell_price=self.sell_price,
                                                     buy_price=self.buy_price)

    def get_atribute(self, atribute):
        """
        Gets the product's atribute value.
        Raises exception if atribute not found.
        """
        atribute = str.lower(atribute)
        if atribute == "title":
            return self.title
        elif atribute == "writer":
            return self.writer
        elif atribute == "genre":
            return self.genre
        elif atribute == "edition":
            return self.edition
        elif atribute == "publisher":
            return self.publisher
        elif atribute == "sell_price":
            return self.sell_price
        elif atribute == "buy_price":
            return self.buy_price
        elif atribute == "taxes":
            return self.taxes
        else:
            raise Exception(f"Error 404: {atribute} not found")
        

    def check_atribute(self, atribute, value):
        """
        Checks if the product's atribute has a given value.
        """
        atribute = str.lower(atribute)
        if atribute == "title":
            return self.title == value
        elif atribute == "writer":
            return self.writer == value
        elif atribute == "genre":
            return self.genre == value
        elif atribute == "edition":
            return self.edition == value
        elif atribute == "publisher":
            return self.publisher == value
        elif atribute == "sell_price" or atribute == "sell price":
            return self.sell_price == value
        elif atribute == "buy_price" or atribute == "buy price":
            return self.buy_price == value
        elif atribute == "taxes":
            return self.taxes == value
        else:
            return False

    def modify_atribute(self, atribute, value):
        """
        Modifies the product's atribute to a given value.
        Returns if the atribute was successfuly modified.
        """
        atribute = str.lower(atribute)
        if atribute == "title":
            self.title = value
        elif atribute == "writer":
            self.writer = value
        elif atribute == "genre":
            self.genre = value
        elif atribute == "edition":
            self.edition = value
        elif atribute == "publisher":
            self.publisher = value
        elif atribute == "sell_price":
            self.sell_price = value
        elif atribute == "buy_price":
            self.buy_price = value
        elif atribute == "taxes":
            self.taxes = value
        else:
            return False
        return True
    
    def __str__(self) -> str:
        return f"{self.title}"
