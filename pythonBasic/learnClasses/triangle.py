from polygon import Polygon
from shape import Shape

class Triangle(Polygon, Shape):
    def area(self):
        return  1/2 * self.get_width() * self.get_height()