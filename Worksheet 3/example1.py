import abc

class Polygon:
    def __init__(self, n, a):
        self.a = a
        self.n = n

    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractstaticmethod
    def area_formula():
        pass
    
    @abc.abstractclassmethod
    def unitary_polygon(cls):
        pass

    @staticmethod
    def definition():
        return """
            A Polygon is a plane figure that is described by a finite number of straight line
            segments connected to form a closed polygonal chain.
        """


class Square(Polygon):
    def __init__(self, a):
        super().__init__(4, a)
    
    def area(self):
        return self.a**2
    
    def area_formula():
        return "A = a^2"
    
    def unitary_polygon(cls):
        return cls(1).area()
