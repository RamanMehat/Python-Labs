# SYSC 1005 Fall 2013 Lab 11 Solutions
# Image processing filters that use lists

from Cimpl import *

#---------------------------------------------------------------
# Exercise 2
# Do not modify or delete any of the statements in this section.

black = create_color(0, 0, 0)
white = create_color(255, 255, 255)

red = create_color(255, 0, 0)
green = create_color(0, 255, 0)
blue = create_color(0, 0, 255)

cyan = create_color(0, 255, 255)
magenta = create_color(255, 0, 255)
yellow = create_color(255, 255, 0)

gray = create_color(128, 128, 128)

teal = create_color(0, 128, 128)
purple = create_color(128, 0, 128)
olive = create_color(128, 128, 0)

maroon = create_color(128, 0, 0)
navy = create_color(0, 0, 128)
other_green = create_color(0, 128, 0)
# Note: W3C names (0, 128, 0) as "green", but other organizations
# define green to be the primary colour (0, 255, 0), and don't name (0, 128, 0).
# To compound the confusion, W3C names (0, 255, 0) as "lime"...

# palette 1 - black and white and gray
palette_1 = [black, white, gray]

# palette 2 - the 8 RGB triplets composed of 0 and 255
palette_2 = [black, white, red, green, blue, cyan, magenta, yellow]

# palette 3 - the 8 RGB triplets composed of 0 and 128
palette_3 = [black, gray, teal, purple, olive, maroon, other_green, navy]

# palette 4 - a union of palettes 1 and 2 (15 colours).
palette_4 = [black, white, gray, red, green, blue, cyan, magenta, yellow,
             teal, purple, olive, maroon, other_green, navy]

# palette 5 - the 3 RGB triplets composed of two 0's and one 255
palette_5 = [red, green, blue]

# palette 6 - the 3 RGB triplets composed of one 0 and two 255's
palette_6 = [cyan, magenta, yellow]

# Write the definition of find_nearest_color here.

def distance (color1, color2):
    r1, g1, b1 = color1
    r2, g2, b2 = color2  
    return math.sqrt((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2)    

def find_nearest_color(color, palette):
    for i in range(1, len(palette)):
        closest = palette[0]
        if distance (color, palette[i]) < distance(color, palette[0]):
            closest = palette [i]
    return closest

# Write the definition of nearest_color_filter here.

def nearest_color_filter(img, palette):
    for x,y,col in img:
        r,g,b = col
        closest = find_nearest_color(col, palette)
        r,g,b = closest
        closest_col = create_color (r,g,b)
        set_color(img, x, y, closest_col)
         
#---------------------------------------------------------------
# Exercise 3
# Do not modify or delete any of the statements in this section.

def build_solarize_lookup_table(threshold):
    
    """ Return a lookup table for a solarizing filter.
    The table is initialized so that only those RGB components with intensities
    less than the specified threshold will be modified:
       For a component c, c < threshold, the new component value is 255 - c.
       For a component c, c >= threshold, the new component value is c; i.e,
       the component is unchanged.
    """
    lookup = []

    # Initialize the table so that, for component c, lookup[c] contains the
    # new value for that component.

    for c in range(256):
        if c < threshold:
            lookup.append(255 - c)
        else:
            lookup.append(c)

    return lookup

# Because the next three statements are defined outside of any function,
# they will be executed every time this module is loaded into the
# Python engine; e.g., by clicking Run. As such, three lookup tables
# for the solarizing function are created and bound to the three variables.

solarize_64_table = build_solarize_lookup_table(64)
solarize_128_table = build_solarize_lookup_table(128)
solarize_196_table = build_solarize_lookup_table(196)

def solarize(img, solarize_table):
    """
    Solarize the specified image, using lookup table solarize_table to
    obtain the RGB components for the solarized image.
    """
    for x, y, col in img:
        red, green, blue = col

        # Use the lookup table to find the solarized values of the
        # red, green and blue components.
        red = solarize_table[red]
        green = solarize_table[green]
        blue = solarize_table[blue]

        col = create_color(red, green, blue)
        set_color(img, x, y, col)

#---------------------------------------------------------
# Exercise 4
# Write the definition of build_hot_metal_lookup_table here.

def build_hot_metal_lookup_table():
    lookup = []
    
    for x in range(256):
        if x <= 170:
            r = 1.5*x
            g = 0
            b = 0
        else:
            r = 255
            g = 3*x - 510
    
        new_col = create_color(r, g, b)
        lookup.append(new_col)
    return lookup

hot_metal_table = build_hot_metal_lookup_table()

def hot_metal(img, table):
    for pixel in img:
        x, y, col = pixel
        r, g, b = col
        wbrightness = 0.3*r + 0.59*g + 0.11*b
        wbrightness = int(wbrightness)
        newcol = hot_metal_table[wbrightness]
        set_color(img, x, y, newcol)

# Write the definition of hot_metal here.

#---------------------------------------------------------
# Exercise 2

from math import *
	
def find_nearest_integer(lst,val):
    closest = lst[0]
    for element in lst:
        diff = abs(val - element)
        diff2 = abs(closest - val)
        if diff < diff2:
            closest = val
    return closest