from abc import ABC, abstractmethod

class Shape (ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    
class Square(Shape):
    def __init__(self, width):
        self.width = width
        
    def area (self):
        return self.width * self.width
    
    def perimeter(self):
        return 4 * self.width
    
class Triangle(Shape):
    def __init__(self, length, height):
        self.length = length
        self.height = height
    
    def area(self):
        return 0.5 * self.length * self.height
    
    def perimeter(self):
       return self.length * 3
    
sq = Square(5)
print(sq.area())
print(sq.perimeter())

tg = Triangle(5,6)
print(tg.area())
print(tg.perimeter())
