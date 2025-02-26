class Shape:
    def __init__(self):
        pass
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth
    
circle = Circle(7)
rectangle = Rectangle(5,6)

print(circle.area())
print(rectangle.area())