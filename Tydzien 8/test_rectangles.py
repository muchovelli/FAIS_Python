import rectangles as rectangle


def test_from_points():
    assert rectangle.Rectangle.from_points([(0, 0), (1, 1)]) == rectangle.Rectangle(0, 0, 1, 1)
    assert rectangle.Rectangle.from_points([(0, 0), (1, 1), (2, 2)]) == rectangle.Rectangle(0, 0, 2, 2)
    assert rectangle.Rectangle.from_points([(0, 0), (1, 1), (2, 2), (3, 3)]) == rectangle.Rectangle(0, 0, 3, 3)
    assert rectangle.Rectangle.from_points([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]) == rectangle.Rectangle(0, 0, 4, 4)


def test_properties():
    r = rectangle.Rectangle(1, 2, 3, 4)
    assert r.top == 4
    assert r.bottom == 2
    assert r.left == 1
    assert r.right == 3
    assert r.width == 2
    assert r.height == 2
    assert r.top_left == rectangle.Point(1, 4)
    assert r.top_right == rectangle.Point(3, 4)
    assert r.bottom_left == rectangle.Point(1, 2)
    assert r.bottom_right == rectangle.Point(3, 2)
    assert r.center == rectangle.Point(2, 3)
