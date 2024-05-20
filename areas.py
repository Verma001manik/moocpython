class Rectangle:
    def __init__(self, length , breadth):
        self.length = length 
        self.breadth = breadth

    def area(self):
        r = self.length * self.breadth
        return f"{r}"
    def __str__(self):
        return f"{self.length}x{self.breadth}"
    
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side,side)
        
        
square = Square(4)
print(square)
print("area:", square.area())