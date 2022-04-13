import math

class Polygon:
    def __init__(self, n, c_r):

        self.edges = n
        self.circum_radius = c_r
    
    @property
    def edges(self):
        return self._edges

    @edges.setter
    def edges(self, n):
        if n <= 2:
            raise ValueError('Number of edges must be 3 or more.')
        else:
            self._edges = n

    @property
    def circum_radius(self):
        return self._circum_radius
     
    @circum_radius.setter
    def circum_radius(self, c_r):
        if c_r <= 0:
            raise ValueError('Number of edges must be positive.')
        else:
            self._circum_radius = c_r
    
    def __repr__(self):
        return f'Polygon(edges = {self.edges}, circumradius = {self.circum_radius})'
    
    @property
    def interior_angle(self):
        try:
            return self._interior_angle
        except:
            self.interior_angle_()
            return self._interior_angle

    def interior_angle_(self):
        self._interior_angle = (self.edges - 2) * (180/self.edges)
        self._interior_angle = round(self._interior_angle, 2)
    
    @property
    def edge_length(self):
        try:
            return self._edge_length
        except:
            self.edge_length_()
            return self._edge_length
    
    def edge_length_(self):
        self._edge_length = 2 * self.circum_radius * math.sin(math.pi/self.edges)
        self._edge_length = round(self._edge_length, 2)
    
    @property
    def apothem(self):
        try:
            return self._apothem
        except:
            self.apothem_()
            return self._apothem
    
    def apothem_(self):
        self._apothem = self.circum_radius * math.cos(math.pi/self.edges)
        self._apothem = round(self._apothem, 2)
    
    @property
    def area(self):
        try:
            return self._area
        except:
            self.area_()
            return self._area

    def area_(self):
        self.apothem
        self.edge_length
        self._area = (self.edges * self.edge_length * self.apothem)/2
        self._area = round(self._area, 2)
    
    @property
    def perimeter(self):
        try:
            return self._perimeter
        except:
            self.perimeter_()
            return self._perimeter

    def perimeter_(self):
        self.edge_length_()
        self._perimeter = self.edges * self.edge_length
        self._perimeter = round(self._perimeter, 2)
    
    def __eq__(self, other):
        if self.edges == other.edges and self.circum_radius == other.circum_radius:
            return True
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Polygon):
            return self.edges > other.edges
        else:
            raise TypeError('Object being compared not instance of Polygon')

if __name__ == '__main__':

    try:
        p1 = Polygon(1, 5)
    except Exception as e:
        print(e)
    
    try:
        p2 = Polygon(3, 5)
    except Exception as e:
        print(e)
    
    print(p2.interior_angle)
    print(p2.area)
    print(p2)

    try:
        p3 = Polygon(3, 5)
    except Exception as e:
        print(e)
    
    try:
        p4 = Polygon(4, 5)
    except Exception as e:
        print(e)
    
    print(f'Is {p2} equal to {p3}? {p2 == p3}')
    print(f'Is {p2} > {p4}? {p2 > p4}')