"""SYSC 1005 Fall 2013 Lab 9"""

def get_points():
    """ Return a list of (x, y) points, with each point stored in a tuple.
    """
    return [(1.0, 5.0), (2.0, 8.0), (3.5, 12.5)]

def fit_line_to_points(points):
    sumx = 0
    sumy = 0
    sumxx = 0
    sumxy = 0
    n = len(points)
    
    for i in range(len(points)): 
        p = points[i]
        sumx = sumx + p[0]
        sumy = sumy + p[1]
        sumxx = sumxx + (p[0]**2)
        sumxy = sumxy +(p[0]* p[1])
        
        
        m = ((sumx * sumy) - (n * sumxy))/((sumx * sumx) - (n * sumxx))
        b = ((sumx * sumxy) - (sumxx * sumy))/((sumx * sumx) - (n * sumxx)) 
   
    return m,b 

if __name__ == "__main__":
    points = get_points()
    m,b = fit_line_to_points(points)
    
    print ("The best fit line is y = " + str(m)+ "x + " + str(b))