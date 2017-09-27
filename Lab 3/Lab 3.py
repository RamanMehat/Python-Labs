import math

def area_of_disk(r):
   return math.pi * r ** 2

def area_of_ring(outer,inner):
   area_outer = area_of_disk(outer)
   area_inner = area_of_disk(inner)
   return area_outer - area_inner
 
def area_of_cone(h,r):
   return math.pi * r * math.sqrt(r ** 2 +h ** 2)

def volume_of_sphere(r):
   return (4/3) * math.pi * r ** 3

def hallow_sphere(larger,smaller):
   volume_larger = volume_of_sphere(larger)
   volume_smaller = volume_of_sphere(smaller)
   return volume_larger - volume_smaller
   
   
   