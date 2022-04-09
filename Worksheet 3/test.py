import example1

# Example 1

# Abstract Class/Method
try:
    example1.Polygon()
except:
    print("Can't create abstract class instance.")

# Instance Method
square = example1.Square(3)
print(square.area())
# 
print(example1.Square.unitary_polygon())
# Static Method
print(example1.Square.area_formula())
