
from collections import namedtuple
import numbers

class Point:
    def __init__(self, x, y):
        if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
            self._pt = (x, y)
        else:
            raise TypeError('Point co-ordinates must be real numbers.')
    
    def __repr__(self):
        return f'Point(x={self._pt[0]}, y={self._pt[1]})'
    
    def __len__(self):      
        return len(self._pt)
    
    def __getitem__(self, s):
        return self._pt[s]

class Polygon:
    def __init__(self, *pts):
        if pts:
            self._pts = [Point(*pt) for pt in pts]
        else:
            self._pts = []
        
    def __repr__(self):
        rep_str = ', '.join([str(pt) for pt in self._pts])
        return f'Polygon({rep_str})'
    
    def __len__(self):
        return len(self._pts)
    
    def __getitem__(self, s):
        return self._pts[s]

    def __setitem__(self, s, pts):

        try:
            rhs = Point(*pts)
            is_single = True
        except TypeError:
            try:
                rhs = [Point(*pt) for pt in pts]
                is_single = False
            except TypeError:
                raise TypeError('Invalid Point or iterable of of Points')
        
        if (isinstance(s, int) and is_single) or (isinstance(s, slice) and not is_single):
            self._pts[s] = rhs
        else:
            raise TypeError('Incompatible assignment with index/slice')

    def __add__(self, other):
        if isinstance(other, Polygon):
            new_pts = self._pts + other._pts
            return Polygon(*new_pts)
        else:
            raise TypeError('Can only concatenate with another Polygon.')
    
    def __iadd__(self, other):
        self.extend(other)
        return self
    
    def append(self, pt):
        self._pts.append(Point(*pt))
    
    def insert(self, i, pt):
        
        self._pts.insert(i, Point(*pt))
        # self._pts[i:i] = Point(*pt)
    
    def extend(self, pts):
        if isinstance(pts, Polygon):
            self._pts += pts._pts
        else:
            points = [Point(*pt) for pt in pts]
            self._pts += points
    

if __name__ == '__main__':
    p1 = Point(1, 2)
    p2 = Point(5, 10)
    print(p1, p2)
    p3 = Point(13, 12)
    p4 = Point(1, -10)

    poly1 = Polygon(p1, p2)
    poly2 = Polygon(p3, p4)

    print(poly1, id(poly1))
    print(poly2, id(poly2))
    new_poly = poly1 + poly2
    print(new_poly, id(new_poly))
    poly1 += poly2
    print(poly1, id(poly1))
    
    print()
    
    poly3 = Polygon((10, 10), Point(20, 20), Point(3, 4))

    print(poly3)
    poly1.append(Point(100, 100))
    print(poly1)
    poly1.insert(1, Point(10, 2))
    print(poly1)
    poly1.extend(poly2)
    print(poly1)

    poly1[0] = Point(500, 500)
    print(poly1)

    try:
        poly1[0] = poly3
    except Exception as e:
        print(e)
    
    try:
        poly1[0:2] = Point(0, 0)
    except Exception as e:
        print(e)
    
    try:
        poly1[0] = ('a', 'b')
    except Exception as e:
        print(e)

    poly1[0] = Point('a', 'b')
