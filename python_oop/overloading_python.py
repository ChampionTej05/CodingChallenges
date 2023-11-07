# python does not support method overloading but it supports operator overloading


# https://www.programiz.com/python-programming/operator-overloading
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #override existing method
    def __str__(self):
        return "[ {x} , {y}] ".format(x=self.x, y=self.y)

    # performs addition of two objects
    def __add__(self, other):
        total_x = self.x + other.x
        total_y = self.y + other.y
        return Point(total_x, total_y)

    def __mul__(self, other):

        total_x = self.x * other.x
        total_y = self.y * other.y
        return Point(total_x, total_y)

    def __lt__(self, other):
        # bitwise operators only for positive numbers
        self_dist = (self.x << 1) + (self.y << 1)
        other_dist = (other.x << 1) + (other.y << 1)

        return self_dist < other_dist

    def __gt__(self, other):
        # bitwise operators only for positive numbers
        self_dist = (self.x << 1) + (self.y << 1)
        other_dist = (other.x << 1) + (other.y << 1)

        return self_dist > other_dist

    def __eq__(self, other):
        # bitwise operators only for positive numbers
        self_dist = (self.x << 1) + (self.y << 1)
        other_dist = (other.x << 1) + (other.y << 1)

        return self_dist == other_dist


def do_point_calculation():
    point1 = Point(2, 3)
    point2 = Point(1, 3)

    print(point1)
    print(point2)

    # how to add two points ?
    print(point1 + point2)

    #multiplacation
    print(point1 * point2)

    # how to compare to points
    print(point1 < point2)
    print(point1 > point2)
    print(point1 == point2)


do_point_calculation()