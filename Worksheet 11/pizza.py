import abc

class PizzaComponent(abc.ABC):
    """
    Pizza in a restaurant.
    """
    def getDescription(self):
        """
        Pizza's description.
        """
        return self.__class__.__name__
    def getTotalCost(self):
        """
        Pizza's cost.
        """
        return self.__class__.cost


class PizzaBox(PizzaComponent):
    """
    All pizzas come in boxes.
    """
    cost = 0.0


class Decorator(PizzaComponent):
    """
    Decorator design pattern.
    """
    def __init__(self, pizza_component):
        self.component = pizza_component

    def getTotalCost(self):
        return self.component.getTotalCost() + PizzaComponent.getTotalCost(self)

    def getDescription(self):
        return f"{self.component.getDescription()} {PizzaComponent.getDescription(self)}"


class Cheese(Decorator):
    cost = 1.00
    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)


class Tomatoes(Decorator):
    cost = 0.5
    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)


class Pineapple(Decorator):
    cost = 0.75
    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)


class Olives(Decorator):
    cost = 0.10
    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)


class Eggs(Decorator):
    cost = 0.60
    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)


class Onions(Decorator):
    cost = 0.15
    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)


if __name__ == "__main__":
    four_cheeses = Cheese(Cheese(Cheese(Cheese(PizzaBox()))))
    print(f"{four_cheeses.getDescription()}: ${four_cheeses.getTotalCost():.2f}")
    portuguese = Cheese(Onions(Eggs(Olives(PizzaBox()))))
    print(f"{portuguese.getDescription()}: ${portuguese.getTotalCost():.2f}")
    margarita = Cheese(Tomatoes(PizzaBox()))
    print(f"{margarita.getDescription()}: ${margarita.getTotalCost():.2f}")
    Hawain = Cheese(Pineapple(PizzaBox()))
    print(f"{Hawain.getDescription()}: ${Hawain.getTotalCost():.2f}")
