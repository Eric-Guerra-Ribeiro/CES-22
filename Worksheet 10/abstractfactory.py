import abc

class Cake(abc.ABC):
    """
    The Cake is a Lie.
    """
    def __init__(self):
        self.ingredient = None
        self.style = None
        self.topping = None

    def set_style(self, style):
        """
        Sets the cake's style.
        """
        self.style = style
    
    def set_topping(self, topping):
        """
        Sets the cake's topping.
        """
        self.topping = topping
    
    def __str__(self) -> str:
        return (f"{self.ingredient} Cake: {'No' if self.topping is None else self.topping} Topping, "
                + f"{'No' if self.style is None else self.style} Style.")

class CarrotCake(Cake):
    """
    Carrot Cake
    """
    def __init__(self):
        super().__init__()
        self.ingredient = "Carrot"

class ChocolateCake(Cake):
    """
    Chocolate Cake
    """
    def __init__(self) -> None:
        super().__init__()
        self.ingredient = "Chocolate"

class CassavaCake(Cake):
    """
    Cassava Cake
    """
    def __init__(self) -> None:
        super().__init__()
        self.ingredient = "Cassava"

class AbstractCakeFactory(abc.ABC):
    """
    Abstract Cake Factory
    """
    @abc.abstractstaticmethod
    def make_carrot_cake():
        """
        Makes a carrot cake.
        """
        pass

    @abc.abstractstaticmethod
    def make_chocolate_cake():
        """
        Makes a chocolate cake.
        """
        pass

    @abc.abstractstaticmethod
    def make_cassava_cake():
        """
        Makes a cassava cake.
        """
        pass

class WeddingCakeNoToppingFactory(AbstractCakeFactory):
    def make_carrot_cake():
        cake = CarrotCake()
        cake.set_style("Wedding")
        cake.set_topping(None)
        return cake
        
    def make_chocolate_cake():
        cake = ChocolateCake()
        cake.set_style("Wedding")
        cake.set_topping(None)
        return cake

    def make_cassava_cake():
        cake = CassavaCake()
        cake.set_style("Wedding")
        cake.set_topping(None)
        return cake

class WeddingCakeWhippedCreamToppingFactory(AbstractCakeFactory):
    def make_carrot_cake():
        cake = CarrotCake()
        cake.set_style("Wedding")
        cake.set_topping("Whipped Cream")
        return cake
        
    def make_chocolate_cake():
        cake = ChocolateCake()
        cake.set_style("Wedding")
        cake.set_topping("Whipped Cream")
        return cake

    def make_cassava_cake():
        cake = CassavaCake()
        cake.set_style("Wedding")
        cake.set_topping("Whipped Cream")
        return cake

class BirthdayCakeNoToppingFactory(AbstractCakeFactory):
    def make_carrot_cake():
        cake = CarrotCake()
        cake.set_style("Birthday")
        cake.set_topping(None)
        return cake
        
    def make_chocolate_cake():
        cake = ChocolateCake()
        cake.set_style("Birthday")
        cake.set_topping(None)
        return cake

    def make_cassava_cake():
        cake = CassavaCake()
        cake.set_style("Birthday")
        cake.set_topping(None)
        return cake

class BirthdayCakeWhippedCreamToppingFactory(AbstractCakeFactory):
    def make_carrot_cake():
        cake = CarrotCake()
        cake.set_style("Birthday")
        cake.set_topping("Whipped Cream")
        return cake
        
    def make_chocolate_cake():
        cake = ChocolateCake()
        cake.set_style("Birthday")
        cake.set_topping("Whipped Cream")
        return cake

    def make_cassava_cake():
        cake = CassavaCake()
        cake.set_style("Birthday")
        cake.set_topping("Whipped Cream")
        return cake

class InformalCakeNoToppingFactory(AbstractCakeFactory):
    def make_carrot_cake():
        cake = CarrotCake()
        cake.set_style("Informal")
        cake.set_topping(None)
        return cake
        
    def make_chocolate_cake():
        cake = ChocolateCake()
        cake.set_style("Informal")
        cake.set_topping(None)
        return cake

    def make_cassava_cake():
        cake = CassavaCake()
        cake.set_style("Informal")
        cake.set_topping(None)
        return cake

class InformalCakeWhippedCreamToppingFactory(AbstractCakeFactory):
    def make_carrot_cake():
        cake = CarrotCake()
        cake.set_style("Informal")
        cake.set_topping("Whipped Cream")
        return cake
        
    def make_chocolate_cake():
        cake = ChocolateCake()
        cake.set_style("Informal")
        cake.set_topping("Whipped Cream")
        return cake

    def make_cassava_cake():
        cake = CassavaCake()
        cake.set_style("Informal")
        cake.set_topping("Whipped Cream")
        return cake

if __name__ == "__main__":
    print("Wedding Carrot Cake no Topping:")
    print(WeddingCakeNoToppingFactory.make_carrot_cake())
    print()
    print("Informal Cassava Cake Whipped Cream Topping:")
    print(InformalCakeWhippedCreamToppingFactory.make_cassava_cake())
    print()
    print("Birthday Chocolate Cake Whipped Cream Topping:")
    print(BirthdayCakeWhippedCreamToppingFactory.make_chocolate_cake())
