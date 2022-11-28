import math

from points import Point


class Triangle:
    """Klasa reprezentująca trójkąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    # "[(x1, y1), (x2, y2), (x3, y3)]"
    def __str__(self):
        return "[{0}, {1}, {2}]".format(self.pt1, self.pt2, self.pt3)

    # "Triangle(x1, y1, x2, y2, x3, y3)"
    def __repr__(self):
        return "Triangle({0}, {1}, {2}, {3}, {4}, {5})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y,
                                                               self.pt3.x,
                                                               self.pt3.y)

    # Obsługa tr1 == tr2
    # Trójkąty powinny być równe, jeżeli mają ten sam zbiór wierzchołków,
    # niezależnie od kolejności pt1, pt2, pt3.
    def __eq__(self, other):
        return self.pt1 in [other.pt1, other.pt2, other.pt3] and self.pt2 in [other.pt1, other.pt2,
                                                                              other.pt3] and self.pt3 in [
                   other.pt1, other.pt2, other.pt3]

    # obsługa tr1 != tr2
    def __ne__(self, other):
        return not self == other

    # zwraca środek (masy) trójkąta
    # write a functio nwhich returns the center of mass of a triangle
    def center(self):
        return Point((self.pt1.x + self.pt2.x + self.pt3.x) / 3, (self.pt1.y + self.pt2.y + self.pt3.y) / 3)

    # przesunięcie o (x, y)
    def move(self, i, k):
        return Triangle(self.pt1.x + i, self.pt1.y + k, self.pt2.x + i, self.pt2.y + k, self.pt3.x + i, self.pt3.y + k)

    # pole powierzchni
    def area(self):
        return (math.fabs((self.pt2.x - self.pt1.x) * (self.pt3.y - self.pt1.y) - (self.pt2.y - self.pt1.y) * (
                self.pt3.x - self.pt1.x))) / 2
