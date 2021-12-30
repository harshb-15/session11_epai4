# I did not use my Previous Assignment Code. I am writing this from scratch.

import math


class Polygon:
    def __init__(self, sides, radius):
        if sides < 3:
            raise ValueError("Number of Edges should be more than 2")
        self._sides = sides
        self._radius = radius
        self._intangle = None
        self._sidelength = None
        self._apothem = None
        self._area = None
        self._perimeter = None

    @property
    def radius(self):
        return self._radius

    @property
    def sides(self):
        return self._sides

    @property
    def intangle(self):
        return round(((self.sides - 2) * 180) / self.sides, 2) if self._intangle is None else self._intangle

    @property
    def sidelength(self):
        return round(2 * self._radius * math.sin(math.pi / self.sides),
                     2) if self._sidelength is None else self._sidelength

    @property
    def apothem(self):
        return round(self._radius * math.cos(math.pi / self.sides), 2) if self._apothem is None else self._apothem

    @property
    def area(self):
        return round((self.sides * self.sidelength * self.apothem) / 2, 2) if self._area is None else self._area

    @property
    def perimeter(self):
        return round(self.sides * self.sidelength, 2) if self._perimeter is None else self._perimeter

    def __repr__(self):
        return f"Regular Convex Polygon : Sides = {self.sides}, Radius = {self.radius}, Angle = {self.intangle} degrees, Side Length = {self.sidelength}, Apothem = {self.apothem}, Area = {self.area}, Perimeter = {self.perimeter}"

    def __eq__(self, other):
        if self.sides == other.sides and self.radius == other.radius:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.sides > other.sides:
            return True
        else:
            return False


class PolygonSeq:
    def __init__(self, maxsides, radius):
        self._maxsides = maxsides
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def maxsides(self):
        return self._maxsides

    def __iter__(self):
        return self.PolygonSeqIter(self.maxsides, self.radius)

    class PolygonSeqIter:
        def __init__(self, maxsides, radius):
            self._maxsides = maxsides
            self._radius = radius
            self.poly_number = 2

        def __next__(self):
            self.poly_number += 1
            if self.poly_number > self._maxsides:
                raise StopIteration
            else:
                return Polygon(self.poly_number, self._radius)

    def __len__(self):
        return self.maxsides - 2

    def __repr__(self):
        return f"Polygon Sequence :- Common Radius: {self.radius}, Max Number of Edges: {self.maxsides}, Number of Polygons: {len(self)} "

    def getmaxeffpoly(self):
        mx = -1
        mxp = -1
        for i in self:
            ratio = i.area / i.perimeter
            if ratio >= mx:
                mxp = i
                mx = ratio
        return f"Maximum Efficiency Polygon with ratio {round(mx, 2)} is {mxp} "
