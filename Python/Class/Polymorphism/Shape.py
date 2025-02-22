class Shape:
    def area(self):
        pass 
    
    def perimeter(self):
        pass 
    
class Square(Shape):
    
    def __init__(self,side):
        self.side = side
        
    def area(self):
        return self.side*self.side
    
    def perimeter(self):
        return 4*self.side

class Cirlce(Shape):
    
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        return 3.14*self.radius*self.radius
    
    def perimeter(self):
        return 2*3.14*self.radius
    
circle = Cirlce(3)
print(circle.area())
print(circle.perimeter())

square = Square(4)
print(square.area())
print(square.perimeter())