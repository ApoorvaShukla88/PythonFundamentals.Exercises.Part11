class Rectangle:
    def __init__(self, length, width):
        self.l = length
        self.w = width

        def area():
            return 2*length*width

        def perimeter():
            return 2*(length+width)


class Square(Rectangle):
    rect = shapes.Rectangle(2, 4)
    rect.area()




