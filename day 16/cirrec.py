# Base class
class Shape:
    def area(self):
        pass  # To be overridden by child classes

    def perimeter(self):
        pass  # To be overridden by child classes

# Child class: Circle
class Circle(Shape):
    def _init_(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Child class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# --- Test the classes ---
circle1 = Circle(5)
rectangle1 = Rectangle(4, 6)

print("Circle Area:", circle1.area())
print("Circle Perimeter:", circle1.perimeter())
print("Rectangle Area:", rectangle1.area())
print("Rectangle Perimeter:", rectangle1.perimeter())