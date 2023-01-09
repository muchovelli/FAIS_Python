from __future__ import annotations
from points import Point


class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    @classmethod
    def from_points(cls, points):
        if not isinstance(points, (list, tuple)):
            raise TypeError("Points must be list or tuple")
        if not all(isinstance(point, Point) for point in points):
            raise TypeError("Points must be list of Point")
        if len(points) != 2:
            raise ValueError("Points must be list of 2 Point")
        return cls(points[0].x, points[0].y, points[1].x, points[1].y)

    def __str__(self) -> str:
        return f'[{self.pt1}, {self.pt2}]'

    def __repr__(self):
        return f'Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})'

    def __eq__(self, other: Rectangle):
        return isinstance(other, Rectangle) and self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other: Rectangle):
        return not self == other

    @property
    def center(self):
        return Point((self.pt1 + self.pt2).x / 2, (self.pt1 + self.pt2).y / 2)

    @property
    def area(self):
        return abs(self.pt2.x - self.pt1.x) * abs(self.pt2.y - self.pt1.y)

    @property
    def top(self):
        return self.pt2.y

    @property
    def bottom(self):
        return self.pt1.y

    @property
    def left(self):
        return self.pt1.x

    @property
    def right(self):
        return self.pt2.x

    @property
    def width(self):
        return abs(self.pt2.x - self.pt1.x)

    @property
    def height(self):
        return abs(self.pt2.y - self.pt1.y)

    @property
    def top_left(self):
        return Point(self.pt1.x, self.pt2.y)

    @property
    def top_right(self):
        return Point(self.pt2.x, self.pt2.y)

    @property
    def bottom_left(self):
        return Point(self.pt1.x, self.pt1.y)

    @property
    def bottom_right(self):
        return Point(self.pt2.x, self.pt1.y)

    def move(self, x: float, y: float):
        move_pt = Point(x, y)
        self.pt1, self.pt2 = self.pt1 + move_pt, self.pt2 + move_pt

    def intersection(self, other: Rectangle):
        if not isinstance(other, Rectangle):
            raise TypeError("Other must be Rectangle")
        if self.pt1.x > other.pt2.x or self.pt2.x < other.pt1.x or self.pt1.y > other.pt2.y or self.pt2.y < other.pt1.y:
            raise ValueError("Rectangles do not intersect")
        else:
            return Rectangle(max(self.pt1.x, other.pt1.x), max(self.pt1.y, other.pt1.y), min(self.pt2.x, other.pt2.x),
                             min(self.pt2.y, other.pt2.y))

    def cover(self, other: Rectangle):
        if not isinstance(other, Rectangle):
            raise TypeError("Other must be Rectangle")
        return Rectangle(min(self.pt1.x, other.pt1.x), min(self.pt1.y, other.pt1.y), max(self.pt2.x, other.pt2.x),
                         max(self.pt2.y, other.pt2.y))

    def make4(self):
        return (
            Rectangle(self.pt1.x, self.center().y,
                      self.center().x, self.pt2.y),
            Rectangle(self.center().x, self.center().y,
                      self.pt2.x, self.pt2.y),
            Rectangle(self.center().x, self.pt1.y,
                      self.pt2.x, self.center().y),
            Rectangle(self.pt1.x, self.pt1.y, self.center().x, self.center().y))
