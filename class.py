import math


class Apple:
    def __init__(self, color, size, day, type):
        self.color = color
        self.size = size
        self.day = day
        self.type = type


apple1 = Apple("red", 25, 5, "good")

print(apple1.color)


class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return math.pi * self.radius ** 2


circle = Circle(25)
print(circle.area())


class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        p = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(abs(p * (p - self.side1) * (p - self.side2) * (p - self.side3)))


tr = Triangle(4, 5, 2)
print(tr.area())


class Hexagon:
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6

    def calculate_perimeter(self):
        return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6


hexagon = Hexagon(2, 5, 7, 3, 6, 5)

print(hexagon.calculate_perimeter())


class Shape:
    def what_am_i(self):
        print("Я - фигура")


class Rectangle(Shape):
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def calculate_perimeter(self):
        return (self.width + self.height) * 2

    def change_size(self, w, h):
        self.width += w
        self.height += h


class Square(Shape):
    square_list = list()

    def __init__(self, s):
        self.square_list.append(self)
        self.side = s

    def calculate_perimeter(self):
        return self.side * 4

    def __repr__(self):
        return ((str(self.side) + " на ") * 3) + (str(self.side))


rect = Rectangle(100, 200)
rect.change_size(20, 20)
rect.what_am_i()
print(rect.calculate_perimeter())

square = Square(2098098)
square.what_am_i()
print(square.calculate_perimeter())


class Rider:
    def __init__(self, n):
        self.name = n


class Horse:
    def __init__(self, n, r):
        self.name = n
        self.rider = r

    def print_rider(self):
        print(self.rider)


rider = Rider("Jon")

horse = Horse("Niki", rider.name)
horse.print_rider()

print(square)


def it_is_equal(obj1, obj2):
    return obj1 is obj2


print(it_is_equal(square, rider))
