import example1
import example2
import example3

# Example 1
print("Example 1")
print()
# Abstract Class/Method
try:
    example1.Polygon()
except:
    print("Can't create abstract class instance.")

# Instance Method
square = example1.Square(3)
print(square.area())
# Class Method
print(example1.Square.from_area(example1.Square, 9).a)
# Static Method
print(example1.Square.area_formula())

# Example 2
print("Example 2")
print()

print(example2.division(10, 2))
print(example2.division(1, 0))

# Example 3
print("Example 3")
print()

print("Class A")
example3.A()
print()

print("Class B")
example3.B()
print()

print("Class C")
example3.C()
print()

print("Class D")
example3.D()
print()

print("Class E")
example3.E()
print()

print("Class F")
example3.F()
print()
