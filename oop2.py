# oop2

class Circle:
    def __init__(self, r:float): # setup
      self.radius = r

    def area(self):
        return 22/7 * self.radius**2

    def perimeter(self):
        return 22/7 * self.radius* 2

    def print_details(self):
        print("Radius is", self.radius)
        print("Area is",self.area())
        print("Perimeter",self.perimeter())

# objects == instance of a class == variable
c1 = Circle(10)
c2 = Circle(28)
c3 = Circle(40)

print(c1.area())
c1.print_details()

my_circles = [c1, c2, c3]
# branches -- copy -- master main
# feature ---