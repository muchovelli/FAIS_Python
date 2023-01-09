from __future__ import annotations


class Point:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other: Point):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __ne__(self, other: Point):
        return not self == other

    def __add__(self, other: Point):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Point):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Point):
        return self.x * other.x + self.y * other.y

    def cross(self, other: Point):
        return self.x * other.y - self.y * other.x

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** (1/2)

    def __hash__(self):
        return hash((self.x, self.y))
