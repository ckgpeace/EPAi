# polygon2.py

import polygon1 as poly1
from collections import namedtuple
import math

Polylist = namedtuple('Edge', 'A_P_ratio')

class polygon2:
    def __init__(self, m, R):
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._R = R
        # self._polygons = [Polygon(i, R) for i in range(3, m+1)]
        
    def __len__(self):
        return self._m - 2

    def __iter__(self):
        return self.PolygonIterator(self._m)

    def __repr__(self):
        return f'Polygons(m={self._m}, R={self._R})'


    def __reversed__(self):
        return self.PolygonIterator(self._m,self._R, reverse=True)

    @property
    def max_efficiency_polygon(self):
        poly_list = list(self.PolygonIterator(self._m, self._R))
        return poly_list.index(max(poly_list)), max(poly_list)


    class PolygonIterator:
        def __init__(self, m, R, reverse=False):
            self._m = m
            self._R = R
            self.reverse = reverse
            self.i = 0

        def __iter__(self):
            return self
        
        def __next__(self):
            if self.i >= self._m:
                raise StopIteration
            else:
                if self.reverse:
                    index = self._m -1 - self.i
                else:
                    index = self.i
                
                if self.i <3:
                    self.e_ratio = 0
                else:
                    p1 = poly1.polygon1(self.i,self._R)
                    self.e_ratio = p1.area/p1.perimeter
                
                self.i += 1
                
                self.max_eratio = 0
                if self.e_ratio> self.max_eratio:
                    self.max_eratio = self.e_ratio

                return (self.max_eratio)