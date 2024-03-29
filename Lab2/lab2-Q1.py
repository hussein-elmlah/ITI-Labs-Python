from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self, name, color):
        self.name = name
        self._color = color
    
    def set_color(self, color):
        self._color = color
    
    def get_color(self):
        return self._color
    
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, name, color, radius):
        super().__init__(name, color)
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius**2

class Square(Shape):
    def __init__(self, name, color, side):
        super().__init__(name, color)
        self.side = side
    
    def calculate_area(self):
        return self.side**2

class Rectangle(Shape):
    def __init__(self, name, color, length, width):
        super().__init__(name, color)
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width

# Test the classes
circle = Circle("Circle", "red", 5)
square = Square("Square", "blue", 5)
rectangle = Rectangle("Rectangle", "green", 5, 5)

print("Area of Circle:", circle.calculate_area())
print("Area of Square:", square.calculate_area())
print("Area of Rectangle:", rectangle.calculate_area())
