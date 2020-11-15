# polygon1.py

import math

print("importing Polygon1 ....")
class polygon1:
  '''
  This is Polygon Class. This class takes input number of edges (n_edges) and circumradius(r_circum) of the Polygon.

  '''
  def __init__(self, n_edge=None, r_circum=None):
    
    ''' Defines the properties of the polygon as edge, circumradius, internal angle, apothem,  edge length, area and perimeter'''

    if n_edge is None or r_circum is None:
      raise ValueError("Edges/vertices or radius can not be none type")
    elif n_edge < 3 or r_circum <= 0:
      raise ValueError("Number of edges can not be less than 3 OR radius can not be less than negative")
    else:
      self.n_edge = n_edge
      self.r_circum = r_circum

  @property
  def count_vertices(self):
      return self.n_edge
  
  @property
  def count_edges(self):
      return self.n_edge
  
  @property
  def circumradius(self):
      return self.r_circum
  
  @property
  def int_angle(self):
      return (self.n_edge - 2) * 180 / self.n_edge

  @property
  def edge_len(self):
      return 2 * self.r_circum * math.sin(math.pi / self.n_edge)
  
  @property
  def apothem(self):
      return self.r_circum * math.cos(math.pi / self.n_edge)
  
  @property
  def area(self):
      return self.n_edge / 2 * self.edge_len * self.apothem
  
  @property
  def perimeter(self):
      return self.n_edge * self.edge_len


  # self.int_angle = 180*(n_edge-2)/n_edge
  # self.edge_len = 2*r_circum*(math.sin((math.pi)/n_edge))
  # self.apothem = r_circum*(math.cos((math.pi)/n_edge))
  # self.area = 0.5*n_edge*self.edge_len*self.apothem
  # self.perimeter = self.edge_len*n_edge
  # self.apr = (self.area/self.perimeter)

  
  def __repr__(self):
    ''' __repr__ function provides the basic info for this class Polygon'''
    return f'The Current Instance of Polygon has following properties: \n \
    Number of Edges: {self.n_edge} Circumradius: {self.r_circum} Internal Angle: {self.int_angle} Edge Length: {self.edge_len} Apothem: {self.apothem} Area: {self.area} and Perimeter: {self.perimeter}'

  def __eq__(self, other):
    ''' Compares the two instances of Polygon class'''
    return self.n_edge == other.n_edge and self.r_circum == other.r_circum

  def __gt__(self, other):
    ''' Compares the two instances of Polygon class'''
    if self.n_edge > other.n_edge:
      return True
    else:
      return False