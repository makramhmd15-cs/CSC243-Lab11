from Point import Point

class Rectangle:

    def __init__(self, p, q):
        assert isinstance(p, Point) and isinstance(q, Point), "Bad input!"
        assert p.x <= q.x and p.y <= q.y, "Bad input!"

        self.p = p
        self.q = q

    def __str__(self):
        return "(p=" + str(self.p) + ", q=" + str(self.q) + ")"

    def get_width(self):
        return self.q.x - self.p.x

    def get_height(self):
        return self.q.y - self.p.y

    def perimeter(self):
        return 2 * (self.get_width() + self.get_height())

    def area(self):
        return self.get_width() * self.get_height()

    def contains(self, pt):
        assert isinstance(pt, Point), "Bad Input!"

        if self.p.x <= pt.x and pt.x <= self.q.x:
            if self.p.y <= pt.y and pt.y <= self.q.y:
                return True

        return False