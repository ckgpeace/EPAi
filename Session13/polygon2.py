import math
import polygon1 as pol1

class polygon2:
  '''
  This is Polygon Class. This class takes input number of edges (n)
  '''
  def __init__(self, n=None):
    if n is None or n<3:
      raise ValueError("Edges/vertices can not be none or less than 3")
    else:
      self.n = n

  def __repr__(self):
    ''' __repr__ function provides the basic info for this class Polygon'''

    return f'The class returns the area to perimeter ratio of series of polygons with same circumradius: 100 \n The total number of polygons in the series: {self.n-3}'
  
  def __len__(self):
    return self.n

  def __getitem__(self, s):
    if isinstance(s, int):
        if s < 0 or s >=self.n:
            raise IndexError
        else:
            return polygon2._eratio(s)

  @staticmethod #Static methods are methods that are bound to a class rather than its object.
  def _eratio(n):
    ''' The _eratio function returns ratio of area and perimeter of a  n-side polygon. The common circum radius taken as 100'''
    if n < 3:
        return 0
    else:
        p1 = pol1.polygon1(n,100)
        return p1.area/p1.perimeter

