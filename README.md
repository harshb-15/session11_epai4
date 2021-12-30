# EPAi4.0 Session 11
GitHub Profile : [harshb-15](https://github.com/harshb-15)

Colab Link : [GoogleColab]()
## Iterables and Iterators
This assignment is to be done on top of previous assignment.
1. We have to make some changes in Polygon classes such that it's attributes are lazily calculated.
2. We also have  to make some changes in PolygonSeq class to transform it into an iterable which produces Polygon Iterators. It's elements too should be lazily computed.
## Part 1
### Making a Polygon class
```
    def __init__(self, sides, radius):
        if sides < 3:
            raise TypeError("Number of Edges should be more than 2")
        self._sides = sides
        self._radius = radius
        self._intangle = None
        self._sidelength = None
        self._apothem = None
        self._area = None
        self._perimeter = None
```
This class takes in Sides and Circumradius and will produce its properties when they are needed. 

Properties' name starts with `_` to tell other developers not to get or set values directly. Use getters/setters made below.
Polygon starts with minimum 3 sides.
```
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
```
Adding `@property` in front of a method makes it a getter method for a variable. Hence, it is only calculated when it's value has found to be `None` ie. never been calculated before
```
    def __repr__(self):
        return f"Regular Convex Polygon : Sides = {self.sides}, Radius = {self.radius}, Angle = {self.intangle} degrees, Side Length = {self.sidelength}, Apothem = {self.apothem}, Area = {self.area}, Perimeter = {self.perimeter}"
```
`__repr__` function to properly represent it. It calculates and mentions all of it's attributes.
```
    def __gt__(self, other):
        if self.sides > other.sides:
            return True
        else:
            return False
```
One Polygon is bigger than other simply if its sides is more than others.
```
    def __eq__(self, other):
        if self.sides == other.sides and self.radius == other.radius:
            return True
        else:
            return False
```
If Polygons have same number of sides and radius then they are called equal.
## Part 2
### Making PolygonSeq class
```
    def __init__(self, maxsides, radius):
        self._maxsides = maxsides
        self._radius = radius
```
Sequence of Polygons provided with the highest number of sides in a Polygon and common radius is PolygonSeq class.
Its properties too should not be fiddled with directly by other developers working on the project, so we have written `_` in front of the variables.
```
@property
    def radius(self):
        return self._radius

    @property
    def maxsides(self):
        return self._maxsides
```
Getters for the attributes have been made with `@property` decorator.
```
    def __iter__(self):
        return self.PolygonSeqIter(self.maxsides, self.radius)
```
`__iter__` function is used by `for loop` to provide `__next__` of which class should be used for the iteration.
So the `__next__` of `PolygonSeqIter` is used for iteration.
```
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
```
The `__next__` method will create Polygons according the inputs(sides,radius) provided one by one.

`PolygonSeqIter` is an Iterator while `PolygonSeq` is an Iterable.
```
    def getmaxeffpoly(self):
        mx = -1
        mxp = -1
        for i in self:
            ratio = i.area / i.perimeter
            if ratio >= mx:
                mxp = i
                mx = ratio
        return f"Maximum Efficiency Polygon with ratio {round(mx, 2)} is {mxp} "
```
This will return the Polygon with Maximum Efficiency ie. the highest ratio of Area:Perimeter.
This is done by Looping through all the Polygons, calculating the ratio and comparing at each step.
```
    def __repr__(self):
        return f"Polygon Sequence :- Common Radius: {self.radius}, Max Number of Edges: {self.maxsides}, Number of Polygons: {len(self)} "
```
Repr function to represent whole PolygonSeq.

### How to run the file
1. `pyTest` is needed to run the `test_session11.py`, so `pip install pytest` will do the job. 
2. Clone all files to your local repository.
3. Open a terminal in that repository and type in `python -m pytest test-session11.py` and press enter.
