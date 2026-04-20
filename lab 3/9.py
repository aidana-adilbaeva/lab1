class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self, pi = 3.14159):
        return pi * (self.radius**2)

radius = int(input())
circle = Circle(radius)

area = circle.area()
print(f"{area:.2f}")