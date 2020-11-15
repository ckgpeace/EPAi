#polygon1.py

import math
class polygon1:
    def __init__(self, n, R):
        if n < 3 or R <= 0:
            raise ValueError('Polygon must have at least 3 vertices or negative/zero Radius')
        self._n = n
        self._R = R
        self.circum = R
        
    def __repr__(self):
        return f'Polygon(n={self._n}, R={self._R})'
    
    
    @property
    def count_vertices(self):
        return self._n
    
    @property
    def count_edges(self):
        return self._n
    
    @property
    def circumradius(self):
        return self._R
    
    @property
    def circum(self):
        return self._circum

    @circum.setter
    def circum(self, R):
        # print("Setter is set.")
        self._R = R
        self._interior_angle = None
        self._side_length = None
        self._apothem = None
        self._area = None
        self._perimeter = None

    @property
    def interior_angle(self):
        if self._interior_angle is None:
            # print('1st time calculating: Int Angle...')
            self._interior_angle = (self._n - 2) * 180 / self._n
        return self._interior_angle

    @property
    def side_length(self):
        if self._side_length is None:
            # print('1st time calculating: side_length ...')
            self._side_length = 2 * self._R * math.sin(math.pi / self._n)
        return self._side_length
    
    @property
    def apothem(self):
        if self._apothem is None:
            # print('1st time calculating: apothem ...')
            self._apothem = self._R * math.cos(math.pi / self._n)
        return self._apothem
    
    @property
    def area(self):
        if self._area is None:
            # print('1st time calculating: area ...')
            self._area = self._n / 2 * self.side_length * self.apothem
        return self._area
        
    @property
    def perimeter(self):
        if self._perimeter is None:
            # print('1st time calculating: Perimeter ...')
            self._perimeter = self._n * self.side_length
        return self._perimeter