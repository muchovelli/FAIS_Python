import points as p


class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    # Chcemy, aby x1 < x2, y1 < y2.
    def __init__(self, x1, y1, x2, y2):
        self.pt1 = p.Point(x1, y1)
        self.pt2 = p.Point(x2, y2)

    # "[(x1, y1), (x2, y2)]"
    def __str__(self):
        return "[{0}, {1}]".format(self.pt1, self.pt2)

    # "Rectangle(x1, y1, x2, y2)"
    def __repr__(self):
        return "Rectangle({0}, {1}, {2}, {3})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    # obsługa rect1 == rect2
    def __eq__(self, other):
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    # obsługa rect1 != rect2
    def __ne__(self, other):
        return not self == other

    # zwraca środek prostokąta
    def center(self):
        return p.Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    # pole powierzchni
    def area(self):
        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

    # przesunięcie o (x, y)
    def move(self, x, y):
        return Rectangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y)

    # część wspólna prostokątów
    def intersection(self, other):
        if self.pt1.x > other.pt2.x or self.pt2.x < other.pt1.x or self.pt1.y > other.pt2.y or self.pt2.y < other.pt1.y:
            raise ValueError("No intersection")
        else:
            return Rectangle(max(self.pt1.x, other.pt1.x), max(self.pt1.y, other.pt1.y), min(self.pt2.x, other.pt2.x),
                             min(self.pt2.y, other.pt2.y))

    # prostąkąt nakrywający oba
    def cover(self, other):
        return (min(self.pt1.x, other.pt1.x), min(self.pt1.y, other.pt1.y), max(self.pt2.x, other.pt2.x),
                max(self.pt2.y, other.pt2.y))

    # zwraca krotkę czterech mniejszych
    # A-------B   po podziale  A---+---B
    # |       |                |   |   |
    # |       |                +---+---+
    # |       |                |   |   |
    # D-------C                D---+---C
    def make4(self):
        center = self.center()
        return (Rectangle(self.pt1.x, self.pt1.y, center.x, center.y),
                Rectangle(center.x, self.pt1.y, self.pt2.x, center.y),
                Rectangle(self.pt1.x, center.y, center.x, self.pt2.y),
                Rectangle(center.x, center.y, self.pt2.x, self.pt2.y))
