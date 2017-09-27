from math import *

def distance(point1, point2):
    x = point2[0] - point1[0] 
    y = point2[1] - point1[1]
    return sqrt((x**2) + (y**2))

def sum_lengths(points):
    x = 0
    for i in range(len(points)):
        tup = points[i]
        x = tup[0] + x
    return x 