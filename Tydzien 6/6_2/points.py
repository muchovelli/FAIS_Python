import math


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  #
        self.x = x
        self.y = y

    # zwraca string "(x, y)"
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    # zwraca string "Point(x, y)"
    def __repr__(self):
        return "Point({0}, {1})".format(self.x, self.y)

    # obsługa point1 == point2
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # obsługa point1 != point2
    def __ne__(self, other):
        return not self == other

    # Punkty jako wektory 2D.

    # v1 + v2
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # v1 - v2
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # v1 * v2, iloczyn skalarny, zwraca liczbę
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
    def cross(self, other):
        return self.x * other.y - self.y * other.x

    # długość wektora
    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    # bazujemy na tuple, immutable points
    def __hash__(self):
        return hash((self.x, self.y))
