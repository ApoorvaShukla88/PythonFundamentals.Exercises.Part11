class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        ar = self.length * self.width
        print(ar)

    def perimeter(self):
        peri = 2 * (self.length + self.width)
        print(peri)


class Square(Rectangle):

    def __init__(self, width):

        self.width = width
        self.length = width



rect = Rectangle(2, 4)
rect.area()
#8
square = Square(8)
square.area()
#64
square.perimeter()
#32