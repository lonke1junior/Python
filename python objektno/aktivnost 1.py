#OOP
#import math
from math import *
class tocka:
  
  def __init__(self, x, y):#konstruktor
     
     self.x = x
     self.y = y
  
  def udaljenost(self):
    return (self.x)*(self.x) + (self.y)*(self.y)

  def xkoord(self):
    return (self.x)

  def euklid(self):
    return sqrt(self.udaljenost())

  def test(self, other):
    a = self.udaljenost()
    b = other.udaljenost()
    if (a > b):
      return self.x
    else:
      return other.x
  def __str__(self):
    return '{},{}'.format(self.x,self.y)

  def __lt__(self, other):
    return self.udaljenost() < other.udaljenost()
    
lista = []
n = int(input())
t = tocka(3,4)
print(t.x,t.y)
print(t)
for i in range (0, n, 1):
  a = int(input())
  b = int(input())
  t = tocka(a,b)
  lista.append(t)
lista.sort()
for k in lista:
  print(k)