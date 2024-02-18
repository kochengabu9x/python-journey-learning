class Python :
    def __init__ (self, pages):
        self.pages = pages
    
    def __add__(self, other):
        return self.pages + other.pages
    
    def __gt__(self, other):
        return self.pages > other.pages
    
    def __sub__(self, other):
        return self.pages - other.pages

class Java:
    def __init__(self, pages):
        self.pages = pages
    

b1 = Python(100)
b2 = Java(150)

print(b1 + b2) # b1.__add__(b2)
print(b1 > b2) # b1.__gt__(b2)
print(b1 - b2) # b1.__sub__(b2)