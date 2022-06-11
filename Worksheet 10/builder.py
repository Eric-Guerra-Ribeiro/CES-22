import abc

class Cake():
    """
    The Cake is a Lie.
    """
    def __init__(self):
        self.ingredient = None
        self.style = None
        self.topping = None
    
    def set_ingredient(self, ingredient):
        """
        Sets the cake's ingredient.
        """
        self.ingredient = ingredient

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


class Builder(abc.ABC):
    """
    Abstract Builder Class
    """
    @abc.abstractstaticmethod
    def build_cake(cake):
        pass


class CarrotCakeBuilder(Builder):
    """
    Builds carrot cakes.
    """
    def build_cake(cake:Cake):
        cake.set_ingredient("Carrot")


class CassavaCakeBuilder(Builder):
    """
    Builds cassava cakes.
    """
    def build_cake(cake:Cake):
        cake.set_ingredient("Cassava")


class ChocolateCakeBuilder(Builder):
    """
    Builds chocolate cakes.
    """
    def build_cake(cake:Cake):
        cake.set_ingredient("Chocolate")


class WeddingCakeBuilder(Builder):
    """
    Builds wedding cakes.
    """
    def build_cake(cake:Cake):
        cake.set_style("Wedding")


class InformalCakeBuilder(Builder):
    """
    Builds informal cakes.
    """
    def build_cake(cake:Cake):
        cake.set_style("Informal")


class BirthdayCakeBuilder(Builder):
    """
    Builds birthday cakes.
    """
    def build_cake(cake:Cake):
        cake.set_style("Birthday")


class NoToppingCakeBuilder(Builder):
    """
    Builds no topping cakes.
    """
    def build_cake(cake:Cake):
        cake.set_topping(None)


class WhippedCreamCakeBuilder(Builder):
    """
    Builds whipped cream cakes.
    """
    def build_cake(cake:Cake):
        cake.set_topping("Whipped Cream")


class Director:
    """
    Directs the build process.
    """
    def __init__(self, ingredient_builder, style_builder, topping_builder) -> None:
        self.ingredient_builder = ingredient_builder
        self.style_builder = style_builder
        self.topping_builder = topping_builder
    
    def build_cake(self):
        cake = Cake()
        self.ingredient_builder.build_cake(cake)
        self.style_builder.build_cake(cake)
        self.topping_builder.build_cake(cake)
        return cake
        


if __name__ == "__main__":
    director = Director(CarrotCakeBuilder, WeddingCakeBuilder, NoToppingCakeBuilder)
    print("Wedding Carrot Cake no Topping:")
    print(director.build_cake())
    print()
    director = Director(CassavaCakeBuilder, InformalCakeBuilder, WhippedCreamCakeBuilder)
    print("Informal Cassava Cake Whipped Cream Topping:")
    print(director.build_cake())
    print()
    director = Director(ChocolateCakeBuilder, BirthdayCakeBuilder, WhippedCreamCakeBuilder)
    print("Birthday Chocolate Cake Whipped Cream Topping:")
    print(director.build_cake())
