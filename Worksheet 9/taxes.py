import abc

class TaxCalculator(abc.ABC):
    """
    Abstract Interface class for calculating taxes.
    """
    def __init__(self) -> None:
        pass

    @abc.abstractmethod
    def get_taxes(self, **kwargs) -> float:
        pass


class BookTaxCalculator(abc.ABC):
    """
    Calulates taxes for books.
    """
    def __init__(self) -> None:
        super().__init__()
    
    def get_taxes(self, **kwargs) ->float:
        genre = str.lower(kwargs["genre"])
        if genre == "fiction":
            genre_rate = 0.30
        elif genre == "educational":
            genre_rate = 0.
        elif genre == "non-fiction":
            genre_rate = 0.15
        else:
            genre_rate = 0.40
        return genre_rate*(kwargs["sell_price"] - kwargs["buy_price"])

