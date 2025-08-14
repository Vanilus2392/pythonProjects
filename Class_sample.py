class Shapes:
    def __init__(self, name):
        self.name = name
        
class Circle(Shapes):
    def __init__(self, radius):
        super().__init__(name = "Circle")
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
class Square(Shapes):
    def __init__(self, side):
        super().__init__(name = "Square")
        self.side = side
    
    def area(self):
        return self.side ** 2

class Triangle(Shapes):
    def __init__(self, base, height):
        super().__init__(name = "Triangle")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
    
def main():
    shapes = [
        Circle(radius=5),
        Square(side=4),
        Triangle(base=3, height=6)
    ]
    
    for shape in shapes:
        print(f"The area of the {shape.name} is: {shape.area()}")

if __name__ == "__main__":
    main()
