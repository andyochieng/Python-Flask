from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def display_message(self):
        return "This is an abstract class"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Create a Rectangle instance
rect = Rectangle(10, 20)
print(rect.area())             # Output: 200
print(rect.perimeter())        # Output: 60
print(rect.display_message())  # Output: This is an abstract class
