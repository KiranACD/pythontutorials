import math
from project1 import Polygon

class Polygons:
    def __init__(self, n, R):
        self.largest_polygon = n
        self.circum_radius = R
        self.num_polygons_()
    
    @property
    def largest_polygon(self):
        return self._largest_polygon

    @largest_polygon.setter
    def largest_polygon(self, n):
        if n < 3:
            raise ValueError('Polygon must have greater than 2 sides.')
        else:
            self._largest_polygon = n
    
    @property
    def circum_radius(self):
        return self._circum_radius

    @circum_radius.setter
    def circum_radius(self, R):
        if R <= 0:
            raise ValueError('Circumradius must be greater than 0.')
        else:
            self._circum_radius = R
    
    @property
    def num_polygons(self):
        try:
            return self._num_polygons
        except:
            self.num_polygons_()
            return self._num_polygons
    
    def num_polygons_(self):
        self._num_polygons = self.largest_polygon - 2

    @property
    def max_efficiency_polygon(self):

        max_efficiency = 0
        polygon = None

        for p in self:
            efficiency = p.area/p.perimeter
            if efficiency > max_efficiency:
                max_efficiency = efficiency
                polygon = p
        
        max_efficiency = round(max_efficiency, 2)
        
        return polygon, max_efficiency

        # n = 3
        # while True:
        #     if n > self.n_edges:
        #         break
        #     p = Polygon(n, self.circum_radius)
        #     efficiency = p.area/p.perimeter
        #     if efficiency > max_efficiency:
        #         max_efficiency = efficiency
        #         polygon = p
        #     n += 1
        
        # return polygon
    
    def __len__(self):
        return self.num_polygons
    
    def __getitem__(self, s):

        if isinstance(s, int):

            if s < 0:
                s = s + self.num_polygons

            if s < 0 or s >= self.num_polygons:
                raise IndexError('Out of bounds')
            else:
                return Polygon(s+3, self.circum_radius)

        elif isinstance(s, slice):

            start, end, step = s.indices(self.num_polygons - 1)
            print(start, end, step)
            if step > 0:

                if start < 0 or end >= self.num_polygons:
                    raise IndexError('Out of bounds')
            else:

                if start >= self.num_polygons or end < 0:
                    raise IndexError('Out of bounds')

            l = []
            n = start + 3

            while True:
                if step > 0:
                    if n > end + 3:
                        break
                else:
                    if n < end + 3:
                        break

                l.append(Polygon(n, self.circum_radius))
                n += step
            return l

if __name__ == '__main__':

    poly_list = Polygons(10, 10)

    n = len(poly_list)
    print(n)


    print(poly_list[5])
    print(poly_list[0])
    try:
        print(poly_list[n])
    except Exception as e:
        print(e)

    try:
        print(poly_list[-n])
    except Exception as e:
        print(e)

    print(poly_list[-1])

    print(poly_list[:])
    print(poly_list[1:2])
    print(poly_list[3:3])
    print(poly_list[1:5:2]) 
    print(poly_list[-1:-5:-1])

    print(poly_list.max_efficiency_polygon)

    for p in poly_list:
        print(p)

